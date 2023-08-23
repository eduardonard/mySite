from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')



from mySite.main import routes
from mySite.proTips import routes