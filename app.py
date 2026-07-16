from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return "Hello this is DevOps Lab"

if __name__ == '__main__':
    app.run(debug=True)