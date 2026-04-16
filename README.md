# Agri Loan Assist

Agri Loan Assist is a Flask-based web application designed to help farmers explore agricultural loan guidance based on their crop type, land size, region, loan purpose, loan amount, farming experience, and current loan status. It also includes farmer registration, login, and dashboard features backed by a MySQL database.

> This project is built as a practical agricultural support dashboard for exploring loan-related guidance and farmer-specific recommendations.

---

## Preview

Agri Loan Assist follows a simple user flow:

1. Open the home page
2. Register as a farmer or log in with an existing account
3. Access the dashboard after login
4. Submit loan-related details such as crop, land size, region, purpose, amount, and experience
5. Receive tailored loan guidance and recommendations based on the submitted inputs

The app stores farmer records and submitted loan guidance inputs using MySQL.

---

## Features

* Flask web application with template-based frontend
* Farmer registration and login system
* Session-based dashboard access
* MySQL-backed data storage
* Database initialization script for farmer records
* Rule-based agricultural loan guidance engine
* Recommendations based on crop, land size, region, purpose, amount, and loan status
* User query submission support for loan-related questions

---

## How It Works

### 1. Farmer registration and login

Users can create a farmer account using personal and agricultural details such as name, mobile number, location, land area, and crop. Registered users can then log in to access their dashboard.

### 2. Dashboard access

After a successful login, the user is redirected to a dashboard that displays stored farmer details fetched from the MySQL database.

### 3. Loan guidance analysis

The app accepts agricultural and loan-related inputs including:

* crop
* land size
* region
* loan purpose
* loan amount
* farming experience
* existing loan status

These values are analyzed using rule-based recommendation dictionaries defined in `main.py`.

### 4. Recommendation generation

The app combines recommendations from multiple categories such as crop analysis, land analysis, region analysis, purpose analysis, and amount analysis, then renders the results on the loan guidance page.

### 5. Database usage

The project uses MySQL to:

* store farmer registration data
* store submitted loan guidance input data
* store user-submitted loan-related questions

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ackerman-sh/Agri-loan-assist.git
cd AgriLoanAssist
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Make sure MySQL is running

Create a MySQL database named `AgroLoan` before running the project.

### 5. Initialize the database

```bash
python initDB.py
```

### 6. Run the project

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
AgriLoanAssist/
├── app.py
├── main.py
├── initDB.py
├── requirements.txt
├── templates/
│   ├── dashboard.html
│   ├── index.html
│   ├── loan_guidance.html
│   ├── loans_applicable.html
│   ├── login.html
│   └── register.html
├── README.md
└── .gitignore
```

---

## Author

**ackerman-sh**
GitHub: `https://github.com/ackerman-sh`
