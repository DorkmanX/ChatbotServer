from flask import *

app=Flask(__name__)

text="Ale jaja"

def count(number):
    n=number
    n*=5
    return n


@app.get("/")
def hello():
    a=str(count(5))
    message={"answer":a}
    return str(a)

if __name__=="__main__":
    app.run()