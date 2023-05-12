
from src.const.const_map import PROMP_SUGGESTION_TEMPLATE,MODEL_NAME
from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTVectorStoreIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from src.utils.get_data_external import get_data_external
import json
import requests
import os
os.environ["OPENAI_API_KEY"] = "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"
async def check_pligiarism(essay: str | None)->bool:
    headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer 1301978B8B90041B21105135A0E7A002D8EBC4F48E0EA9035E43E0270E1210A9'
    }
    content = essay

    myobj = json.dumps({'text':content})

    response = requests.post('https://api.copyleaks.com/v2/writer-detector/thanhlointh-1252023/check', headers=headers, data=myobj)
    response = json.loads(response.content)
    h= response['summary']['human']
    ai = response['summary']['ai']
    if h-ai>0:
        print("An essay not pligiarism")
        return False
    print("An essay pligiarism")
    return True

def construct_index(directory_path):
    if MODEL_NAME == "gpt-3.5-turbo":
        llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.0, model_name=MODEL_NAME, max_tokens=1500))
    else:
        llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.0, model_name=MODEL_NAME, max_tokens=1500))
    documents = SimpleDirectoryReader(directory_path).load_data()    
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, chunk_size_limit=1024)
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
    return index

index = construct_index("context_data/data")
query_engine = index.as_query_engine()

async def call_gpt_suggestion(essay: str | None, list_grammar: str | None, list_vocabulary: str|None):
    prompt_suggestion = PROMP_SUGGESTION_TEMPLATE.format(list_grammar=list_grammar,list_vocabulary=list_vocabulary,essay=essay)
    
    response = query_engine.query(prompt_suggestion)
    return response


async def call_gpt(prompt: str | None):
    prompt_suggestion = prompt
    response = query_engine.query(prompt_suggestion)
    return response


async def generate_images(prompt: str | None,negative_prompt:str|None):
    data = {
        "key": "e9omMZ7TnFpIy3vN9m4Irxf5CpNY0rK73dHoNXd6p05Y45Y7jtigsWvSNv91",
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": "256",
        "height": "256",
        "samples": "4",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker":"yes",
        "webhook": None,
        "track_id": None
    }
    try:
        res = get_data_external(method="POST",
                                data=data,
                                url="https://stablediffusionapi.com/api/v3/text2img",
                                headers=None
                                )
    except Exception as e:
        print(e)
        
    return res


