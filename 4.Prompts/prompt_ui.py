from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core import PromptTemplate

load_dotenv()
model=ChatOpenAI()

st.header("Research Assistant")
paper_input=st.selectbox("Select a research paper",["Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding","GPT-3: Language Models are Few-Shot Learners"])
style_input=st.selectbox("Select a writing style",["Beginner-Friendly","Mathematical","Technical","Code-Oriented"])
length_input=st.selectbox("Select a response length",["Short","Medium","Long"])

template = PromptTemplate(
template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],

)
prompt=template.invoke({
    "paper_input": paper_input,
     "style_input": style_input, 
     "length_input": length_input
     })

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write("Response:", result.content)

