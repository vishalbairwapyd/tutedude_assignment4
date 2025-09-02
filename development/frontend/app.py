from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def to_do_form():
    return render_template("to_do.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)