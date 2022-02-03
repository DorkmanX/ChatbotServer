from flask import *

app=Flask(__name__)

text="Witaj"

def count(number):
    n=number
    n*=5
    return n


@app.get("/")
def hello():
    a=str(count(5))
    message={"answer":a}
    return jsonify(a)

if __name__=="__main__":
    app.run(debug=True)