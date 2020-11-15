import numpy as np
import flask
from flask import Flask, render_template, request, url_for
import pickle
import heapq
from keras.models import load_model
from nltk.tokenize import RegexpTokenizer
from keras.models import model_from_json

def prepare_input(text):
    
    x = np.zeros((1, WORD_LENGTH, len(unique_words)))
    for t, word in enumerate(text.split()):
        # print(word)
        x[0, t, unique_word_index[word]] = 1
    return x

def sample(preds, top_n=3):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)

    return heapq.nlargest(top_n, range(len(preds)), preds.take)

def predict_completions(text, n=3):
    x = prepare_input(text)
    preds = loaded_model.predict(x, verbose=0)[0]
    next_indices = sample(preds, n)
    return [unique_words[idx] for idx in next_indices]
    
WORD_LENGTH = 5
tokenizer =  pickle.load(open("tokenizer.p", "rb"))
unique_words =  pickle.load(open("unique_words.p", "rb"))
unique_word_index =  pickle.load(open("unique_word_index.p", "rb"))

# model = load_model('keras_next_word_model.h5')
# history = pickle.load(open("history.p", "rb"))
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")

# Initiate flask
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('word_prediction.html')

# Initiate flask
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('word_prediction.html')

@app.route('/Predict', methods=['POST'])
def Predict():
    
    if request.method == 'POST':
        text_inp = request.form['message']
        
        if len(text_inp.split()) > 5:
            seq = " ".join(tokenizer.tokenize(text_inp.lower())[len(text_inp.split())-5:])
            a = predict_completions(seq, 5)
            b = ', '.join(a)
        else:
            seq = " ".join(tokenizer.tokenize(text_inp.lower())[0:5])
            a = predict_completions(seq, 5)
            b = ', '.join(a)
#         b = request.form['message']
    return render_template('word_prediction.html', next_words=b)

if __name__ == '__main__':
    app.run(debug = False)