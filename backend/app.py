from flask import Flask, request, jsonify
import google.generativeai as palm
import random
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from TTS import make_sound
from STT import transcribe_file
from models import PosModel
from datetime import datetime
import uuid

API_KEY = 'AIzaSyDmZnz_tzgyL6GotLqDdSsKYWymhn0c1v4'
palm.configure(api_key=API_KEY)

uri = "mongodb+srv://admin:0oaDZ3moDIHYHQbK@cluster0.cquhhbc.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))    
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client['car_positions_db']
car_positions_collection = db['car_positions'] 



# Sample data
car_position_data = {
    "_id": str( uuid.uuid4()),  # Unique identifier for the car
    'pos': {             # Position as a subdocument
        'lat': 32.9751675,  # Latitude
        'lon': -96.7601161  # Longitude
    },
    'prev_quote':"",  # Previous quote in dollars
    'datetime': datetime.now(),  # Current datetime in UTC
    'Running': True,  # Current status of the car
    'AC':79,
    
}

sampleData = PosModel(32.9751675,-96.7601161,79, True, "", 200)

try:
    # Insert the document into the collection
    result = car_positions_collection.insert_one(sampleData.getData())
    print(f"Inserted document with id: {result.inserted_id}")
except Exception as e:
    
    print(f"An error occurred: {e}")
app = Flask(__name__)

#listen from user and send back reply using Bard AI
@app.route('/listen', methods=['GET'])
def listen():
    #print( transcribe_file("./static/Recording.mp3"))
    reply = palm.chat(context="Speak like a toyota assistant", messages = transcribe_file("./static/weather.mp3"))
    response = make_sound(reply.last)
    return jsonify(response)


@app.route('/')
def index():
    return "Vehicle testing supreme"

@app.route('/car/status', methods =['GET'])
#check for vehicle current status
def vehicle_status():
    if request.method =='GET':
        if car_position_data['status']:
            return "The car is currently running"
        else:
            return "Turning car on"
        
if __name__ == "__main__":
    app.run(debug=True)

