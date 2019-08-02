from app import app
from flask import render_template, request
from app.models import model, formopener, api_practice




@app.route('/home')
@app.route('/')
def homephome():
    return render_template ('index2-home.html')
    
@app.route('/candidates')
def candidateLandingPage():
    return render_template('candidateLandingPage.html')
    
@app.route('/about')
def aboutusPage():
    return render_template('about.html')
        
@app.route('/representatives')
def repPage():
    return render_template('api rep.html')
    
@app.route('/warren')
def warren():
    heading = 'Elizabeth Warren'
    info = 'Elizabeth Ann Warren, born on June 22, 1949, is an American politician and former academic serving as the senior United States Senator from Massachusetts since 2013.Warren was formerly a law school professor specializing in bankruptcy law. A progressive, she has focused on consumer protection, economic opportunity, and the social safety net while in the Senate. Pres. Barack Obama appointed her to a position in his administration in 2010. In 2011, she began seeking the Democratic nomination for Ted Kennedy’s former U.S. Senate seat. Learn more about her opinions '
    topic = 'warren'
    image = "static/images/warren.jpg"
    return render_template ('candidateBios.html', info = info, topic = topic, heading = heading, image = image)
    
@app.route('/trump')
def trump():
    heading = 'Donald Trump'
    info = "Donald Trump, born on June 14, 1946, is the 45th and current president of the United States. Before entering politics, he was a businessman and television personality. Trump was born and raised in the New York City borough of Queens, and received an economics degree from the Wharton School. He has portrayed himself in cameo appearances in movies and on television, including 'Zoolander,' 'Sex and the City' and 'Home Alone 2: Lost in New York.' Trump's slogan, 'Make America Great Again,' was first used by Ronald Reagan while he was running against President Jimmy Carter. Learn more about his opinions "
    topic = 'trump'
    image = "/static/images/trump.jpg"
    return render_template ('candidateBios.html', info = info, topic = topic, heading = heading, image=image)
    
@app.route('/biden')
def biden():
    heading = 'Joe Biden'
    info = 'Joseph Robinette Biden Jr.,born on November 20, 1942 in Scranton, Pennsylvania, is an American politician who served as the 47th vice president of the United States from 2009 to 2017. Biden also represented Delaware in the U.S. Senate from 1973 to 2009. A member of the Democratic Party, Biden is a candidate for president in the 2020 election. He became a lawyer in 1969 and was elected to the New Castle County Council in 1970. He was first elected to the U.S. Senate in 1972, when he became the sixth-youngest senator in American history. Learn more about his opinions '
    topic = 'biden'
    image = "/static/images/biden.jpg"
    return render_template ('candidateBios.html', info = info, topic = topic, heading = heading, image=image)
    
@app.route('/sanders')
def sanders():
    heading = 'Bernie Sanders'
    info = 'Bernard Sanders, born on September 8, 1941, is an American politician who served as the junior United States Senator from Vermont since 2007. Sanders ran unsuccessfully for the 2016 Democratic nomination for president and is running again in 2020. On domestic policy, he broadly supports labor rights, and has supported universal and single-payer healthcare, paid parental leave, and tuition-free tertiary education. On foreign policy, he broadly supports reducing military spending, pursuing more diplomacy and international cooperation, and putting greater emphasis on labor rights and environmental concerns when negotiating international trade agreements. Learn more about his opinions '
    topic = 'sanders'
    image = "/static/images/sanders.png"
    return render_template ('candidateBios.html', info = info, topic = topic, heading = heading, image=image)
    
# @app.route('/candidatebio/<topic>')
# def candidateBios():
#     return render_template('candidateBios.html')
    
@app.route('/issues')
def issues():
    return render_template('index.html')
    
@app.route('/immigration')
def immigration():
    heading = "Immigration"
    message= "With millions of people attempting to migrate to the United States every year, immgration is a controversial topic that candidates spend a lot of time debating. Use the survey underneath to determine where you stand on the matter."
    image = "/static/images/immigrationn.jpg"
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
    message = 'To what extent do you think should the society or the government invest in advancing the rights of the marginalized groups? Use the survey underneath to determine where you stand on the matter.'
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
        title = "Immigration"
        question = 'On a Scale of 1-10, how strongly do you support America being more open to immigration, legal and otherwise?'
        question2 = 'Do you think the government should forgive illegal immigrants?'
    elif topic=='abortion':
        title = 'Abortion'
        question = 'On a scale of 1-10, how strongly do you feel about abortion?'
        question2 = 'Should the government be pro-life or pro-choice?'
    elif topic=='civil_rights':
        title = 'Civil Rights'
        question = 'On a scale of 1-10, how strongly do you feel about civil rights?'
        question2 = 'Should marijuana be legalized?'
    elif topic=='lgbtq':
        title = 'LGBTQ+'
        question = 'On a scale of 1-10. how strongly do you feel about the integration of LGBTQ+ people into society?'
        question2 = 'Should the government protect the rights of and respect the gender identity of transgender people?'
    return render_template('iSurvey.html', question = question, question2 = question2, topic=topic, title = title)
    
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
                otherResultsblurb= 'Elizabeth Warren wishes to eliminate criminal penalties for those crossing the border without papers. She also wishes to reduce immigration detention. Learn more about Senator Warrens past decisions on immigration '
            elif topic == 'abortion':
                otherResultsblurb = "Elizabeth Warren is passionate about her opinion on abortion as she believes guaranteeing abortion and other reproductive rights around the country is very important. She calls on Congress to enshrine the right to abortion in federal statute, in case Roe v. Wade is overturned and the current federal right to abortion is taken away. More information about Warren’s decisions on Abortion can be found "
            elif topic == 'lgbtq':
                otherResultsblurb = "I want to see the president evolve because I believe that is right; marriage equality is morally right,' Warren told the Washington Blade. Warren amends the Defense of Marriage Act to let states recognize same sex marriage. She defines 'marriage' to provide that an individual shall be considered married if that individual's marriage is valid in the state or country where the marriage was entered into. For more information about Warren on LGBTQ visit "
            elif topic == 'civil_rights':
                otherResultsblurb = 'To get more information about Elizabeth Warren’s opinion on Civil Rights visit '
            return render_template('otherResults.html', value = value, value1=value1, otherResultsblurb=otherResultsblurb, topic=topic)
        else:
            if topic == 'immigration':
                resultsblurb= 'President Trump wishes to secure our border by constructing a border wall and ensuring the swift removal of unlawful entrants. With his policy, he hopes to serve the national interest and protect American workers. Learn more about President Trump’s past immigration decisions'
            elif topic == 'abortion':
                resultsblurb = "Trump’s position on Abortion is 'pro-life' as he tweeted, 'As most people know, and for those who would like to know, I am strongly Pro-Life, with the three exceptions — Rape, Incest and protecting the Life of the mother — the same position taken by Ronald Reagan.' For more information about Trump’s views on Abortion go "

            elif topic == 'lgbtq':
                resultsblurb = 'To get more information about Donald Trump’s opinion on LGBTQ visit the site .'  

            elif topic == 'civil_rights':
                resultsblurb = 'To get more information about Donald Trump’s opinion on Civil Rights visit the site .'

            return render_template('results.html', value=value, value1=value1, resultsblurb=resultsblurb, topic=topic)
    
    
    
@app.route('/events/new', methods=['GET', 'POST'])    
def new_event():
    if request.method == "GET":
        return render_template('api rep.html')
    else:
        address = request.form['address']
        candidates = api_practice.api_function(address)
        #print (candidates)
        return render_template("api rep.html", candidates=candidates)
        

#api_practice.api_function(address)
        
        
    
