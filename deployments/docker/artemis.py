from flask import Flask
from flask import render_template
app = Flask(_name_)
@app.route('/')
def index():
    return 'Welcome to Artemis E-commerse web application.'
if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')