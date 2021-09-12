from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/trap')
def trap():
    return render_template("trap.html")
if __name__ == '__main__':
    app.run(port=80,debug=True)
