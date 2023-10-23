from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return "Hellow World"

@app.route("/a")
def Achu():
    return "Hellow Achu"
@app.route("/d")
def Dundu():
    return "Hellow Dundu"
if __name__ == "__main__":
    app.run(debug=True)