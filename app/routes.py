from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/immigration')
def immigration():
    return render_template('landing.html')
    
@app.route('/survey')
def survey():
    return render_template('iSurvey.html')
    
@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == 'GET':
        return render_template('iSurvey.html')
    else:
        value = int(request.form['istance'])
        print (value)
        if value >= 5:
            return render_template('otherResults.html')
        else:
            return render_template('results.html', value=value)
    
    
