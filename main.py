from flask import render_template

def hello_world(request):
    return render_template('index.html')