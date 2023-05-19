from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open("./Airline Passengers.pkl", "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        Gender = request.form[ "Gender"]
        if Gender == "Female":
            Gender = 0
        if Gender == "Male":
            Gender = 1
        CustomerType = "0"
        Age = request.form['Age']
        Type_of_Travel = request.form['Type_of_Travel']
        if Type_of_Travel == 'Business travel':
            Type_of_Travel = 0
        if Type_of_Travel == "Personal Travel":
            Type_of_Travel = 1
        Class = request.form['Class']
        if Class == "Business":
            Class = 0
        if Class == "Eco":
            Class = 1
        if Class == "Eco Plus":
            Class = 2
        Flight_Distance = request.form["Flight_Distance"]
        Inflight_wifi_service = request.form["Inflight_wifi_service"]
        Departure_Arrival_time_convenient = request.form["Departure_Arrival_time_convenient"]
        Ease_of_Online_booking = request.form["Ease_of_Online_booking"]
        Gate_location = request.form["Gate_location"]
        Food_and_drink = request.form["Food_and_drink"]
        Online_boarding = request.form["Online_boarding"]
        Seat_comfort = request.form["Seat_comfort"]
        Inflight_entertainment = request.form["Inflight_entertainment"]
        On_board_service = request.form["On_board_service"]
        Leg_room_service = request.form["Leg_room_service"]
        Baggage_handling = request.form["Baggage_handling"]
        Checkin_service = request.form["Checkin_service"]
        Inflight_service = request.form["Inflight_service"]
        Cleanliness = request.form["Cleanliness"]
        Departure_Delay_in_Minutes = request.form["Departure_Delay_in_Minutes"]
        Arrival_Delay_in_Minutes = request.form["Arrival_Delay_in_Minutes"]

        total = [[Gender, CustomerType, Age, Type_of_Travel, Class, Flight_Distance, Inflight_wifi_service, Departure_Arrival_time_convenient, Ease_of_Online_booking, Gate_location, Food_and_drink, Online_boarding, Seat_comfort, Inflight_entertainment, On_board_service, Leg_room_service, Baggage_handling, Checkin_service, Inflight_service, Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes]]
        print(len(total[0]))
        payload_scoring = {"input_data": [{"field": ["Gender", "CustomerType", "Age", "Type_of_Travel", "Class", "Flight_Distance", "Inflight_wifi_service", "Departure_Arrival_time_convenient", "Ease_of_Online_booking", "Gate_location", "Food_and_drink", "Online_boarding", "Seat_comfort", "Inflight_entertainment", "On_board_service", "Leg_room_service", "Baggage_handling", "Checkin_service", "Inflight_service", "Cleanliness", "Departure_Delay_in_Minutes", "Arrival_Delay_in_Minutes"]}] }
        
        print("Scoring response")
        prediction = model.predict(total)
        print(prediction)
        pred  = prediction[0]
        print(pred)
        print(pred)
        if int(pred) == 0:
            pred = "Passengers have satisfies the Airline Service"
        else:
            pred = "Passengers have neutral or dissatisfied the Airline Service"
        print("hello", pred)
        return render_template('predict.html', prediction_text=pred)
    else:
        print("GET method")
        return render_template('predict.html', prediction_text="GET")


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    print(__name__)
    app.run(debug=True)