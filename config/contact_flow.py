"""
Contact details update conversation flows for the UniSuper AI Assistant demo.
"""

# Initial contact scenario
INITIAL_CONTACT = [
    {
        "role": "user",
        "content": "I need to update my address and phone number."
    },
    {
        "role": "assistant",
        "content": "Hi Natasha, I'd be happy to help you update your contact details. I can see that your current information is:\n\nAddress: 42 Research Drive, Carlton VIC 3053\nPhone: 0412 345 678\nEmail: natasha.campbell@unimelb.edu.au\n\nWhich details would you like to update today?"
    }
]

# Guided address update scenario
ADDRESS_UPDATE = [
    {
        "role": "user",
        "content": "I've moved to a new address. I want to update it to 15 University Avenue, Parkville VIC 3052."
    },
    {
        "role": "assistant",
        "content": "Got it! To confirm, I'll update your address from:\n\n42 Research Drive, Carlton VIC 3053\n\nTo:\n\n15 University Avenue, Parkville VIC 3052\n\nIs this correct? Also, would you like to keep your current mailing preferences for this new address?"
    }
]

# Contact verification scenario
CONTACT_VERIFICATION = [
    {
        "role": "user",
        "content": "Yes, that's correct. And yes, keep my mailing preferences the same."
    },
    {
        "role": "assistant",
        "content": "Great! For security purposes, I need to verify your identity before making this change. Could you please confirm your date of birth and member ID? Your member ID can be found on your UniSuper statements or by logging into your online account."
    },
    {
        "role": "user",
        "content": "My date of birth is 15/06/1980 and my member ID is US1234567."
    },
    {
        "role": "assistant",
        "content": "Thank you for verifying your identity. I've successfully updated your address to 15 University Avenue, Parkville VIC 3052.\n\nYour communication preferences remain unchanged - you'll continue to receive quarterly notifications via email.\n\nIs there anything else you'd like to update, such as your phone number or email address?"
    }
]

# Phone update scenario
PHONE_UPDATE = [
    {
        "role": "user",
        "content": "Yes, I also have a new phone number. It's 0487 654 321."
    },
    {
        "role": "assistant",
        "content": "Thank you. I'll update your phone number from 0412 345 678 to 0487 654 321. Is that correct?"
    },
    {
        "role": "user",
        "content": "Yes, that's right."
    },
    {
        "role": "assistant",
        "content": "Perfect! I've updated your phone number to 0487 654 321. Your contact details are now fully updated in our system.\n\nWhile I have you, would you like me to check if there are any other aspects of your UniSuper account that might need attention? For example, I can help review your investment options or insurance coverage."
    }
]

# Value-added services scenario
VALUE_ADDED_SERVICES = [
    {
        "role": "user",
        "content": "Actually, I've been thinking about my investment options. Can you tell me about them?"
    },
    {
        "role": "assistant",
        "content": "I'd be happy to help with that, Natasha! I can see you're currently invested in the Balanced option, which has delivered an average return of 7.5% p.a. over the last 5 years.\n\nInterestingly, your super grew by 5.2% last year, compared to an average of 6.8% for members in your age group and profession. \n\nBased on your age and projected retirement at 67, you might want to consider options with potentially higher returns over the long term. Our analysis suggests that someone in your situation might benefit from exploring:\n\n1. The High Growth option - higher potential returns with more volatility\n2. The Sustainable High Growth option - similar growth focus but with ESG considerations\n\nWould you like to see a comparison of how these different options might affect your projected retirement balance?"
    }
]

# Investment comparison scenario
INVESTMENT_COMPARISON = [
    {
        "role": "user",
        "content": "Yes, I'd like to see that comparison."
    },
    {
        "role": "assistant",
        "content": "Great! Here's a comparison of your projected retirement balance at age 67 based on different investment options:\n\n- Current Balanced option: ~$1.25 million\n- High Growth option: ~$1.48 million\n- Sustainable High Growth: ~$1.41 million\n\nThese projections assume your current contribution rate of 12.5% and salary of $142,000 with standard growth assumptions.\n\nI'll send this comparison to your email so you can review it in detail later. Would you like to book a consultation with a UniSuper financial advisor to discuss these options in more detail? They can provide personalized advice tailored to your complete financial situation."
    }
]

# Guided next steps scenario
GUIDED_NEXT_STEPS = [
    {
        "role": "user",
        "content": "That would be good. Can you help me book an appointment?"
    },
    {
        "role": "assistant",
        "content": "I'd be happy to help you book an appointment with a UniSuper financial advisor. They can provide personalized advice about your investment options and retirement strategy.\n\nBased on your location in Parkville, there are appointments available at the UniSuper Parkville office on:\n\n- Tuesday, March 12 at 10:00 AM\n- Wednesday, March 13 at 2:30 PM\n- Friday, March 15 at 9:15 AM\n\nAlternatively, you can schedule a video consultation if that's more convenient. Would any of these options work for you, or would you prefer a video appointment?"
    },
    {
        "role": "user",
        "content": "Tuesday would work for me."
    },
    {
        "role": "assistant",
        "content": "Perfect! I've booked you in for Tuesday, March 12 at 10:00 AM with Sarah Johnson, one of our senior financial advisors at the Parkville office. You'll receive a confirmation email shortly with all the details and what to bring.\n\nIs there anything specific you'd like me to note that you want to discuss during your appointment?"
    }

]