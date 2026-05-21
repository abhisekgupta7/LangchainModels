from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline



llm=HuggingFacePipeline.from_model_id(
    model_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100, "temperature": 0.3},

)


model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of France?")  

print(result.content)