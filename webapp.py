import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];   

@app.route('/')
def renderMain():
    


    
if __name__=="__main__":
    app.run(debug=True)
