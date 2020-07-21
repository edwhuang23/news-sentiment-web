from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        textInput = request.form.get("articleText")
        return redirect(url_for('analyze', text=textInput))

    return render_template("home.html")


@app.route("/analyze")
def analyze():
    return "Analysis of: " + request.args['text']

if __name__ == "__main__":
    app.run(debug=True)
