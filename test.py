import os
import urllib.parse

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, g
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from functools import wraps

open("study.db").close()
db = SQL("sqlite:///study.db")

subject_id = db.execute("""SELECT subject_id FROM assignments WHERE user_id=:user_id""", user_id=3)
sbjnumber = len(subject_id)

subscores = []
for i in range(sbjnumber):
    j = []
    subscore = db.execute("""SELECT score1, score2, score3, score4, score5, score6 FROM assignments WHERE user_id=:user_id AND subject_id=:subject_id""", user_id=3, subject_id=subject_id[i]["subject_id"])
    j.append(subscore[0]['score1'])
    j.append(subscore[0]['score2'])
    j.append(subscore[0]['score3'])
    j.append(subscore[0]['score4'])
    j.append(subscore[0]['score5'])
    j.append(subscore[0]['score6'])
    subscores.append(j)


print(f"{subscores}")