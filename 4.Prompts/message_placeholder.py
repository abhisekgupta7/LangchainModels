from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder



#chat template

chat_template=ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent.'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human','{query}')
])
chat_history=[]

#load conversation history

with open("chat_history.txt","r") as f:
    chat_history.extend(f.readlines())

print(chat_history)

#create prompt 


query="How can I reset my password?"
prompt = chat_template.invoke({"query": query, "chat_history": chat_history})
print(prompt)
