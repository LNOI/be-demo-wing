from pydantic import BaseModel, ValidationError, validator

class Essay(BaseModel):
    essay_id : int
    topic : str
    level : str
    # class Config:
    #     orm_mode = True


class Courses(BaseModel):
    
    class Config:
        orm_mode = True


class PromptSchema(BaseModel):
    content : str

    @validator("content")
    def content_less_300_words(cls,v):
        if len(v.split(" ")) > 300:
            raise ValueError("Essay content must be less than 300 words")
        return v
class EssaySchema(PromptSchema):
    topic : str
   


class StableDiffustionSchema(BaseModel):
    prompt : str
