import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime


def past_date(date):
    dateformatter = "%Y-%m-%d %H:%M:%S"
    competition_date = datetime.strptime(date, dateformatter)
    today = datetime.now()
    if today > competition_date:
        return True
    else:
        return False


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        for competition in listOfCompetitions:
            competition["past"]=past_date(competition["date"])
        return listOfCompetitions


def find_user_with_email(club_database,email):
    for club in club_database:
        if club["email"] == email:
            return club
    return "404error"

def find_user_with_name(club_database,name):
    for club in club_database:
        if club["name"] == name:
            return club
    return "404error"

def find_competition_with_name(competition_database,name):
    for competitition in competition_database:
        if competitition["name"] == name:
            return competitition
    return "404error"

def booking(club, competition, place):
    reponses = {"club":club,
                "competition": competition,
                "message": ""}
    try:
        place_int = int(place)
        deductpoint = place_int * 3
        if place_int <= 12:
            if deductpoint <= int(club['points']):
                reponses["competition"]['numberOfPlaces'] = int(competition['numberOfPlaces']) - place_int
                reponses["club"]["points"] = int(club["points"]) - deductpoint
                reponses["message"] = f"Great-booking complete!, you've book {place_int} places"
            else:
                reponses["message"] = "You don't have enough points"
        else:
            reponses["message"] =  "You can't book than 12 places"
    except ValueError:
        reponses["message"] = "Something went wrong"
    return reponses


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary',methods=['POST'])
def showSummary():
    user = find_user_with_email(clubs,request.form["email"])
    if not user == "404error":
        return render_template('welcome.html', club=user, competitions=competitions)
    else:
        flash("Sorry, that email wasn't found.")
        return render_template('index.html')



@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = find_user_with_name(clubs,club)
    foundCompetition = find_competition_with_name(competitions,competition)
    if not (foundClub and foundCompetition) == "404error":
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    club = find_user_with_name(clubs,request.form["club"])
    competition = find_competition_with_name(competitions,request.form["competition"])
    if not (club and competition) == "404error":
        booking_response = booking(place=request.form['places'], club=club, competition=competition)
        flash(booking_response["message"])
        return render_template('welcome.html', club=booking_response["club"], competitions=competitions)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route("/board")
def displayboard():
    return render_template("displayboard.html", clubs=loadClubs())

@app.route('/logout')
def logout():
    return redirect(url_for('index'))