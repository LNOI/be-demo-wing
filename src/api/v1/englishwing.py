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
        "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"
    ]
    OPEN_API_KEY = random.choice(list_key)
    print("OPEN_API_KEY :" +OPEN_API_KEY)
    os.environ["OPENAI_API_KEY"]=OPEN_API_KEY