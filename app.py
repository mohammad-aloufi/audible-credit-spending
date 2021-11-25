from flask import Flask, render_template, request
import joblib


app = Flask(__name__)

# Load our model
model = joblib.load('model.pkl')


@app.route('/result')
def result():
    #Get the values from the args and convert them to floats.
    price = float(request.args.get('book_price'))
    hours = float(request.args.get('book_hour_length'))
    minutes = float(request.args.get('book_minute_length'))
    #We'll combine the hours and minutes values into one called duration.
    duration = ((hours*60+minutes)/60)
    #We do the prediction
    prediction = model.predict([[price, duration]])
    if prediction[0] == 0:
        print(duration)
        return "It's probably better if you buy this book with cash and save the credit for another book"
    else:
        return "It's probably better if you just spend the credit on this book"


@app.route('/')
def index():
    #Append numbers from 0 to 59 to a list to send to the html template
    numbers_for_boxes = []
    for i in range(60):
        numbers_for_boxes.append(i)
    return render_template('index.html', hours=numbers_for_boxes, minutes=numbers_for_boxes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
