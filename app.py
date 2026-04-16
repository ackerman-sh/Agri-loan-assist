from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
from urllib.parse import quote_plus
from main import *

app = Flask(__name__)
app.secret_key = "your-secret-key-here"

# Encode password for safety
DB_PASSWORD = "!akaliXackerman"
ENCODED_DB_PASSWORD = quote_plus(DB_PASSWORD)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": DB_PASSWORD,
    "database": "AgroLoan",
    "charset": "utf8mb4",
    "collation": "utf8mb4_general_ci"
}

def getCC():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        return conn, cursor
    except mysql.connector.Error as e:
        print(f"Connection Error: {e}")
        return None, None

# ---------------- DB Utility Functions ----------------

def register_farmer(name, mobile, password, location, land_area, crop):
    conn, cursor = getCC()
    if not conn or not cursor:
        return "Database connection failed."
    try:
        cursor.execute("SELECT id FROM farmers WHERE mobile = %s", (mobile,))
        if cursor.fetchone():
            return "Farmer already exists."

        cursor.execute("""
            INSERT INTO farmers (name, mobile, password, location, land_area, crop)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, mobile, password, location, land_area, crop))
        conn.commit()
        return "Registered successfully."
    except mysql.connector.Error as err:
        return f"Database Error: {err}"
    finally:
        cursor.close()
        conn.close()


def validate_farmer_login(mobile, password):
    conn, cursor = getCC()
    if not conn or not cursor:
        return False
    try:
        cursor.execute("SELECT password FROM farmers WHERE mobile = %s", (mobile,))
        result = cursor.fetchone()
        return result and result['password'] == password
    finally:
        cursor.close()
        conn.close()

# ---------------- Routes ----------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    msg = None
    if request.method == "POST":
        try:
            name = request.form["name"]
            mobile = request.form["mobile"]
            password = request.form["password"]
            location = request.form["location"]
            land_area = request.form["land_area"]
            crop = request.form["crop"]
            msg = register_farmer(name, mobile, password, location, land_area, crop)
        except Exception as e:
            msg = f"Form Error: {e}"
    return render_template("register.html", msg=msg)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        mobile = request.form["mobile"]
        password = request.form["password"]
        if validate_farmer_login(mobile, password):
            session["loggedin"] = True
            session["mobile"] = mobile
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid mobile number or password"
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if not session.get("loggedin"):
        return redirect(url_for("login"))

    mobile = session["mobile"]
    conn, cursor = getCC()
    farmer = {}
    if not conn or not cursor:
        return "Database connection failed."
    try:
        cursor.execute("""
            SELECT name, location, land_area, crop, created_at 
            FROM farmers 
            WHERE mobile = %s
        """, (mobile,))
        farmer = cursor.fetchone()
    except mysql.connector.Error as err:
        return f"Database Error: {err}"
    finally:
        cursor.close()
        conn.close()

    return render_template("dashboard.html", farmer=farmer)

# ---------------- Loan Guidance ----------------

@app.route("/loan-guidance", methods=["GET", "POST"])
def loan_guidance():
    if request.method == "POST":
        answers = {k: request.form[k] for k in ["crop","land","region","loanPurpose","loanAmount","experience","existingLoan"]}
        session['answers'] = answers

        conn, cursor = getCC()
        if not conn or not cursor:
            return "Database connection failed."
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    crop VARCHAR(255),
                    land_area DECIMAL(10,2),
                    region VARCHAR(255),
                    loan_purpose VARCHAR(255),
                    loan_amount INT,
                    experience VARCHAR(255),
                    existing_loan VARCHAR(50),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("""
                INSERT INTO user_data (crop, land_area, region, loan_purpose, loan_amount, experience, existing_loan)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, (answers['crop'], answers['land'], answers['region'], answers['loanPurpose'], answers['loanAmount'], answers['experience'], answers['existingLoan']))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

        raw_results = [
            get_crop_analysis(answers['crop']),
            analyze_land_size(float(answers['land'])),
            analyze_region(answers['region']),
            analyze_loan_purpose(answers['loanPurpose']),
            analyze_loan_amount(answers['loanAmount']),
            analyze_experience(answers['experience']),
            analyze_loan_status(answers['existingLoan'])
        ]

        analysis_results = []
        for res in raw_results:
            if isinstance(res, dict):
                for k,v in res.items():
                    if isinstance(v,list):
                        for item in v:
                            analysis_results.append(f"{k.capitalize()}: {item}")
                    else:
                        analysis_results.append(f"{k.capitalize()}: {v}")
            elif isinstance(res, list):
                analysis_results.extend(res)
            elif isinstance(res, str):
                analysis_results.append(res)

        return render_template("loan_guidance.html", analysis_results=analysis_results)

    return render_template("loan_guidance.html", analysis_results=[])

# ---------------- Ask Question ----------------

@app.route("/ask-question", methods=["POST"])
def ask_question():
    question = request.form.get("question")
    if not question:
        return "No question submitted", 400

    conn, cursor = getCC()
    if not conn or not cursor:
        return "Database connection failed."
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS loan_queries (
                id SERIAL PRIMARY KEY,
                question TEXT NOT NULL,
                submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("INSERT INTO loan_queries (question) VALUES (%s)", (question,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    return redirect("/dashboard")

@app.route("/loans_applicable")
def loans_applicable():
    return render_template('loans_applicable.html')

if __name__ == "__main__":
    app.run(debug=True)
