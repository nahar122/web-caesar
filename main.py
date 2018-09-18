from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            button {
                background-color: #3366ff;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <form method="POST">
            <h1>Rotate by:</h1><input type="text" name="rot" value=0><br><br>
            <textarea name="text"></textarea>
            <input type="submit">
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form
@app.route("/",methods=['POST'])
def encryption():
    rot = int(request.form["rot"])
    text = request.form["text"]
    jumbled_test = rotate_string(text,rot)
    return "<h1>" + jumbled_test + "</h1>"
    
app.run()