from server import past_date
import server as app

GOOD_CLUB ={"name": "Simply Lift",
           "email":"john@simplylift.co",
           "points":"13"}

GOOD_COMPETITION = {"name": "Spring Festival",
                    "date": "2022-03-27 10:00:00",
                    "numberOfPlaces": "25",
                    "past":False}

GOOD_EMAIL = "john@simplylift.co"
WRONG_EMAIL = "wrong@email.com"
WRONG_NAME = "wrong name"
GOOD_CLUB_NAME = "Simply Lift"
GOOD_COMPETITION_NAME = "Spring Festival"


def test_past_competition():
    date = "1900-10-22 13:30:00"
    response = app.past_date(date)
    assert response == True


def test_bookable_competition():
    date = "3000-10-22 13:30:00"
    response = app.past_date(date)
    assert response == False


def test_find_user_with_wrong_email():
    response = app.find_user_with_email(app.clubs, WRONG_EMAIL)
    assert response == "404error"


def test_find_user_with_good_email():
    response = app.find_user_with_email(app.clubs, GOOD_EMAIL)
    assert response == GOOD_CLUB


def test_find_user_with_wrong_name():
    response = app.find_user_with_name(app.clubs, WRONG_NAME)
    assert response == "404error"


def test_find_user_with_good_name():
    response = app.find_user_with_name(app.clubs, GOOD_CLUB_NAME)
    assert response == GOOD_CLUB

def test_find_competition_with_wrong_name():
    response = app.find_competition_with_name(app.clubs, WRONG_NAME)
    assert response == "404error"


def test_find_competition_with_good_name():
    response = app.find_competition_with_name(app.competitions, GOOD_COMPETITION_NAME)
    assert response == GOOD_COMPETITION

def test_booking_works_well():
    response = app.booking(GOOD_CLUB, GOOD_COMPETITION, 2)
    assert response["message"] == "Great-booking complete!, you've book 2 places"
    assert response["competition"] == GOOD_COMPETITION
    assert response["club"]["points"] == 7

def test_booking_not_enough_points():
    response = app.booking(GOOD_CLUB, GOOD_COMPETITION, 10)
    assert response["message"] == "You don't have enough points"
    assert response["competition"] == GOOD_COMPETITION
    assert response["club"] == GOOD_CLUB

def test_booking_more_than_12_places():
    response = app.booking(GOOD_CLUB, GOOD_COMPETITION, 1000)
    assert response["message"] == "You can't book than 12 places"
    assert response["competition"] == GOOD_COMPETITION
    assert response["club"] == GOOD_CLUB

def test_booking_places_is_not_an_integer():
    response = app.booking(GOOD_CLUB, GOOD_COMPETITION, "a")
    assert response["message"] == "Something went wrong"
    assert response["competition"] == GOOD_COMPETITION
    assert response["club"] == GOOD_CLUB