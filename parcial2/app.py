from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template, Environment, FileSystemLoader


app = Flask (__name__)

@app.route('/')
def my_form():
    return render_template('myform.html')

@app.route ('/', methods = ['POST'])
def form_post():
    text = request.form ['text']
    pro_text = text.upper()
    low_text = text.lower()

    return pro_text, low_text

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)