import os
import urllib.parse

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, g
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from functools import wraps
from trivia import login_required


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
open("study.db").close()
db = SQL("sqlite:///study.db")

@app.route("/")
def index():
    return render_template("index.html")

def warning(PWorNAMEorCON):
    if not request.form.get(PWorNAMEorCON):
        flash(f"Please Enter Your {PWorNAMEorCON}")
        return redirect(request.referrer)

def warn(PWorNAME):
    if not request.form.get(PWorNAME):
        flash(f"Please Enter Your {PWorNAME}")
        return redirect(request.referrer)

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        signup_check = warning("username") or warning("password") or warning("confirmation")
        if signup_check is not None:
            return signup_check
        if request.form.get("password") != request.form.get("confirmation"):
            flash("Confirmation does not match with Password.")
            return redirect("sign_up.html")
        try:
            primary = db.execute("INSERT INTO students (username, hash) VALUES (:username, :hash)",
                username=request.form.get("username"),
                hash=generate_password_hash(request.form.get("password")))
        except:
            flash("Username Already Exist")
            return redirect(request.referrer)

        if primary is None:
            flash("Registration Error")
            return redirect("sign_up.html")
        session["user_id"] = primary
        return redirect("/schedule")
    else:
        return render_template("sign_up.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_check = warn("username") or warn("password")
        if login_check is not None:
            return login_check

        session.clear()

        # Query database for username
        rows = db.execute("SELECT * FROM students WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Invalid Username and/or Password")
            return redirect("login.html")
        else:
            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]
        course = db.execute("""SELECT subject, code, target, weight, assignment1, assignment2, assignment3, assignment4, assignment5, assignment6, due1, due2, due3, due4, due5, due6 FROM schedule
        WHERE user_id=:user_id""", user_id=session["user_id"])
        return render_template("schedule.html", course=course)

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()

    return redirect("/")

@app.route("/schedule", methods=["GET", "POST"])
@login_required
def schedule():
    if request.method == "POST":
        subject = request.form.get("subject")
        code = request.form.get("code")
        target = request.form.get("target")
        weight = request.form.get("weight")
        asm1 = request.form.get("asm1")
        asm2 = request.form.get("asm2")
        asm3 = request.form.get("asm3")
        asm4 = request.form.get("asm4")
        asm5 = request.form.get("asm5")
        asm6 = request.form.get("asm6")
        due1 = request.form.get("due1")
        due2 = request.form.get("due2")
        due3 = request.form.get("due3")
        due4 = request.form.get("due4")
        due5 = request.form.get("due5")
        due6 = request.form.get("due6")
        weight1 = request.form.get("weight1")
        weight2 = request.form.get("weight2")
        weight3 = request.form.get("weight3")
        weight4 = request.form.get("weight4")
        weight5 = request.form.get("weight5")
        weight6 = request.form.get("weight6")
        if subject is not None:
            db.execute("""INSERT INTO schedule (subject, code, user_id, target, weight)
                VALUES (:subject, :code, :user_id, :target, :weight)""",
                subject = subject,
                code = code,
                user_id = session["user_id"],
                target = target,
                weight = weight)
        elif asm1 is not None:
            db.execute("""INSERT INTO schedule (assignment1, due1, weight1, assignment2, due2, weight2, assignment3, due3, weight3, assignment4, due4, weight4, assignment5, due5, weight5, assignment6, due6, weight6)
                VALUES (:assignment1, :due1, ;weight1, :assignment2, :due2, ;weight2, :assignment3, :due3, ;weight3, :assignment4, :due4, ;weight4, :assignment5, :due5, ;weight5, :assignment6, :due6 ;weight6)""",
                assignment1 = asm1,
                assignment2 = asm2,
                assignment3 = asm3,
                assignment4 = asm4,
                assignment5 = asm5,
                assignment6 = asm6,
                due1 = due1,
                due2 = due2,
                due3 = due3,
                due4 = due4,
                due5 = due5,
                due6 = due6,
                weight1 = weight1,
                weight2 = weight2,
                weight3 = weight3,
                weight4 = weight4,
                weight5 = weight5,
                weight6 = weight6)
        course = db.execute("""SELECT subject, code, assignment1, assignment2, assignment3, assignment4, assignment5, assignment6 FROM schedule
        WHERE user_id=:user_id""", user_id=session["user_id"])
        return render_template("schedule.html", course=course)
    else:
        course = db.execute("""SELECT subject, code, assignment1, assignment2, assignment3, assignment4, assignment5, assignment6,
        due1, due2, due3, due4, due5, due6, weight1, weight2, weight3, weight4, weight5, weight6 FROM schedule
        WHERE user_id=:user_id""", user_id=session["user_id"])
        return render_template("schedule.html", course=course)

@app.route("/subject", methods=["GET", "POST"])
@login_required
def subject():
    if request.method == "POST":
        return render_template("subject.html")
    else:
        return render_template("subject.html")

@app.route("/record", methods=["GET", "POST"])
@login_required
def record():
    if request.method == "POST":
        return render_template("record.html")
    else:
        return render_template("record.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    flash("Unexpected Error")
    return redirect(request.referrer)



# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)