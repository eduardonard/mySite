from flask import Blueprint, render_template, url_for, flash, redirect

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("homepage.html")

@main.route("/proTips")
def proTips():
    return render_template("proTips/proTips.html")

@main.route("/test")
def test():
    return render_template("test/test.html")