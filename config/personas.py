"""
Customer personas for the UniSuper AI Assistant demo.
Includes detailed profiles for demonstration scenarios.
"""

# Primary persona used in the demo
NATASHA = {
    "personal_info": {
        "name": "Natasha Campbell",
        "member_id": "US1234567",
        "dob": "15/06/1980",
        "email": "natasha.campbell@unimelb.edu.au",
        "phone": "0412 345 678",
        "occupation": "Associate Professor, Department of Economics",
        "employer": "University of Melbourne",
        "joined_date": "23/03/2010",
        "address": "42 Research Drive, Carlton VIC 3053",
        "life_stage": "mid-career"
    },
    "account_details": {
        "balance": 487652.43,
        "contribution_rate": 12.5,
        "fund_type": "Accumulation 2",
        "investment_option": "Balanced",
        "insurance_coverage": {
            "death_cover": 750000,
            "tpd_cover": 750000, 
            "income_protection": "Yes, 75% of salary for up to 2 years"
        },
        "last_statement_date": "30/06/2023",
        "member_since": "2010",
        "salary": 142000
    },
    "beneficiaries": {
        "type": "Non-Binding",
        "last_updated": "15/07/2019",
        "nominations": [
            {"name": "Michael Campbell", "relationship": "Spouse", "allocation": 70},
            {"name": "Emma Campbell", "relationship": "Child", "allocation": 15},
            {"name": "James Campbell", "relationship": "Child", "allocation": 15}
        ],
        "status": "Expiring soon"
    },
    "preferences": {
        "communication_channel": "Email",
        "notification_frequency": "Quarterly",
        "interests": ["Retirement planning", "Investment performance", "Ethical investing"],
        "risk_profile": "Moderate",
        "engagement_level": "Medium",
        "digital_proficiency": "High"
    },
    "insights": {
        "potential_retirement_age": 67,
        "projected_retirement_balance": 1250000,
        "projected_annual_income": 62500,
        "retirement_adequacy": "On track",
        "suggested_contribution_increase": 2.5,
        "suggested_investment_options": ["Sustainable High Growth", "Australian Equity"],
        "insurance_adequacy": "Adequate"
    },
    "recent_activities": [
        {"date": "10/01/2023", "activity": "Downloaded annual statement"},
        {"date": "22/05/2023", "activity": "Viewed retirement calculator"},
        {"date": "05/06/2023", "activity": "Attended webinar on sustainable investing"}
    ],
    "contact_details": {
        "phone": "0412 345 678",
        "email": "natasha.campbell@unimelb.edu.au",
        "address": {
            "street": "42 Research Drive",
            "suburb": "Carlton",
            "state": "VIC",
            "postcode": "3053",
            "country": "Australia"
        },
        "last_updated": "15/05/2021"
    }
}

# Secondary persona for alternative scenarios (not used in primary demo)
MICHELLE = {
    "personal_info": {
        "name": "David Zhang",
        "member_id": "US7891234",
        "dob": "03/11/1975",
        "email": "d.zhang@unsw.edu.au",
        "phone": "0435 678 901",
        "occupation": "Professor, Faculty of Engineering",
        "employer": "University of New South Wales",
        "joined_date": "17/02/2008",
        "address": "15 Academic Way, Kensington NSW 2033",
        "life_stage": "pre-retirement"
    },
    "account_details": {
        "balance": 892341.75,
        "contribution_rate": 15.0,
        "fund_type": "Defined Benefit",
        "investment_option": "Conservative",
        "insurance_coverage": {
            "death_cover": 1000000,
            "tpd_cover": 1000000,
            "income_protection": "Yes, 85% of salary for up to 5 years"
        },
        "last_statement_date": "30/06/2023"
    },
    "beneficiaries": {
        "type": "Binding",
        "last_updated": "22/09/2022",
        "expiry_date": "22/09/2025",
        "nominations": [
            {"name": "Linda Zhang", "relationship": "Spouse", "allocation": 100}
        ],
        "status": "Current"
    }
}

# Function to get persona data
def get_persona(name="Natasha"):
    """Return the specified persona data"""
    if name.lower() == "natasha":
        return NATASHA
    elif name.lower() == "michelle":
        return MICHELLE
    else:
        return NATASHA  # Default to Natasha