from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.String(50), nullable=False)
    passenger = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(100), nullable=False)

@app.route('/rides', methods=['GET', 'POST'])
def manage_rides():
    if request.method == 'GET':
        rides = Ride.query.all()
        return jsonify([{'driver': ride.driver, 'passenger': ride.passenger, 'destination': ride.destination} for ride in rides])
    elif request.method == 'POST':
        data = request.json
        new_ride = Ride(driver=data['driver'], passenger=data['passenger'], destination=data['destination'])
        db.session.add(new_ride)
        db.session.commit()
        return jsonify({'message': 'Ride added'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
