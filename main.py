from flask import Flask, request, url_for, redirect, render_template
from analyze import textAnalyze, makeDecision
from imageanalysisTest import imageAnalyze
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = {'jpg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file'] if request.files['file'] else None
        textInput = request.form.get("articleText") if request.form.get("articleText") else ""

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = ""
        return redirect(url_for('analyze', text=textInput, image=filename))

    return render_template("home.html")


@app.route("/analyze")
def analyze():
    responseString = ""

    # Analyze image
    if request.args['image'] != "":
        imageSentiment = imageAnalyze(request.args['image'])
        responseString += "The image sentiment is " + imageSentiment
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], request.args['image']))

    # Analyze text
    if request.args['text'] != "":
        processedText, pickled_model = textAnalyze(request.args['text'])
        responseString += "The text sentiment is " + makeDecision(processedText, pickled_model)

    return render_template("results.html", value=responseString)

if __name__ == "__main__":
    app.run(debug=True)
