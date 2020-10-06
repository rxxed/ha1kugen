import haikugen
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    first = second = third = ""
    if request.method == "POST":
        if request.form.get("generate") == "generate":
            first, second, third = haikugen.genhaiku()
    return render_template("index.html", first=first, second=second, third=third)

if __name__ == "__main__":
    app.run()
