import os, fnmatch
import webbrowser
import pandas as pd
import pipeline_model
from threading import Timer
from flask import Flask, render_template, request


app = Flask(__name__)

directory = "datasets\default_places"
options = []
mapping = {}
for filename in os.listdir(directory):
    name_stripped = filename.split(".")[0].replace("_"," ").capitalize()
    mapping[name_stripped] = filename
    options.append(name_stripped)

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

@app.route('/')
def index():
    return render_template('base-index.html', data=options)

@app.route("/processing" , methods=['GET', 'POST'])
def processing():
    selected = request.args.get('data')
    chosen = mapping.get(selected)
    try:
        file = find_all(str(chosen),directory)[0]
    except:
       return render_template('base-index.html',invalid="Requested location not present",data=options)
    dataset = pipeline_model.present(file) # this would 
    return render_template('base-index.html',table=dataset,data=options)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:4449/')

if __name__ == '__main__':
    Timer(1, open_browser).start();
    # Run the app server on localhost:4449
    app.run('localhost', 4449)