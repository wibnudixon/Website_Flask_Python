from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home goes here!"

@app.route('/about/')
def about():
    return "Webiste content goes here!"

if __name__=="__main__":
    app.run(debug=True)

