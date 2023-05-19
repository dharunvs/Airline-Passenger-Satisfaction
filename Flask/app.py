from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open("./Airline Passengers.pkl", "rb"))

app = Flask(__name__)

@app.route('/pred', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        Gender = request.form[ "Gender"]
        if Gender == "Female":
            Gender = 0
        if Gender == "Male":
            Gender = 1
        Age = request.form['Age']
        Type_of_Travel = request.form['Type of Travel']
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
        Flight_Distance = request.form['Flight Distance']
        Inflight_wifi_service = request.form['Inflight wifi service']
        Departure_Arrival_time_convenient = request.form['Departure/Arrival time convenient']
        Ease_of_Online_booking = request.form['Ease of Online booking']
        Gate_location = request.form['Gate Location']
        Food_and_drink = request.form['Food and drink']
        Online_boarding = request.form['Online boarding'] 
        Seat_comfort = request.form[ "Seat comfort"]
        Inflight_entertainment = request.form['Inflight entertainment']
        On_board_service = request.form['On-board service']
        Leg_room_service = request.form['Leg room service']
        Baggage_handling = request.form['Baggage handling']
        Checkin_service = request.form['Checkin service']
        Inflight_service = request.form['Inflight service']
        Cleanliness = request.form['Cleanliness']
        Departure_Delay_in_Minutes = request.form['Departure Delay in Minutes']
        Arrival_Delay_in_Minutes = request.form['Arrival Delay in Minutes']

        total = [[Gender, Age, Type_of_Travel, Class, Flight_Distance, Inflight_wifi_service, Departure_Arrival_time_convenient, Ease_of_Online_booking, Gate_location, Food_and_drink, Online_boarding, Seat_comfort, Inflight_entertainment, On_board_service, Leg_room_service, Baggage_handling, Checkin_service, Inflight_service, Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes]]
        print(total)
        payload_scoring = {"input_data": [{"field": ["Gender", "Age", "Type_of_Travel", "Class", "Flight_Distance", "Inflight_wifi_service", "Departure_Arrival_time_convenient", "Ease_of_Online_booking", "Gate_location", "Food_and_drink", "Online_boarding", "Seat_comfort", "Inflight_entertainment", "On_board_service", "Leg_room_service", "Baggage_handling", "Checkin_service", "Inflight_service", "Cleanliness", "Departure_Delay_in_Minutes", "Arrival_Delay_in_Minutes"]}] }
        
        print("Scoring response")
        prediction = model.predict(total)
        print(prediction)
        pred  = prediction["predictions"][0]['values'][0][0]
        print(pred)
        print(pred)
        if int(pred) == 0:
            pred = "Passengers have satisfies the Airline Service"
        else:
            pred = "Passengers have neutral or dissatisfied the Airline Service"
        print("hello", pred)
        return render_template('prediction.html', prediction_text=pred)


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    print(__name__)
    app.run(debug=True)