from flask import Flask, render_template, request

app = Flask(__name__)

database = ['connectwithavinash', 'sridhar', 'vashuagarwal', 'ishaanbagul', 'adepubharath', 'sai-sudhane-g']

##############
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/thankyou", methods=['POST'])
def registration():
    uname = request.form.get("user_name")
    uage = int(request.form.get("user_age"))
    return render_template("thankyou.html", uname=uname, uage=uage)

# Dynamic Routing
@app.route('/in/<user_name>')
def user_profile(user_name):
    if user_name in database:
        return render_template("user_profile.html", uname=user_name)
    return "Kindly register and come back."

##############


if __name__ == '__main__':
    app.run(debug=True)