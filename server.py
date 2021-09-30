from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def how_to():
    return "To play the game type /play or /play/(x) or /play/(x)/(color) into the URL"

@app.route("/play")
def lvl1():
    return render_template("index.html", number = 3)

@app.route("/play/<int:number>")
def lvl2(number):
    return render_template("index.html", number=number)

@app.route("/play/<int:number>/<string:color>")
def lvl3(number, color):
    return render_template("index.html", number=number, color=color)

if __name__ == "__main__":
    app.run(debug=True)