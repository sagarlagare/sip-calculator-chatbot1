import streamlit as st

# Function to calculate SIP corpus
def calculate_sip(principal, years, rate):
    n = years * 12  # total months
    r = rate / 100 / 12  # monthly interest rate
    future_value = principal * (((1 + r) ** n - 1) / r) * (1 + r)
    return round(future_value, 2)

# Streamlit UI
st.set_page_config(page_title="SIP Calculator Chatbot", page_icon="💰")

st.title("💬 SIP Calculator Chatbot")
st.write("Ask me about your SIP returns!")

# Simple chatbot-style input
user_input = st.text_input("You:", "e.g., If I invest 5000 for 20 years at 12% return")

if user_input:
    try:
        # Very simple parsing of numbers from user input
        import re
        numbers = re.findall(r"\d+", user_input)

        if len(numbers) >= 3:
            principal = int(numbers[0])
            years = int(numbers[1])
            rate = int(numbers[2])

            result = calculate_sip(principal, years, rate)
            st.success(f"If you invest ₹{principal} per month for {years} years at {rate}% return, you will have ₹{result}.")
        else:
            st.warning("Please enter in format: 5000 for 20 years at 12% return")

    except Exception as e:
        st.error(f"Error: {str(e)}")
