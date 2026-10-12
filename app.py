from flask import Flask, render_template, request

app = Flask(__name__)

ticket_availability = {
    "summer-party": 100,
    "beach-party": 80,
    "dj-night": 120,
    "halloween-night": 100,
    "joana-party": 100,
    "winter-party": 80,
    "new-years-party": 150
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/event/<event_name>")
def event(event_name):

    if event_name == "joana's-party":
        event_name = "joana-party"

    available = ticket_availability[event_name]

    return render_template(
        "event.html",
        event_name=event_name,
        available=available
    )


@app.route("/book/<event_name>")
def book(event_name):
    return render_template("book.html", event_name=event_name)


@app.route("/confirmation")
def confirmation():
    name = request.args.get("name")
    email = request.args.get("email")
    tickets = request.args.get("tickets")
    event = request.args.get("event")

    tickets = int(tickets)

    if tickets > ticket_availability[event]:
        return "Sorry, there are not enough tickets available."

    ticket_availability[event] -= tickets

    event_names = {
        "summer-party": "Summer Party",
        "beach-party": "Beach Party",
        "dj-night": "DJ Night",
        "halloween-night": "Halloween Night",
        "joana-party": "Joana's Party",
        "winter-party": "Winter Party",
        "new-years-party": "New Year's Party"
    }

    event = event_names.get(event, event)

    price_per_ticket = 15
    total_price = tickets * price_per_ticket

    return render_template(
        "confirmation.html",
        name=name,
        email=email,
        tickets=tickets,
        event=event,
        total_price=total_price
    )


@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


if __name__ == "__main__":
    app.run(debug=True)
