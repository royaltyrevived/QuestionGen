from flask import Flask, json, Response, request, render_template, url_for
from werkzeug.utils import secure_filename, redirect
from os import path, getcwd, error
import time
from db import Database
import sqlite3
import re
app = Flask(__name__)

app.db = Database()

def lda():
    


@app.route('/enter-question',methods=['POST'])
def enterquestion():
    error= None
    if request.method== 'POST'
        question=request.form('question')
        subject=request.form('subject')
        complexity=request.form('complexity')

    return None

