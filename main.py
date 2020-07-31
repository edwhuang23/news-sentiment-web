from flask import Flask, request, url_for, redirect, render_template
from analyze import textAnalyze, imageAnalyze
import os

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "/uploads"

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.files:
            imageInput = request.files["image"]
            #imageInput.save(os.path.join(app.config["IMAGE_UPLOADS"], imageInput.filename))
            textInput = request.form.get("articleText")
            return redirect(url_for('analyze', text=textInput, image=imageInput))

    return render_template("home.html")


@app.route("/analyze")
def analyze():
    responseString = ""

    # Analyze image
    imageSentiment = imageAnalyze(request.args['image'])
    responseString += "The image sentiment is "

    if imageSentiment == 1:
        responseString += "positive. "
    elif imageSentiment == -1:
        responseString += "negative. "

    # Analyze text
    textSentiment = textAnalyze(request.args['text'])
    responseString += "The text sentiment is " + textSentiment


    return responseString

if __name__ == "__main__":
    app.run(debug=True)
