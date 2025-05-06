import streamlit as st
import random
import nltk

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Define greeting inputs and responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

# Function to check for greetings
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Function to generate a response
def response(user_response):
    # Here you can add more sophisticated response logic
    return "I am sorry! I don't understand you."

# Streamlit UI
st.title("Chatbot")
st.write("### Talk to the Chatbot!")

# User input
user_input = st.text_input("You: ")

if user_input:
    # Check for greeting
    if greeting(user_input) is not None:
        st.write("Chatbot: " + greeting(user_input))
    else:
        st.write("Chatbot: " + response(user_input))