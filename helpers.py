
import pickle



MODEL_PICKEL_FILENAME = "toxic_msgs_logistic_regression_and_vector.pkl"

def splitIntoWords(text):
    return list(text.split(' '))

def get_Vectorizer_Model():
    model = None
        
    with open(MODEL_PICKEL_FILENAME, 'rb') as f:
            vectorizer, model = pickle.load(f)
       
    return vectorizer , model