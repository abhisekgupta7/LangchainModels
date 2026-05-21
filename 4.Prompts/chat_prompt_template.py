from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system', 'You are a {domain} expert assistant.'),
    ('human', 'Explain {topic} to me in a simple style.')
])
 

prompt=chat_template.invoke({
    "domain": "machine learning",
    "topic": "transformer architecture"
})
print(prompt)

