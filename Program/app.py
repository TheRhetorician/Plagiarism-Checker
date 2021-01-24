import os
from flask import Flask, render_template, request
from pre_process import *
from give_docs import *
import pickle
from load_data import *
from create_database import *
from calc_score import *
from scan_plagiarism import *
import operator

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)

    path = destination
    category_words_docs, id_name, term_freq_db, doc_freq_db, tf_idf_db = load_data()
    sim_score =  scan_plagiarism(path, category_words_docs, id_name, 0.5)

    return render_template("result.html", sim_score=sim_score)

if __name__ == '__main__':
    app.run(debug = True)