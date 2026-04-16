crop_analysis = {
    "paddy": {
        "type": "Water-intensive",
        "recommend": [
            "Look for irrigation-based schemes like PMKSY.",
            "Eligible for crop insurance under PMFBY.",
            "Subsidy on transplanting machinery (in some states)."
        ]
    },
    "sugarcane": {
        "type": "Cash crop, water-intensive",
        "recommend": [
            "Eligible for drip irrigation subsidies.",
            "Check for state-level sugarcane farmer benefits.",
            "Consider long-term working capital loans."
        ]
    },
    "wheat": {
        "type": "Staple crop",
        "recommend": [
            "Standard short-term crop loans available.",
            "Eligible for MSP support and crop insurance.",
            "Requires moderate water, less subsidy-oriented."
        ]
    },
    "cotton": {
        "type": "Commercial crop",
        "recommend": [
            "Eligible for PMFBY (prone to pest issues).",
            "Look for input cost subsidies (fertilizers, seeds)."
        ]
    },
    "vegetables": {
        "type": "Perishable, market-linked",
        "recommend": [
            "KCC loans ideal due to quick cycle.",
            "State schemes may support cold storage or logistics.",
            "Organic/niche farming schemes if applicable."
        ]
    },
    "millets": {
        "type": "Climate-resilient",
        "recommend": [
            "Promoted under National Food Security Mission.",
            "Schemes for dryland farming regions.",
            "Lower water need, eco-supportive grants."
        ]
    },
    "fruits": {
        "type": "Horticulture",
        "recommend": [
            "Eligible under National Horticulture Board (NHB).",
            "Subsidy available for planting material & irrigation.",
            "Longer ROI — check for term-based agri credit."
        ]
    },
    "organic": {
        "type": "Niche/agroecology",
        "recommend": [
            "Eligible for Paramparagat Krishi Vikas Yojana (PKVY).",
            "Market-linked subsidy schemes.",
            "Support for certification & logistics."
        ]
    }
}

land_analysis = {
    "marginal": {
        "range": (0, 1),
        "label": "Marginal Farmer",
        "recommend": [
            "Eligible for micro-loans (₹10k–₹50k) under Kisan Credit Card (KCC).",
            "Low-interest input loans preferred.",
            "Some states offer special schemes for landless/marginal farmers."
        ]
    },
    "small": {
        "range": (1, 2),
        "label": "Small Farmer",
        "recommend": [
            "Loan range up to ₹1.5 lakh under standard crop loan.",
            "Can avail subsidies for small irrigation and machinery.",
            "KCC + PMFBY coverage highly recommended."
        ]
    },
    "semi-medium": {
        "range": (2, 4),
        "label": "Semi-Medium Farmer",
        "recommend": [
            "Eligible for ₹1.5–3 lakh depending on crop type.",
            "Capable of availing long-term and equipment loans.",
            "Eligible for storage infrastructure support."
        ]
    },
    "medium": {
        "range": (4, 10),
        "label": "Medium Farmer",
        "recommend": [
            "Eligible for larger loans (₹3L+), especially for mechanization.",
            "Schemes available for warehouse/storage, fencing, etc.",
            "Loan term could be mid to long (1–5 years)."
        ]
    },
    "large": {
        "range": (10, float("inf")),
        "label": "Large Farmer",
        "recommend": [
            "High-credit schemes for advanced farming methods.",
            "Possible eligibility for NABARD-backed infra projects.",
            "Can explore agribusiness schemes, FPO formation."
        ]
    }
}

region_analysis = {
    "Tamil Nadu": {
        "recommend": [
            "Eligible for Tamil Nadu State Government's Agricultural Loan Scheme.",
            "Subsidy on micro-irrigation systems (Drip/Sprinkler).",
            "PM-KISAN eligible for farmers below ₹2 lakh income.",
            "Special focus on Paddy and Sugarcane, check for local subsidies."
        ]
    },
    "Punjab": {
        "recommend": [
            "Eligible for Punjab State Government's crop loan scheme.",
            "PMFBY (PM Fasal Bima Yojana) coverage for wheat and paddy.",
            "Subsidy for mechanization under the PM-Kisan Tractor Scheme."
        ]
    },
    "Maharashtra": {
        "recommend": [
            "Eligible for Maharashtra State Crop Loan Scheme.",
            "Subsidy for rainwater harvesting and irrigation schemes.",
            "Check for state-backed loan for cotton farmers."
        ]
    },
    "Uttar Pradesh": {
        "recommend": [
            "Eligible for UP State Government’s Kisan Credit Card Scheme.",
            "Subsidies available for organic farming under state schemes.",
            "Eligibility for machinery loans, especially for wheat, maize, and sugarcane."
        ]
    },
    "Andhra Pradesh": {
        "recommend": [
            "Eligible for Andhra Pradesh State Government Agriculture Scheme.",
            "Subsidy available for micro-irrigation systems.",
            "Check for farmer producer organizations (FPOs) for group loans."
        ]
    },
    "Karnataka": {
        "recommend": [
            "Eligible for Karnataka State Crop Loan Scheme.",
            "Subsidies on organic farming inputs.",
            "Loan assistance for horticultural farmers (tomato, banana, etc.)."
        ]
    },
    "Himachal Pradesh": {
        "recommend": [
            "Eligible for Himachal Pradesh state-specific irrigation schemes.",
            "Loans for fruit and vegetable growers with low-interest rates.",
            "Subsidy for protected cultivation (poly-houses)."
        ]
    },
    "Kerala": {
        "recommend": [
            "Eligible for Kerala State Agricultural Loan Scheme.",
            "Subsidies for coconut and rubber cultivation.",
            "PMFBY coverage for all crops."
        ]
    }
}

purpose_analysis = {
    "Buy seeds and fertilizers": {
        "recommend": [
            "Eligible for crop input loans under KCC or PMFBY.",
            "Loan amount typically covers cost of seeds, fertilizers, and pesticides.",
            "Eligible for seed subsidy schemes in various states.",
            "If you are a first-time borrower, check for seed assistance schemes in your region."
        ]
    },
    "Purchase farming equipment": {
        "recommend": [
            "Eligible for agricultural equipment loans under PM-KISAN.",
            "Consider NABARD’s Rural Infrastructure Development Fund (RIDF) for large equipment purchases.",
            "Subsidy options available for small equipment under the state agricultural schemes.",
            "Also eligible for loans for storage or processing equipment."
        ]
    },
    "Set up irrigation": {
        "recommend": [
            "Eligible for irrigation equipment loan schemes under the Pradhan Mantri Krishi Sinchayee Yojana (PMKSY).",
            "Check for state-specific subsidies on drip/sprinkler irrigation systems.",
            "If applying for land expansion, consider including irrigation system funding in your loan."
        ]
    },
    "Expand land or livestock": {
        "recommend": [
            "Eligible for land expansion loans under PMFBY or state schemes.",
            "Consider land and livestock expansion schemes under NABARD-backed programs.",
            "Loan can cover purchase of additional land, livestock, and related infrastructure."
        ]
    },
    "Repay existing agricultural loans": {
        "recommend": [
            "Eligible for debt restructuring loans under various government schemes.",
            "State-specific loan waivers may apply depending on your region.",
            "If under financial stress, consider applying for emergency credit or emergency loan relief schemes."
        ]
    }
}

amount_analysis = {
    "10000": {
        "recommend": [
            "Eligible for micro-loans under Kisan Credit Card (KCC) Scheme.",
            "Short-term repayment plan (6 months to 1 year).",
            "Legal terms: Minimum documentation, lower interest rates (3%-5%)."
        ]
    },
    "50000": {
        "recommend": [
            "Eligible for small loan schemes under PM-KISAN.",
            "Repayment period of 1-3 years, suitable for purchasing equipment or seeds.",
            "Legal terms: Fixed interest rate, no prepayment penalty, collateral may not be required for amounts below ₹50,000."
        ]
    },
    "150000": {
        "recommend": [
            "Medium-term loan options under NABARD’s Rural Development Fund (RDF) and state government schemes.",
            "Repayment period of 3-5 years, suitable for land expansion, irrigation setup, or equipment purchases.",
            "Legal terms: Collateral may be required, fixed or floating interest rate, detailed documentation of business plan and repayment history."
        ]
    },
    "500000": {
        "recommend": [
            "Large loan options for farmers eligible for PMFBY, government schemes, or commercial banks.",
            "Repayment period of 5-7 years for expansion, large-scale equipment, or debt repayment.",
            "Legal terms: Collateral is usually required, detailed business plan required, interest rate varies from 6%-10%, and specific clauses on defaults."
        ]
    },
    "1000000": {
        "recommend": [
            "Eligible for large-scale project funding from NABARD or other government-backed loan schemes.",
            "Long-term loan repayment plan of 7-10 years for extensive land purchases, livestock farming, or irrigation projects.",
            "Legal terms: Higher collateral value, detailed financial disclosures required, interest rates in the range of 8%-12%, specific clauses on defaults, and penalties."
        ]
    }
}

experience_analysis = {
    "0-1": {
        "recommend": [
            "Eligibility for subsidized loans under PM-KISAN or KCC Scheme.",
            "Shorter loan repayment period (1-3 years), lower loan amounts.",
            "Legal terms: Minimum documentation, no collateral required for loans under ₹50,000."
        ]
    },
    "2-5": {
        "recommend": [
            "Eligible for small to medium-sized loans under NABARD or state schemes.",
            "Repayment period of 3-5 years, suitable for equipment, irrigation setup, or seeds.",
            "Legal terms: May require collateral for loans over ₹50,000, fixed interest rates."
        ]
    },
    "6-10": {
        "recommend": [
            "Eligible for larger loans under commercial banks, NABARD, and government programs.",
            "Repayment period of 5-7 years, suitable for land expansion or buying expensive farming equipment.",
            "Legal terms: Collateral required for loans over ₹1,50,000, flexible interest rates, detailed financial disclosures needed."
        ]
    },
    "10+": {
        "recommend": [
            "Eligible for high-value loans under government or commercial bank schemes with lower interest rates.",
            "Long-term repayment period of 7-10 years, suitable for large-scale farming projects, infrastructure, or livestock farming.",
            "Legal terms: Higher collateral value, specific repayment schedules, financial disclosures required, default clauses included."
        ]
    }
}

loan_status_analysis = {
    "yes": {
        "recommend": [
            "Eligibility for debt-repayment schemes (e.g., Restructured Loan Scheme, KCC Debt Relief Scheme).",
            "Possible consolidation of existing loans into a single loan with better terms and lower interest rates.",
            "Legal terms: Documentation of all existing loans, collateral may be required to secure new loans."
        ]
    },
    "no": {
        "recommend": [
            "Eligible for a wide range of loans including seed loans, equipment loans, irrigation loans, etc.",
            "Loan options with flexible repayment terms and interest rates based on credit history.",
            "Legal terms: Minimum documentation required for first-time loan applicants."
        ]
    }
}
def get_crop_analysis(crop):
    user_crop = crop
    info = crop_analysis.get(user_crop.lower())

    if info:
        data = (f"Crop Type:\n {info['type']}") + "\nRecommended Actions:\n"
        
        for rec in info['recommend']:
            data = data + (f"- {rec}")
        return data 
    else:
        return("Crop not recognized. Please enter a known crop type.")

def analyze_land_size(acres):
    for category, info in land_analysis.items():
        min_acre, max_acre = info["range"]
        if min_acre < acres <= max_acre:
            return {
                "category": info["label"],
                "recommend": info["recommend"]
            }
    return {"category": "Unknown", "recommend": ["Invalid land size entered."]}

def analyze_region(state):
    state = state.lower()
    recommendations = region_analysis.get(state.title(), None)
    
    if recommendations:
        return recommendations["recommend"]
    else:
        return ["No state-specific data found. Please check again."]

def analyze_loan_purpose(purpose):
    # Match with purpose options and provide analysis
    recommendations = purpose_analysis.get(purpose.lower(), None)
    
    if recommendations:
        return recommendations["recommend"]
    else:
        return ["No information found for the selected loan purpose. Please check the options."]

def analyze_loan_amount(amount):
    # Match loan amount with available legal terms and repayment options
    recommendations = amount_analysis.get(str(amount), None)
    
    if recommendations:
        return recommendations["recommend"]
    else:
        return ["No loan amount information found for the specified value. Please enter a valid amount."]

def analyze_experience(experience):
    # Match experience with available loan schemes and legal terms
    recommendations = experience_analysis.get(experience, None)
    
    if recommendations:
        return recommendations["recommend"]
    else:
        return ["No recommendation available for the specified years of experience."]

def analyze_loan_status(loan_status):
    # Match loan status with available loan schemes and legal terms
    recommendations = loan_status_analysis.get(loan_status, None)
    
    if recommendations:
        return recommendations["recommend"]
    else:
        return ["No recommendation available for the specified loan status."]
