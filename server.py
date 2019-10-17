from flask import Flask,request

app=Flask(__name__)

print(app)

@app.route('/')
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(port='3000')