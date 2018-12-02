from flask import Flask, render_template, redirect, url_for,request
from flask import make_response

app = Flask(__name__)

@app.route("/")
def home():
    import testInter
    testInter.interfaceTk()
    return "Programa Terminado"

@app.route("/index")

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
        result = "return this"
        resp = make_response('{"response": '+result+'}')
        resp.headers['Content-Type'] = "application/json"
        return resp
        return render_template('login.html', message='')

if __name__ == "__main__":
    app.run(debug = True)