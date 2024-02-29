from flask import Flask, render_template, request
import re

app = Flask(__name__)

## define routes
@app.route('/')
def homePage():
    return render_template('page.html')

## post will make query params hidden in the client request url
@app.route('/add', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        var1 = int(request.form['a'])
        var2 = int(request.form['b'])    
    else:
        var1 = int(request.args.get('a'))
        var2 = int(request.args.get('b'))

    return str(var1+var2)

@app.route('/login', methods=['POST'])
def sign_in():
    user = request.form['user_email']
    print(user)
    pattern = "^[a-zA-Z0-9]*"
    user_name = re.match(pattern, user)
    user_name = user_name.group()

    return "Welcome {}!. Thank you for visiting our page".format(user_name)

## dynamic routes
@app.route('/user/<user_name>')
def users(user_name):

    return "Welcome {}!. Thank you for visiting our page".format(user_name)


app.run(debug=True)