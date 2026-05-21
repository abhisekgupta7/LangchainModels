from pydantic import BaseModel, Field,EmailStr
from typing import Optional

class Student(BaseModel):
    name: str ='nitish'
    age: Optional[int] = Field(None, description="The age of the student")
    email:EmailStr
    cgpa:float=Field(gt=0,lt=4,description="The CGPA of the student must be between 0 and 4",default=3.5)

new_student=Student(name="Nitish")
student=Student(**new_student.dict())