from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTVectorStoreIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
import sys
import os
import random

from IPython.display import Markdown, display
def random_key_openai():
    list_key = [
        "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",
    ]
    OPEN_API_KEY = random.choice(list_key)
    print("OPEN_API_KEY :" +OPEN_API_KEY)
    os.environ["OPENAI_API_KEY"]=OPEN_API_KEY
random_key_openai()
def construct_index(directory_path):
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0., model_name="gpt-3.5-turbo", max_tokens=1500))
 
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, chunk_size_limit=1024)
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
    return index

def ask_ai():
    index = construct_index("context_data/data")
    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)
    with open("response.txt","a") as res:
        res.writelines(response.response)
ask_ai()

