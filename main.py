from flask import Flask,jsonify
import calculation


app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("welcome to flask")
    return "Success"

@app.route('/addition')

def add():
    x=100
    y=200
    result=calculation.get_addition(x,y)
    return jsonify({"result": f"addition of {x} and {y} is {result}"})



if __name__ == "__main__":

    app.run(host='0.0.0.0', port = 5000 , debug=True)

