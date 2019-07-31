from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/index2')
@app.route('/')
def index2_home():
    return render_template ('index2-home.html')
    
@app.route('/candidates')
def candidateLandingPage():
    return render_template('candidateLandingPage.html')
@app.route('/candidatebio')
def candidateBios():
    return render_template('candidateBios.html')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/immigration')
def immigration():
    heading = "Immigration"
    message= "With millions of people attempting to migrate to the United States every year, immgration is a controversial topic that candidates spend a lot of time debating. Use the survey underneath to determine where you stand on the matter."
    image = "/static/images/immigration3.jpg"
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
    topic = 'lgbtq'
    return render_template('landing.html', message=message, heading=heading,image=image, topic=topic)
# @app.route('/lsurvey')
# def 

@app.route('/civil_rights')
def civil_rights():
    heading = 'Civil Rights'
    message = 'To what extent do you think should the society or the government invest in advancing the rigts of the marginalized groups? Use the survey underneath to determine where you stand on the matter.'
    image = '/static/images/rights.jpg'
    topic = 'civil_rights'
    return render_template('landing.html', message=message, heading=heading,image=image,topic=topic)

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
    print (topic)
    if topic == 'immigration':
        question = 'On a Scale of 1-10, how strongly do you support America being more open to immigration, legal and otherwise?'
        question2 = 'To what extent should the government forgive illegal immigrants?'
    elif topic=='abortion':
        question = 'On a scale of 1-10, how strongly do you feel about abortion?'
        question2 = 'Should the govt be pro-life or pro-choice?'
    elif topic=='civil_rights':
        question = 'On a scale of 1-10, how strongly do you feel about civil rights?'
        question2 = 'Should the government protect the rights of and respect the gender identity of transgender people?'
    elif topic=='lgbtq':
        question = 'On a scale of 1-10. how strongly do you feel about the integration of lgbtq ppl in society?'
        question2 = 'Should the government focus on #MeToo, or is it unnecessary? Should marijuana be legalized?'
    return render_template('iSurvey.html', question = question, question2 = question2, topic=topic)
    
@app.route('/results/<topic>', methods = ['GET', 'POST'])
def results(topic):
    print (topic + 'again')
    if request.method == 'GET':
        print ('its not working')
        return render_template('iSurvey.html')
    else:
        value = int(request.form['istance'])
        value1= int(request.form['istance1'])
        print (value)
        if (value+value1) >= 10:
            print ('lol')
            print (value+value1)
            if topic == 'immigration':
                otherResultsblurb= ' Elizabeth Warren wishes to eliminate criminal penalties for those crossing the border without papers. She also wishes to reduce immigration detention. Learn more about Senator Warrens past decisions on immigration'
            elif topic == 'abortion':
                otherResultsblurb = 'liz is pro-choice, i think'
            elif topic == 'lgbtq':
                otherResultsblurb = 'liz is For The Gays'
            elif topic == 'civil_rights':
                otherResultsblurb = 'Liz said blm'
            return render_template('otherResults.html', value = value, value1=value1, otherResultsblurb=otherResultsblurb, topic=topic)
        else:
            if topic == 'immigration':
                resultsblurb= 'trump said no one can come over anymore srry'
            elif topic == 'abortion':
                resultsblurb = 'Donald Trump is pro-life, i think'
            elif topic == 'lgbtq':
                resultsblurb = 'Trump is Against the Gays'
            elif topic == 'civil_rights':
                resultsblurb = 'Trump said: black lives ZONT matter'
            return render_template('results.html', value=value, value1=value1, resultsblurb=resultsblurb, topic=topic)
    
    
