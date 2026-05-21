from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
from pydantic import BaseModel, Field,EmailStr

load_dotenv()

model=ChatOpenAI()

json_schema={
    "title": "Review",
    "description": "A structured representation of a review, including key themes, summary, sentiment, pros and cons, and the reviewer's name.",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "The main themes or topics discussed in the review"
        },
        "summary": {
            "type": "string",
            "description": "A concise summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "neutral", "negative"],
            "description": "The sentiment of the review, either 'positive', 'neutral' or 'negative'"
        },
        "pros": {
            "type": "array",
            "items": {
                "type": ["string", "null"]
            },
            "description": "A list of positive aspects mentioned in the review, if any"
        },
        "cons": {
            "type": "array",
            "items": {
                "type":  ["string", "null"]
            },
            "description": "A list of negative aspects mentioned in the review, if any"
        },
        "name": {
            "type": ["string", "null"],
            "description": "The name of the reviewer"
        }
    },
    "required": ["key_themes", "summary", "sentiment"]
}

structured_model=model.with_structured_output(json_schema)

result=structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)
print(result['summary'])
print(result['sentiment'])