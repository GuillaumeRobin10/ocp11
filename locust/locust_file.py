from locust import HttpUser, task, between
from random import randint

COMPETITION = "Spring Festival",

CLUB = "Simply Lift"
# amélio randint




class User(HttpUser):
    wait_time = between(1, 2.5)

    @task(10)
    def index(self):
        """Declared a task with the index method with a higher weight (10)."""
        self.client.get("/")

    @task(3)
    def logout(self):
        """Declared a task with the logout method with a higher weight (3)."""
        self.client.get("/logout")

    @task(1)
    def show_clubs(self):
        """Declared a task with the show_clubs method with a higher weight (1)."""
        self.client.get("/board")

    @task(8)
    def login(self):
        """Declared a task with the show_summary method with a higher weight (8)."""
        email_address = "john@simplylift.co"
        #faire un adresse en erreur
        self.client.post("/showSummary", {"email": email_address})

    @task(3)
    def purchase_places(self):
        """Declared a task with the purchase_places method with a higher weight (3)."""
        places = randint(1, 50)
        self.client.post(
            "/purchasePlaces",
            {"competition": competition, "club": CLUB, "places": COMPETITION},
        )

    @task(6)
    def book(self):
        """Declared a task with the book method with a higher weight (6)."""
        self.client.get(f"/book/{COMPETITION}/{CLUB}")
