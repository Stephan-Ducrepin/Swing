from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/immigration')
def immigration():
    heading = "Immigration"
    message= "With millions of people attempting to migrate to the United States every year, immgration is a controversial topic that candidates spend a lot of time debating. Use the survey underneath to determine where you stand on the matter."
    image = "/static/images/idk.jpg"
    topic = 'immigration'
    return render_template('landing.html', message = message, heading = heading, image = image, topic=topic)

@app.route('/abortion')
def abortion():
    heading = "Abortion"
    message = "To what extent do you think the government should be involved in protecting the rights of abortion for women in America? Use the survey underneath to determine where you stand on the matter."
    image = "/static/images/pink.png"
    topic = 'abortion'
    return render_template('landing.html', heading=heading, message=message,image=image, topic = topic )

@app.route('/lgbtq')
def lgbtq():
    heading = 'LGBTQ'
    message= 'How do you feel about the integration of LGBTQ+ people into greater society? Use the survey underneath to determine where you stand on the matter.'
    image = '/static/images/idk5.jpg'
    topic= 'lgbtq'
    return render_template('landing.html', message=message, heading=heading,image=image, topic = topic)
# @app.route('/lsurvey')
# def 

@app.route('/civil_rights')
def civil_rights():
    heading = 'Civil Rights'
    message = 'To what extent do you think should the society or the government invest in advancing the rigts of the marginalized groups? Use the survey underneath to determine where you stand on the matter.'
    image = '/static/images/rights.jpg'
    topic = 'civil_rights'
    return render_template('landing.html', message=message, heading=heading,image=image, topic=topic)

@app.route('/gun_control')
def gun_control():
    heading = "Gun Control"
    return render_template('gun_control.html')

@app.route('/student_loans')
def student_loans():
    return render_template('student_loans.html')
    
@app.route('/survey/<topic>')
def survey(topic):
    # topic = request.args['topic']
    if topic == 'immigration':
        question = 'On a Scale of 1-10, how strongly do you support America being more open to immigration, legal and otherwise?'
    elif topic == 'abortion':
        question = 'On a scae of 1-10, aboriton' 
    elif topic == 'lgbtq':
        question = 'On a scale of 1-10, how strongly do you feel on lgbtq rights?'
    elif topic == 'civil_rights':
        question = "On a scale of 1-10, how strongly do you feel on civil rights?"
    return render_template('iSurvey.html', question = question)
    
@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == 'GET':
        return render_template('iSurvey.html')
    else:
        value = int(request.form['istance'])
        value1=int(request.form['istance1'])
        print (value+value1)
        if (value+value1) >= 5:
            return render_template('otherResults.html')
        else:
            return render_template('results.html', value=value)
    
    
