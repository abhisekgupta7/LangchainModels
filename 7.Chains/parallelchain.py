from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1=ChatOpenAI(model="gpt-3.5-turbo")
model2=ChatAnthropic(model="claude-3-opus-20241209")
prompt1=PromptTemplate(
    template="Generate short and simple notes from the following text\n {text}",
    input_variables=["text"]
)
prompt2=PromptTemplate(
    template="Generate 5 short questions answers from the followong text \n {text}",
    input_variables=["text"]
)

prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        "notes": prompt1|model1|parser,
        "quiz": prompt2|model2|parser
    }
)

merge_chain=prompt3|model1|parser

chain=parallel_chain|merge_chain
text="The Earth is the third planet from the Sun and the only astronomical object known to harbor life. It has a diameter of about 12,742 km and a mass of about 5.97 x 10^24 kg. The Earth's atmosphere is composed mainly of nitrogen and oxygen, and it has a magnetic field that protects it from solar radiation. The Earth orbits the Sun at an average distance of about 149.6 million km and takes about 365.25 days to complete one orbit.\nThe Earth has one natural satellite, the Moon, which orbits the Earth at an average distance of about 384,400 km. The Earth is home to a diverse range of ecosystems and is the only known planet to support life as we know it. It has a rich history of geological and biological evolution, and it continues to be a subject of scientific study and exploration.\nThe Earth is also facing various environmental challenges, such as climate change, deforestation, and pollution, which threaten the health and well-being of its inhabitants. Efforts are being made globally to address these issues and promote sustainable living on our planet.The Earth is the third planet from the Sun and the only astronomical object known to harbor life. It has a diameter of about 12,742 km and a mass of about 5.97 x 10^24 kg. The Earth's atmosphere is composed mainly of nitrogen and oxygen, and it has a magnetic field that protects it from solar radiation. The Earth orbits the Sun at an average distance of about 149.6 million km and takes about 365.25 days to complete one orbit.\nThe Earth has one natural satellite, the Moon, which orbits the Earth at an average distance of about 384,400 km. The Earth is home to a diverse range of ecosystems and is the only known planet to support life as we know it. It has a rich history of geological and biological evolution, and it continues to be a subject of scientific study and exploration.\nThe Earth is also facing various environmental challenges, such as climate change, deforestation, and pollution, which threaten the health and well-being of its inhabitants. Efforts are being made globally to address these issues and promote sustainable living on our planet."


result=chain.invoke({"text": text})
print(result)