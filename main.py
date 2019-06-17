from flask import Flask, request, redirect
import cgi

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
    return "<H1>Hello, "+cgi.escape(first_name)+"!</h1>"

time_form = """ 
<!DOCTYPE html>
<html>
<style>
    .error{{color:red;}}
</style>
    <body>
        <h1>Validate Time </h1>
        <form method="POST">
        <label>Hour (24 Hour Format)
            <input value="{hours}" type="text" name="hours"/>
        </label>
        <p class = "error">{hours_error} </p>
        <label>Minutes
            <input value="{minutes}" type="text" name="minutes"/>
        </label>
        <p class = "error">{minutes_error} </p>
        <input type="submit" Value="Convert"/>

        </form>
    </body>
</html>
"""
@app.route("/validate-time")
def display_time():
    return time_form.format(hours='',hours_error='',minutes='',minutes_error='')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/validate-time", methods=['POST'])
def validate_time():
    hours = request.form['hours']
    minutes = request.form['minutes']
    hours_error=''
    minutes_error=''
    if not is_integer(hours):
        hours_error = "Not a valid integer."
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = "Hours value out of range (0-23)"
            hours = ''
    if not is_integer(minutes):
        minutes_error = "Not a valid integer"
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = "Minutes value out of range (0-59)"
            minutes = ''
    if not hours_error and not minutes_error:
        time = str(hours)+":"+str(minutes)
        return redirect("/valid-time?time={0}".format(time))
    else:
        return time_form.format(hours=hours,hours_error=hours_error,minutes=minutes,minutes_error=minutes_error)
 
@app.route("/valid-time")
def valid_time():
    time = request.args.get('time')
    return "<h1>You submitted {0}. Thank you for submitting a valid time!! </h1>".format(time)

app.run()