from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True
form = """ 
<!DOCTYPE html>
<html>
    <body>
        <form action="/hello"  method="POST">
        <label for="first_name">First Name</label>
            <input id="first_name" type="text" name="first_name"/>
            <input type="submit"/>
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/hello",methods=['POST','GET'])
def hello():
    first_name = request.form['first_name']
    return "<H1>Hello, "+first_name+"!</h1>"


app.run()