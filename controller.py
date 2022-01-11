# Controller for redirecting the request calls to their respective services


#IMPORTs

from typing import List, Optional 

from fastapi import FastAPI 

from fastapi.middleware.cors import CORSMiddleware 

from pydantic import BaseModel

from services import detect

#end IMPORTs 


#initializing app 

app  = FastAPI()


#adding cors middleware for authentication 

app.add_middleware(
    CORSMiddleware, 
    allow_origins =['*'], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#end CORS 

class Document(BaseModel):
    title : Optional[str] = None  
    description : Optional[str] = None  
    content : str
    hashtags : Optional[List[str]] = None


class PlainText(BaseModel): 
    text : str  

@app.get('/')
def describe():
    return {
        'Hello' : "I am an API which detects Vulgar Words in a given text"
    }


@app.post('/train')
def TrainModel(id : str, text : str ):
    #can only done by authorized users
    # verify 'id'
    # if valid 'id'  - train the model 
     
    return "model trained"

@app.post('/detectWords')
def detectVulgarWords(pt : PlainText):
    if(pt == None or pt.text == None): 
        return None 
    
    return {
        'toxic' : detect(pt.text), 
        'ranges' : []
    }

 