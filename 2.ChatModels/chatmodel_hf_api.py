import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro", 
    task="text-generation",
    huggingfacehub_api_token=hf_token,)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of France?")

print(result.content)