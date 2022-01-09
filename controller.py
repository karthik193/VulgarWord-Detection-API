# Controller for redirecting the request calls to their respective services


#IMPORTs

from typing import List, Optional 

from fastapi import FastAPI 

from pydantic import BaseModel

from services import detect

#end IMPORTs 


#initializing app 

app  = FastAPI()


class Document(BaseModel):
    title : str 
    description : Optional[str] = None  
    content : str
    hashtags : List[str]

@app.get('/')
def describe():
    return 
    {
        'Hello' : "I am an API which detects Vulgar Words in a given text"
    }


@app.post('/train')
def TrainModel(id : str, text : str ):
    #can only done by authorized users
    # verify 'id'
    # if valid 'id'  - train the model 
     
    return "model trained"

@app.post('/detectWords/')
def detectVulgarWords(text : str ):
    if(text == None): 
        return None 
    
    return {
        'there' : detect(text), 
        'ranges' : []
    }

 