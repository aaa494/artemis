from flask import Flask
from flask import render_template
app = Flask(_name_)
@app.route('/')
def index():
    return 'Example code from dev-feature/example'
if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')