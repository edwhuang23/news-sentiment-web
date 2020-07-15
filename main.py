from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    return redirect(url_for('analyze'))

@app.route("/analyze")
def analyze():
    return "Analysis..."

if __name__ == "__main__":
    app.run(debug=True)
