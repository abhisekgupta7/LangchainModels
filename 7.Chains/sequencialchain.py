from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=PromptTemplate(
    template="Generate detailed report on {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Summarize the following report in 5 bullet points \n {report}",
    input_variables=["report"]
)
model=ChatOpenAI(model="gpt-3.5-turbo")
parser=StrOutputParser()
chain=prompt1|model|parser|prompt2|model|parser
result=chain.invoke({"topic":"climate change"})
print(result)

