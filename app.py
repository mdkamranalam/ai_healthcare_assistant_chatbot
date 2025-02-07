import os
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain import PromptTemplate, LLMChain
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from dotenv import load_dotenv

# Download necessary NLTK data
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load environment variables
# load_dotenv()
# sec_key = os.getenv("HUGGINGFACE_TOKEN")

# Load secret key in streamlit
sec_key = st.secrets['HUGGINGFACE_TOKEN']

# Validate API Key
if not sec_key:
    st.error("Error: Hugging Face API token is missing. Please check your .env file.")
    st.stop()

# Define the LLM model with the correct parameters
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceEndpoint(
    repo_id=repo_id, 
    task="text-generation", 
    truncation=True, 
    temperature=0.7, 
    token=sec_key
)

# Process user input
def preprocess_input(user_input):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(user_input)
    filtered_word = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_word)

# Define healthcare-specific response logic
def healthcare_chatbot(user_input):
    user_input = preprocess_input(user_input).lower()
    
    # Define the prompt template
    template = """
    Use the pieces of information provided in the context to answer user's question.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Don't provide anything out of the context.
    Only generate answer related to healthcare, medication, lifestyle recommendation.
    Question: {question}
    Start the answer directly. No small talk please.
    """
    prompt = PromptTemplate(template=template, input_variables=['question'])
    
    # Create the LLM chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    response = llm_chain.invoke({"question": user_input})
    return response['text']

# Streamlit Web Application Interface
def main():
    st.title("AI Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you?")
    
    if st.button("Submit"):
        if user_input.strip():
            st.write("User: ", user_input)
            with st.spinner("Processing, please wait..."):
                try:
                    response = healthcare_chatbot(user_input)
                    st.write("Chatbot: ", response.strip())
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid question.")

if __name__ == "__main__":
    main()
