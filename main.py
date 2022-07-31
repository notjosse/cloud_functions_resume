from flask import render_template
import functions_framework

@functions_framework.http
def resume(request):
    return render_template('index.html')