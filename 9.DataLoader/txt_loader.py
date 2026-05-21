from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo")

parser=StrOutputParser()

prompt=PromptTemplate(
    template="Write a summary of the following poem-\n {poem}",
    input_variables=["poem"]
)

loader=TextLoader("example.txt",encoding="utf-8")

documents=loader.load()
print(documents)
print(len(documents))
print(documents[0])
print(documents[0].page_content)
print(documents[0].metadata)

chain=prompt|model|parser
result=chain.invoke({"poem": documents[0].page_content})    
print(result)