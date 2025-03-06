"""
Australian superannuation regulations and compliance guardrails.
Used to ensure the AI assistant provides accurate regulatory information
and follows appropriate compliance processes.
"""

# Beneficiary nomination regulations
BENEFICIARY_REGULATIONS = {
    "binding_nomination": {
        "requirements": [
            "Must be in writing on an approved form",
            "Must be signed and dated by the member in the presence of two witnesses",
            "Witnesses must be 18+ years old and not nominated as beneficiaries",
            "Must clearly state the proportion of benefit allocated to each beneficiary",
            "Beneficiaries must be dependents (spouse, child, financial dependent) or legal representative"
        ],
        "duration": "Valid for 3 years from the date of signing",
        "renewal": "Must be renewed every 3 years",
        "lapsing": "If not renewed, reverts to non-binding nomination",
        "advantages": [
            "Legally binding if valid",
            "Trustee must follow your instructions",
            "Can provide certainty about distribution of benefits"
        ],
        "disadvantages": [
            "Requires witness signatures and formal documentation",
            "Must be renewed regularly",
            "Less flexibility if circumstances change"
        ],
        "update_process": "Cannot be updated online, requires physical form with witnesses"
    },
    "non_binding_nomination": {
        "requirements": [
            "Can be made online or in writing",
            "No witness requirements",
            "Must clearly state preferred beneficiaries"
        ],
        "duration": "Does not expire, but regular review recommended",
        "advantages": [
            "Easy to update",
            "No renewal requirements",
            "Can be updated online"
        ],
        "disadvantages": [
            "Not legally binding on the trustee",
            "Trustee has discretion to distribute benefits",
            "May not guarantee your wishes are followed"
        ],
        "update_process": "Can be updated online through member portal"
    },
    "eligible_beneficiaries": [
        "Spouse (including de facto and same-sex partners)",
        "Children of any age (including adopted and step-children)",
        "Financial dependents",
        "Interdependency relationships",
        "Legal personal representative (executor of will/estate)"
    ],
    "ineligible_beneficiaries": [
        "Friends",
        "Parents (unless financially dependent)",
        "Siblings (unless financially dependent)",
        "Ex-spouses",
        "Other relatives (unless financially dependent)"
    ]
}

# Privacy and data protection requirements
PRIVACY_REQUIREMENTS = {
    "identity_verification": [
        "Member must verify identity before making any account changes",
        "Two-factor authentication required for online updates",
        "Additional verification required for high-risk transactions"
    ],
    "data_protection": [
        "Member data must be encrypted in transit and at rest",
        "Access to member data must be logged and auditable",
        "Personal information must be handled in accordance with Privacy Act 1988"
    ],
    "consent_requirements": [
        "Explicit consent required before sharing information with third parties",
        "Purpose of data collection must be clearly communicated",
        "Members can withdraw consent at any time"
    ]
}

# Responsible AI principles for financial services
RESPONSIBLE_AI_PRINCIPLES = {
    "transparency": [
        "Members must be informed when interacting with AI systems",
        "AI decision-making process should be explainable",
        "Clear disclosure of limitations of AI advice"
    ],
    "accountability": [
        "Human oversight required for critical decisions",
        "Clear escalation paths to human representatives",
        "Regular auditing of AI recommendations"
    ],
    "fairness": [
        "AI must not discriminate based on protected attributes",
        "Regular testing for bias in recommendations",
        "Equal quality of service for all members"
    ],
    "member_best_interest": [
        "AI recommendations must prioritize member's financial interests",
        "Recommendations should be personalized to member circumstances",
        "Clear disclosure of any limitations or conflicts"
    ]
}

# Financial advice boundaries
FINANCIAL_ADVICE_BOUNDARIES = {
    "general_information": [
        "Fund features and benefits",
        "Explanation of investment options without specific recommendations",
        "Factual information about superannuation rules",
        "Educational material about retirement planning"
    ],
    "intrafund_advice": [
        "Investment choice within the fund",
        "Insurance needs within the fund",
        "Contribution strategies",
        "Basic retirement adequacy projections"
    ],
    "personal_advice_requiring_escalation": [
        "Specific investment recommendations outside the fund",
        "Comprehensive retirement planning",
        "Estate planning strategies",
        "Tax optimization strategies",
        "Recommendations considering external financial situations"
    ],
    "disclaimers": [
        "Information provided is general in nature",
        "Does not take into account personal financial situation",
        "Not a substitute for personal financial advice",
        "Consider seeking advice from a licensed financial advisor"
    ]
}

# Regulatory validation functions
def validate_binding_nomination(nominations):
    """
    Validate if a binding nomination meets regulatory requirements
    
    Args:
        nominations (list): List of nomination objects with beneficiary details
        
    Returns:
        tuple: (is_valid, issues)
    """
    is_valid = True
    issues = []
    
    # Check total allocation equals 100%
    total_allocation = sum(nom["allocation"] for nom in nominations)
    if total_allocation != 100:
        is_valid = False
        issues.append(f"Total allocation must equal 100%. Current total: {total_allocation}%")
    
    # Check for zero allocations
    zero_allocations = [nom for nom in nominations if nom["allocation"] == 0]
    if zero_allocations:
        is_valid = False
        issues.append("All listed beneficiaries must have an allocation greater than 0%")
    
    return is_valid, issues

def get_advice_boundary(topic):
    """
    Determine if a topic is within general advice boundaries or requires escalation
    
    Args:
        topic (str): The advice topic
        
    Returns:
        str: "general", "intrafund", or "personal"
    """
    topic_lower = topic.lower()
    
    # Topics that require personal advice
    personal_advice_keywords = [
        "tax strategy", "estate plan", "external investment", 
        "specific recommendation", "smsf", "property investment"
    ]
    
    # Topics within intrafund advice
    intrafund_advice_keywords = [
        "investment choice", "insurance need", "contribution strategy",
        "retirement projection", "adequacy", "investment switch"
    ]
    
    for keyword in personal_advice_keywords:
        if keyword in topic_lower:
            return "personal"
    
    for keyword in intrafund_advice_keywords:
        if keyword in topic_lower:
            return "intrafund"
    
    return "general"

def get_required_disclaimer(advice_type):
    """
    Returns appropriate disclaimer based on advice type
    
    Args:
        advice_type (str): "general", "intrafund", or "personal"
        
    Returns:
        str: Appropriate disclaimer text
    """
    if advice_type == "personal":
        return "This topic requires personal financial advice. I recommend speaking with a UniSuper financial advisor who can provide personalized recommendations based on your complete financial situation."
    
    elif advice_type == "intrafund":
        return "This information is provided as general and intrafund advice about UniSuper products. It does not take into account your complete financial situation or needs. Consider seeking advice from a qualified financial advisor before making financial decisions."
    
    else:  # general
        return "This information is general in nature and does not consider your personal circumstances. Consider your own objectives and financial situation before making any decisions based on this information."