# # app.py
# from flask import Flask, render_template, request
# from textblob import TextBlob

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     sentiment = None
#     polarity = None
#     subjectivity = None

#     if request.method == "POST":
#         user_text = request.form["user_text"]
#         blob = TextBlob(user_text)
#         polarity = blob.sentiment.polarity
#         subjectivity = blob.sentiment.subjectivity

#         # classify sentiment
#         if polarity > 0:
#             sentiment = "Positive 🙂"
#         elif polarity < 0:
#             sentiment = "Negative 😟"
#         else:
#             sentiment = "Neutral 😐"

#     return render_template("index.html", sentiment=sentiment,
#                            polarity=polarity, subjectivity=subjectivity)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, polarity, subjectivity

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    polarity = None
    subjectivity = None
    
    if request.method == "POST":
        user_text = request.form["user_text"]
        sentiment, polarity, subjectivity = analyze_sentiment(user_text)
    
    return render_template("index.html", 
                           sentiment=sentiment, 
                           polarity=polarity, 
                           subjectivity=subjectivity)

if __name__ == "__main__":
    app.run(debug=True)
