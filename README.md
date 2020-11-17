# Next-Word-Predict-Sample

Deployment link: https://sample-next-word-prediction.herokuapp.com/

Model training refered from https://medium.com/analytics-vidhya/build-a-simple-predictive-keyboard-using-python-and-keras-b78d3c88cffb

- Data used-  Sherlock Holmes Novel
- Model- LSTM
- Web app built using Flask
- Deployed in Heroku

FYI: This is the basic model. It has few drawbacks which I will handle in future as I am unable to handle now due to my laptop limitations, and when attempted to handle them, it is killing my laptop. :(

Drawbacks:
1) If the new word is give as an input (word which is not used in training the model), it will fail.
2) If the spelling is wrong, it will fail.
3) Couldn't train on big data set due to laptop limitations.

* Will be working on this in future to optimise it.


