from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    message = request.form["message"]
    return f"<h3>Thank you, {name}!<br>Your message: {message}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
