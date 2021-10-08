from server import past_date
import server as app
import pytest

@pytest.fixture()
def good_club():
    return {"name": "Simply Lift",
           "email":"john@simplylift.co",
           "points":"13"}

@pytest.fixture()
def good_competition():
    return {"name": "Spring Festival",
                    "date": "2022-03-27 10:00:00",
                    "numberOfPlaces": "25",
                    "past":False}
@pytest.fixture()
def good_email():
    return "john@simplylift.co"

@pytest.fixture()
def wrong_email():
    return "wrong@email.com"

@pytest.fixture()
def wrong_name():
    return "wrong name"

@pytest.fixture()
def good_club_name():
    return "Simply Lift"

@pytest.fixture()
def good_competition_name():
    return "Spring Festival"


def test_past_competition():
    date = "1900-10-22 13:30:00"
    response = app.past_date(date)
    assert response == True


def test_bookable_competition():
    date = "3000-10-22 13:30:00"
    response = app.past_date(date)
    assert response == False


def test_find_user_with_wrong_email(wrong_email):
    """

    :param wrong_email: fixture wrong email email
    :return:
    """
    response = app.find_user_with_email(app.clubs, wrong_email)
    assert response is None


def test_find_user_with_good_email(good_email,good_club):
    response = app.find_user_with_email(app.clubs, good_email)
    assert response == good_club


def test_find_user_with_wrong_name(wrong_name):
    response = app.find_user_with_name(app.clubs, wrong_name)
    assert response is None


def test_find_user_with_good_name(good_club_name,good_club ):
    response = app.find_user_with_name(app.clubs, good_club_name)
    assert response == good_club

def test_find_competition_with_wrong_name(wrong_name):
    response = app.find_competition_with_name(app.clubs, wrong_name)
    assert response is None


def test_find_competition_with_good_name(good_competition, good_competition_name):
    response = app.find_competition_with_name(app.competitions, good_competition_name)
    assert response == good_competition

def test_booking_works_well(good_club,good_competition):
    response = app.booking(good_club, good_competition, 2)
    assert response["message"] == "Great-booking complete!, you've book 2 places"
    assert response["competition"] == good_competition
    assert response["club"]["points"] == 7

def test_booking_not_enough_points(good_club, good_competition):
    response = app.booking(good_club, good_competition, 10)
    assert response["message"] == "You don't have enough points"
    assert response["competition"] == good_competition
    assert response["club"] == good_club

def test_booking_more_than_12_places(good_club, good_competition):
    response = app.booking(good_club, good_competition, 1000)
    assert response["message"] == "You can't book than 12 places"
    assert response["competition"] == good_competition
    assert response["club"] == good_club

def test_booking_places_is_not_an_integer(good_club, good_competition):
    response = app.booking(good_club, good_competition, "a")
    assert response["message"] == "Something went wrong"
    assert response["competition"] == good_competition
    assert response["club"] == good_club