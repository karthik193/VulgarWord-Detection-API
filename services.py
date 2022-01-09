
from helpers import splitIntoWords,get_Vectorizer_Model
from pandas import DataFrame


#services 

def detect(text):

    #spliting the given string into list of words  
    wordList  = splitIntoWords(text)

    #getting the trained Model, Vectorizer
    vectorizer , model  = get_Vectorizer_Model()

    #transform the words into vectors 
    df  = vectorizer.transform(DataFrame({"words" : [i for i in wordList] })["words"] )

    #predict

    result  = model.predict(df).tolist()

    print("result" , result , len(result))

    a = False 

    for i in range(len(result)) : 
        a = a | (result[i] == 1) 
    return a 


#services - END