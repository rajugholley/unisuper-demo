import streamlit as st
from anthropic import Anthropic
import os
from dotenv import load_dotenv
import pandas as pd
import re
from datetime import datetime

# Load API key from .env file
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# Configure page
st.set_page_config(page_title="UniSuper", layout="wide")

# Hide Streamlit branding
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Add system action function
def add_system_action(action, details=None):
    """Add a system action for the demonstration view"""
    if "system_actions" not in st.session_state:
        st.session_state.system_actions = []
        
    st.session_state.system_actions.append({
        "action": action,
        "details": details,
        "time": datetime.now().strftime("%H:%M:%S")
    })

# Function to update customer database
def update_customer_db(field, new_value):
    """Update the customer database with a new value for a field"""
    # Get the current database
    df = st.session_state.customer_db.copy()
    
    # Get the index of the field to update
    field_idx = df[df['Field'] == field].index[0]
    
    # Get old value for display
    old_value = df.at[field_idx, 'Value']
    
    # Update the value
    df.at[field_idx, 'Value'] = new_value
    
    # Update the Last Updated field
    last_updated_idx = df[df['Field'] == 'Last Updated'].index[0]
    df.at[last_updated_idx, 'Value'] = datetime.now().strftime("%d/%m/%Y")
    
    # Save the updated database
    st.session_state.customer_db = df
    
    # Set update pending to False
    st.session_state.db_update_pending = False
    
    # Add a system action
    add_system_action(f"Updated {field}", f"Old: {old_value} → New: {new_value}")
    
    # Add a system notification to chat
    system_message = f"✅ Your {field.lower()} has been updated to {new_value}"
    st.session_state.messages.append({"role": "system", "content": system_message})
    print(f"SYSTEM MESSAGE ADDED: {system_message}")

# Check for database updates in conversation
def check_for_db_updates(prompt, response):
    """Check for patterns in the conversation where we need to update the database"""
    # Check if there's a new phone number in the prompt
    phone_pattern = r'(\d{4}\s\d{3}\s\d{3}|\d{10}|\d{4}\s\d{6})'
    phone_matches = re.findall(phone_pattern, prompt)
    
    if phone_matches and "phone" in prompt.lower():
        # Store the new phone number
        st.session_state.new_phone = phone_matches[0]
        # Set update pending to True
        st.session_state.db_update_pending = True
        
    # Check if there's confirmation in the prompt after a pending update
    if st.session_state.db_update_pending and any(word in prompt.lower() for word in ['yes', 'correct', 'right', 'yep', 'yeah']):
        # Update the database
        update_customer_db('Phone', st.session_state.new_phone)
        st.session_state.db_update_pending = False

# Simple UniSuper header with HTML/CSS
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; border-bottom: 1px solid #e5e5e5; background-color: white;">
    <span style="color: #004B87; font-size: 50px; font-weight: bold;">UniSuper</span>
    <div style="display: flex; gap: 2rem; align-items: center;">
        <a href="#" style="color: #0062cc; text-decoration: none;">Contact us</a>
        <a href="#" style="color: #0062cc; text-decoration: none;">About us</a>
        <a href="#" style="color: #0062cc; text-decoration: none;">Employers</a>
        <a href="#" style="padding: 0.5rem 2rem; border: 1px solid #0062cc; border-radius: 4px; color: #0062cc; text-decoration: none;">Login</a>
        <a href="#" style="padding: 0.5rem 2rem; background-color: #0062cc; border-radius: 4px; color: white; text-decoration: none;">Sign-up</a>
    </div>
</div>
<div style="border-bottom: 1px solid #e5e5e5; padding: 0.5rem 2rem; background-color: white;">
    <div style="display: flex; gap: 2rem; max-width: 1200px; margin: 0 auto;">
        <a href="#" style="color: #0062cc; text-decoration: none;">Compare</a>
        <a href="#" style="color: #0062cc; text-decoration: none;">Super</a>
        <a href="#" style="color: #0062cc; text-decoration: none;">Retirement</a>
        <a href="#" style="color: #0062cc; text-decoration: none;">Investments</a>
        <a href="#" style="color: #0062cc; text-decoration: none;">Financial advice</a>
        <a href="#" style="color: #0062cc; text-decoration: none;">Insurance</a>
        <a href="#" style="color: #0062cc; text-decoration: none;">Tools and learning</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    <h1>Welcome to UniSuper</h1>
    <p>Australia's leading superannuation fund for the higher education and research sector.</p>
    <p>We're dedicated to helping our members build a secure financial future.</p>
    """, unsafe_allow_html=True)
    
    st.write("")  # Spacing
    
    st.markdown("""
    <h2>Need help?</h2>
    <p>Our virtual assistant is here to help you with account updates, investment information, and more.</p>
    <p>Start chatting with our assistant in the panel to the right.</p>
    """, unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi Michelle! I'm your UniSuper assistant. How can I help you today?"}
    ]

# Initialize customer database
if "customer_db" not in st.session_state:
    st.session_state.customer_db = pd.DataFrame({
        'Field': ['Name', 'Member ID', 'Email', 'Phone', 'Address', 'Last Updated'],
        'Value': [
            'Natasha Campbell', 
            'US1234567', 
            'natasha.campbell@unimelb.edu.au', 
            '0412 345 678', 
            '42 Research Drive, Carlton VIC 3053',
            '15/05/2021'
        ]
    })
    
if "db_update_pending" not in st.session_state:
    st.session_state.db_update_pending = False
    
if "new_phone" not in st.session_state:
    st.session_state.new_phone = ""

# Chat interface using simple HTML/CSS
with col2:
    # Simple chat header
    st.markdown('<div style="background-color: #004B87; color: white; padding: 15px; border-radius: 10px 10px 0 0; display: flex; align-items: center;"><span style="margin-right: 8px; font-size: 20px;">💬</span><b>UniSuper Assistant</b></div>', unsafe_allow_html=True)
    
    # Chat messages container with fixed height
    st.markdown('<div style="height: 200px; overflow-y: auto; padding: 10px; border-left: 1px solid #e0e0e0; border-right: 1px solid #e0e0e0; background-color: #f0f5fa; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">', unsafe_allow_html=True)

    
    # Display messages with custom styling
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div style="background-color: #E3F2FD; color: #01579B; padding: 10px; border-radius: 10px; margin: 5px 0 5px auto; max-width: 80%; text-align: right;">{message["content"]}</div>', unsafe_allow_html=True)
        elif message["role"] == "assistant":
            st.markdown(f'<div style="background-color: #004B87; color: white; padding: 10px; border-radius: 10px; margin: 5px auto 5px 0; max-width: 80%;">{message["content"]}</div>', unsafe_allow_html=True)
        elif message["role"] == "system":
             st.markdown(f'<div style="background-color: #e6ffe6; border: 2px solid #00cc00; padding: 10px; margin: 10px 0; border-radius: 4px; font-size: 1em; font-weight: bold; color: #006600;">{message["content"]}</div>', unsafe_allow_html=True)
    # Close the chat messages container
    st.markdown('</div>', unsafe_allow_html=True)
    with st.spinner(''):  # This creates an invisible spinner that prevents multiple submits
        prompt = st.chat_input("Type your message here...", key="chat_input")
    # Chat input styling
    st.markdown('<div style="border-left: 1px solid #e0e0e0; border-right: 1px solid #e0e0e0; border-bottom: 1px solid #e0e0e0; padding: 10px; border-radius: 0 0 10px 10px; background-color: #f0f5fa; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">', unsafe_allow_html=True)
    
    # System changes in a collapsed section
    
    # Close styling container
    st.markdown('</div>', unsafe_allow_html=True)

# Chat input
if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get Claude response
    try:
        client = Anthropic(api_key=api_key)
        messages = []
        
        # Format message history for Claude
        for msg in st.session_state.messages:
            if msg["role"] != "system":  # Skip system messages for Claude
                role = "assistant" if msg["role"] == "assistant" else "user"
                messages.append({"role": role, "content": msg["content"]})
        
        # Call Claude API
        response = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=500,
            messages=messages[-5:],  # Limit context window
            system="""You are UniSuper's AI Assistant helping members manage their superannuation.

IMPORTANT: Follow this EXACT conversation flow without any deviation:

INITIAL GREETING:
- Start with: "Hi Michelle! I'm your UniSuper assistant. How can I help you today?"?"

FOR CONTACT UPDATES:
- When she mentions changing email: Say "Sure! Your current email on file is michelle.campbell@unimelb.edu.au. What's your new email address?"
- When she mentions changing phone: Say "Sure! Your current phone on file is 0412 345 678. What's your new phone number?"
- After she provides new details: Ask "Got it! Just to confirm, your new [email/phone] will be [new info]. Is that correct?"
- After confirmation: Say "Great! Your [email/phone] has been updated successfully. Would you also like to update your communication preferences?"
- If she wants to change preferences: Say "Currently, you're set to receive updates via email only. I can switch you to SMS only or SMS + Email. Which do you prefer?"
- After setting preferences: Say "Done! You'll now receive updates via [preference]. If you ever want to change this, just ask!"
- After completing : Wait for Michelle to respond, ok or Thanks or anything that shows closure. Once she says that, jump to INVESTMENT NUDGE, but make it very smooth. Don't look desperate. Keep it as warm and natural as possible without trying too hard to sell

INVESTMENT NUDGE:
- For the investment nudge say: Say "By the way, I am looking through your account and I noticed you haven't made any changes to your super investment options in the past 3 years. In next paragraph say, Many members review their investment mix every few years to ensure it still aligns with their financial goals."
- If she asks about performance: Say "I can show you how your current investment mix compares to others in your age group. Would you like to take a quick look?"
- Then provide: "Alright! Here's a quick breakdown:
  Your current allocation: 80% in a balanced fund, 20% in cash.
  Typical allocation for members your age: 60% growth assets, 30% balanced, 10% cash. Highlight these numbers in green bold format. 
  Performance comparison: Your super grew by 5.2% last year, compared to an average of 6.8% for similar members and higher returns means you'll have more funds saved up for a comfortable retirement. Highlight these numbers in maroon bold and this sentence as a separate paragraph.
  Would you like to explore different investment options or speak with an adviser?"
- If she's interested: Say "I can show you a comparison of available investment strategies, including their historical returns and risk levels. Then next paragraph , say,  I'll send this to your email so you can review it at your convenience. In next paragraph If you'd like to discuss your options further, I can also book a free session with an adviser. Let me know if you'd like me to schedule it!"
- For booking, give her options in bullets and separate lines - 10 - 11 AM, Monday 12 May 2025, 3-4 PM, Wednesday 14 May 2025. 
- When she selects one of these then move to next step 'For booking'. 
- For booking: Say "Done! I've emailed you the investment comparison, and you're booked in for a session with an adviser on Thursday at 10 AM. Let me know if you need to reschedule. Have a great day, Michelle!. Stop right after this. If customer says thanks, just acknowledge warmly and say if you want to reschdeule appointment or want to discuss anything about your superannuation account , please don't hestiate to contact me"

BEHIND THE SCENES (but don't mention this directly):
- Contact Management Agent: Handles verification and updating of contact details in the system
- Investment Analysis Agent: Analyzes current portfolio and generates personalized comparisons
- Scheduling Agent: Checks advisor availability and books appointments

Keep responses conversational, warm and brief. Always use the name 'Natasha' instead of 'Emma'.
"""
        )
        
        assistant_response = response.content[0].text
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        # Check for database updates
        check_for_db_updates(prompt, assistant_response)
        
    except Exception as e:
        error_message = "I'm sorry, I'm having trouble connecting right now. Please try again later."
        st.session_state.messages.append({"role": "assistant", "content": error_message})
    
    # Force a rerun to display the new messages
    st.experimental_rerun()

# UniSuper footer
st.markdown("""
<div style="background-color: #004B87; color: white; padding: 2rem; margin-top: 3rem;">
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
        <div>
            <h3>Contact UniSuper</h3>
            <p>1800 331 685</p>
            <p>info@unisuper.com.au</p>
        </div>
        <div>
            <h3>Quick links</h3>
            <p>Forms & downloads</p>
            <p>Find my super</p>
        </div>
        <div>
            <h3>Legal</h3>
            <p>Privacy policy</p>
            <p>Terms of use</p>
        </div>
    </div>
    <div style="max-width: 1200px; margin: 1rem auto 0; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.2);">
        <p>© 2025 UniSuper Management Pty Ltd. All rights reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)