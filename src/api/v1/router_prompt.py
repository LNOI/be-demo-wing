from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from src.db.base import SessionLocal, DBContext
from src.schemas.response_schema import ResponseModel
from src.schemas.Users import users_chema as schemas
from src.models import models
from src.services import gpt_services as GPT_Services
from src.const import const_map as CONST_MAP
from typing import List

router = APIRouter(
    prefix="/api/v1",
    tags=["api/v1"],
    dependencies=[]
)



@router.post("/suggestion", response_model=ResponseModel)
async def create_user(input_map: schemas.EssaySchema):
    print(input_map.topic)
    is_plagiarism = await GPT_Services.check_pligiarism(input_map.content)
    print(is_plagiarism)
    if  is_plagiarism:
        response = "Detect plagiarism"
    else:
        # response = "Not dao văn"
        response = await GPT_Services.call_gpt_suggestion(essay=input_map.content,
                                                        list_grammar=CONST_MAP.GRAMMAR_TOPIC[input_map.topic],
                                                        list_vocabulary=CONST_MAP.VOCABULARY_TOPIC[input_map.topic]
                                                        )
    return ResponseModel(status_code=200,
                         message="suggestion",
                         data=response
                         )

@router.post("/call_gpt", response_model=ResponseModel)
async def call_gpt(input_map: schemas.PromptSchema):
    # is_plagiarism = await GPT_Services.check_pligiarism(input_map.content)
    # if is_plagiarism:
    #     response = "Detect plagiarism"
    # else:
    #     response = "Not dao văn"
    return ResponseModel(status_code=200,
                         message="call gpt",
                         data=""
                         )


@router.post("/stable_diffustion", response_model=ResponseModel)
async def stable_diffustion(input_map: schemas.StableDiffustionSchema):
    print(input_map.prompt)
    response = await GPT_Services.generate_images(prompt=input_map.prompt,negative_prompt="")
    try:
        if  "message" in response and  response["message"]=="Your monthly limit exceeded, upgrade subscription now on https://stablediffusionapi.com/pricing":
            response = [
                "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/1cbcc7e6-6356-4966-a6e5-a6e4dc0821cd-0.png",
                "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/1cbcc7e6-6356-4966-a6e5-a6e4dc0821cd-1.png",
                "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/1cbcc7e6-6356-4966-a6e5-a6e4dc0821cd-2.png",
                "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/1cbcc7e6-6356-4966-a6e5-a6e4dc0821cd-3.png"
            ]
        else:
            response = response["output"]
    except Exception as e:
        
        response = [
                "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/1cbcc7e6-6356-4966-a6e5-a6e4dc0821cd-0.png",
                "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/1cbcc7e6-6356-4966-a6e5-a6e4dc0821cd-1.png",
                "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/1cbcc7e6-6356-4966-a6e5-a6e4dc0821cd-2.png",
                "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/1cbcc7e6-6356-4966-a6e5-a6e4dc0821cd-3.png"
        ]
    print(response)
    return ResponseModel(status_code=200,
                         message="Generate Image",
                         data=response
                         )

