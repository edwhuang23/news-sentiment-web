from flask import Flask, request, url_for, redirect, render_template
from analyze import textAnalyze, imageAnalyze

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        textInput = request.form.get("articleText")
        return redirect(url_for('analyze', text=textInput))

    return render_template("home.html")


@app.route("/analyze")
def analyze():
    responseString = ""

    # Analyze image
    imageSentiment = imageAnalyze("Happy!")
    responseString += "The image sentiment is "

    if imageSentiment == 1:
        responseString += "positive. "
    elif imageSentiment == -1:
        responseString += "negative. "

    # Analyze text
    textSentiment = textAnalyze(request.args['text'])
    responseString += "The text sentiment is "

    if textSentiment == 1:
        responseString += "positive."
    elif textSentiment == -1:
        responseString += "negative."

    return responseString

if __name__ == "__main__":
    app.run(debug=True)
