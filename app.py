 # Importing required packages
import streamlit as st
import openai
from openai import OpenAI



# Set up the page
st.set_page_config(page_title="Streamlit GPT APP")
st.title('🦜🔗 Quickstart App')
st.sidebar.title("Math Tutor using Open AI GPT")
st.sidebar.divider()
st.sidebar.markdown("Smita", unsafe_allow_html=True)
st.sidebar.markdown("🎓 🎓 🎓")
st.sidebar.divider()

# Initialize OpenAI client

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
client = OpenAI(api_key=openai_api_key)

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

thread = client.beta.threads.create()

with st.form('my_form'):
    text = st.text_input("what Math problem can I help you with?")
 
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=text
)
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Student. The user has a premium account."
)
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)
messages = client.beta.threads.messages.list(
  thread_id=thread.id
)
for message in reversed(messages.data):
    st.info(message.role + ": " + message.content[0].text.value)

 
     
