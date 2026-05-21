from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("example.pdf")
documents = loader.load()
print(documents)
print(documents[0].page_content)
print(len(documents))
