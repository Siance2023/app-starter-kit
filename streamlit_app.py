import streamlit as st
from langchain.llms import OpenAI

st.title('🎈 SDSI Elaboration Assistant')
st.write('Hello world!')

# Retrieve the API key from the environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
openai.api_key = OPENAI_API_KEY

Entreprise_name = st.sidebar.text_input('Entreprise Name')

st.sidebar.file_uploader("Upload SDSI specification", type=["txt"])

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'Enter your use case here and ask for test cases.')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠️')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
