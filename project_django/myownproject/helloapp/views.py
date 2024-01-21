# helloapp/views.py
from django.http import HttpResponse

def hello_world(request):
    html_content = """
    <html>
    <head>
        <title>Hello,it is me arun kumar!</title>
        <style>
            body {
                background-color: #000000; /* black background */
                font-family: 'Arial', sans-serif;
                text-align: center;
                margin-top: 100px;
            }
            h1 {
                color: #ff0000; /* red text color */
            }
        </style>
    </head>
    <body>
        <h1>Hello,it is me arun kumar!</h1>
    </body>
    </html>
    """
    return HttpResponse(html_content)
