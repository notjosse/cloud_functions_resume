from flask import render_template
import functions_framework

@functions_framework.http
def hello_world(request):
    return render_template('index.html')