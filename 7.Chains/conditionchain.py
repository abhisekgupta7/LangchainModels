from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda


load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo")

parser=StrOutputParser()

pydantic_parser=PydanticOutputParser(pydantic_object=Feedback)

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the feedback")


prompt1=PromptTemplate(
    template="Classify the following text into one of the following feedback text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions":pydantic_parser.get_format_instructions()}
)
classification_chain=prompt1|model|pydantic_parser

prompt2=PromptTemplate(
    template="Write an appropriate response to the positive feedback \n {feedback}",
    input_variables=["feedback"]
)
prompt3=PromptTemplate(
    template="Write an appropriate response to the negative feedback \n {feedback}",
    input_variables=["feedback"]
)

branch_chain=RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2|model|parser),
    (lambda x: x.sentiment == "negative", prompt3|model|parser),
   RunnableLambda(lambda x: "Could not find the sentiment of the feedback")
)

chain=classification_chain|branch_chain

result=chain.invoke({"feedback": "I love the product! It has exceeded my expectations."})
print(result)