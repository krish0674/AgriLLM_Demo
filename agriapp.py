import streamlit as st
import requests
import time

# Set Streamlit page configuration
st.set_page_config(page_title="Agricultural Query Assistance")
st.title("Agricultural Query Assistance")

# Sidebar for user login or instructions
with st.sidebar:
    st.title("Instructions for Use")
    st.write("""
        - Please enter your query using short, keyword-focused sentences as shown in the examples.
        - This tool is specifically designed for farmers in Tamil Nadu.
        - The model provides the best results with concise queries.
        - Each query should be independent of previous ones; the model does not support back-and-forth conversations.
    """)

# Function to call the model API
def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/krish0674/agrillm_bart"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Display buttons for each query option and handle user input
query_options = ["local agriculture department number", "banana nutrient management", "top dressing for paddy", "watermelon sowing season"]
user_input = None
for option in query_options:
    if "selected_option" not in st.session_state or option != st.session_state.selected_option:
        if st.button(option):
            user_input = option
            st.session_state.selected_option = option
            
            break

user_query = st.text_input("Enter your query here")

# Process the selected option or user input
if user_input or user_query:
    query_text = user_input if user_input else user_query
    flag = True
    while flag:
        output = query({"inputs": query_text})
        if ( isinstance(output, dict) and "error" in output[0].keys()):
            st.write(output)
            time.sleep(10)
        else:
            flag = False
            # with st.container():
            #     st.write(f"👨‍🌾 Query: {query_text}")
            with st.container():
                st.write(f"👨‍🌾💡 Response: {output[0]['generated_text']}")
            break

if 'selected_option' in st.session_state:
    del st.session_state.selected_option





