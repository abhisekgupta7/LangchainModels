from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema



load_dotenv()

llm=HuggingFaceEndpoint(
    repository_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
 
model=ChatHuggingFace(llm=llm)
schema=[
    ResponseSchema(name="fact1", description="fact 1 about the topic"),
    ResponseSchema(name="fact2", description="fact 2 about the topic"),
    ResponseSchema(name="fact3", description="fact 3 about the topic"),
]
parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give me 3 facts about {topic} in the following format \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions":parser.get_format_instructions() } 
)

prompt=template.format(topic="Climate Change")  

# result=model.invoke(prompt)
# parsed_result=parser.parse(result.content)
# print(parsed_result)

chain=template|model|parser

result=chain.invoke(topic="Climate Change")
print(result)

