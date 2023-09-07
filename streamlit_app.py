from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def main():
    st.title("Gorilla LLM")
    input_prompt = st.text_area("Enter your prompt:")
    
    model_options = ('gorilla-7b-hf-v1', 'gorilla-mpt-7b-hf-v0')
    option = st.selectbox('Select a model:', model_options)
    
    if st.button("Create"):
        if len(input_prompt) > 0:
            result = get_gorilla_response(prompt=input_prompt, model=option)
            st.write(result)
            # ...
if st.button("Gorilla Magic"):
    if len(input_prompt) > 0:
        # ...
        with col2:
            code_result = extract_code_from_output(result)
            if option == "gorilla-7b-hf-v1":
                st.subheader("Generated Output")
                st.code(code_result, language='python')
            elif option == "gorilla-mpt-7b-hf-v0":
                lines = code_result.split('\\n')
                for line in lines[:-1]:
                    st.code(line, language='python')
            # ...
            run_generated_code(file_path)
