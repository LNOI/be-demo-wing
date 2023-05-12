from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
import os
import re
import time
import random

def essay(essay:str,vol:str)->str:
    
    return ""

def random_key_openai():
    list_key = [
        "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",
        "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",
        "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",
    ]
    OPEN_API_KEY = random.choice(list_key)
    print("OPEN_API_KEY :" +OPEN_API_KEY)
    os.environ["OPENAI_API_KEY"]=OPEN_API_KEY