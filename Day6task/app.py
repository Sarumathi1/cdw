import random
from dotenv import load_dotenv
import streamlit as st
import chain

load_dotenv()

def Code_Generator():
    """
    Code Generator Bot
    """
    with st.form("Code_Generator"):
        st.write("## 🤖Code Generator")
    
        language= st.text_input("language 🗣️")
        problem_statement = st.text_input(" Tell me your problem! 🧐")
        submitted = st.form_submit_button("Here u go!!",type="primary")
        if(submitted):
            response =chain.Generate_code(language,problem_statement)
            st.info(response)
            st.write(random.choice([
                "🤓 Boom! Now go and pretend you wrote this yourself.",
                
            ]))

        

Code_Generator()