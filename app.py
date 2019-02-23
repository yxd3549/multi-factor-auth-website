from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html', user="fool")


@app.route("/login")
def simple_login():
    return render_template('login.html')

@app.route("/mobileLogin")
def mobile_login():
    return render_template("mobileLogin.html")

if __name__ == "__main__":
    app.run(debug=True)