from flask import Flask, request, render_template

app = Flask(__name__)

## Q1. Create a Flask application that displays "Hello, World!" on the homepage.

@app.route("/")
def index():
    return "Hello World"


## Q2. Write a Flask route that takes a name parameter and returns "Hello, [name]!" as plain text.

@app.route("/query")
def input_function():
    data = request.args.get('x')
    return "Hello {}".format(data)

## Q3. Write a Flask route that takes a number parameter and returns the square of that number as plain text.

@app.route("/square/<int:num>")
def square(num):
    return str(num**2)

## Q4. Write a Flask route that displays a simple HTML form that asks for a name and returns "Hello, [name]!" when submitted.

@app.route('/formname', methods = ['GET', 'POST'])
def names():
    if request.method == "POST":
        name = request.form['clientname']
        ourname = name

        return render_template('displayname.html', name=ourname)





if __name__=="__main__":
    app.run(host='0.0.0.0')

