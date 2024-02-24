from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') ## , methods['POST]
def intro():
    # return 'Welcome to our Page'
    return render_template('home_page.html') ## rendering html file in the webpage instead of plain str like above

@app.route('/about')
def about():
    return 'Welcome to About Page'

@app.route('/add')
def add(): ## for this to work, client need to give query param. not a prod lvl design, HTML rendering is better
    var1 = int(request.args.get('a')) ## by default, https will take it as string
    var2 = int(request.args.get('b'))

    return str(var1+var2) ## again we have to typecast to string when sending to client

app.run(debug=True)