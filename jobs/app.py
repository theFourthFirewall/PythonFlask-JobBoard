from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')


# @app.route('/jobs')
# def jobs():
#     return render_template('index.html')
# create route() decorator with URL of '/' as argument
