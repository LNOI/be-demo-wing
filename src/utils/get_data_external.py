import requests
import ujson

def get_data_external(method:str|None,data:dict|None,url:str|None,headers:str|None):
    if method == "POST":
        res = requests.post(url=url,
                            data=data,
                        )
    return ujson.loads(res.content)
    