from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm=HuggingFaceEndpoint(
    repository_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

template1=PromptTemplate(
    template="Write detailed report on {topic}",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template="Write 5 line summary on the given text,/n {text}",
    input_variables=["text"]
)

prompt1=template1.invoke(topic="Climate Change")
result =model.invoke(prompt1)

prompt2=template2.invoke(text=result.content)
result2=model.invoke(prompt2)
print(result2.content)

