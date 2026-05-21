from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


from langchain_core.output_parsers import JsonOutputParser




load_dotenv()

llm=HuggingFaceEndpoint(
    repository_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
model=ChatHuggingFace(llm=llm)
parser=JsonOutputParser()
template=PromptTemplate(
    template="Give me name,age and city of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions":parser.get_format_instructions() }
)

# result=model.invoke(prompt)
# parsed_result=parser.parse(result.content)
# print(parsed_result)

chain=template|model|parser
prompt=template.format()
result=chain.invoke({})
print(result)

