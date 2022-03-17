import os, fnmatch
import webbrowser
import pandas as pd
from threading import Timer
from flask import Flask, render_template, request


app = Flask(__name__)

directory = "datasets\default_places"
options = []
for filename in os.listdir(directory):
    options.append(filename)

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
    file = find_all(str(selected),directory)[0]
    dataframe = pd.read_csv(file)[:10]
    dataset = dataframe.to_html()
    print(type(dataset))
    return render_template('base-index.html',table=dataset,data=options)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:4449/')

if __name__ == '__main__':
    Timer(1, open_browser).start();
    # Run the app server on localhost:4449
    app.run('localhost', 4449)