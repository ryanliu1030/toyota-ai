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

uri = "mongodb+srv://xinruiliu1030:rDO3Dqd14ouGeHRU@cluster0.ihd1grf.mongodb.net/?retryWrites=true&w=majority"

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


# sampleData = PosModel(32.9751675,-96.7601161,79, True, "", 200, 50)

# try:
#     # Insert the document into the collection
#     result = car_positions_collection.insert_one(sampleData.getData())
#     print(f"Inserted document with id: {result.inserted_id}")
# except Exception as e:
    
#     print(f"An error occurred: {e}")
app = Flask(__name__)

#listen from user and send back reply using Bard AI
@app.route('/listen', methods=['GET'])
def listen():
    last_pos = get_latest_car_position()
    context = "You are a in-cabin Toyota virtual assistant, your current position is at longitude " + str(last_pos['pos']['lon']) + ", and latitude "\
                + str(last_pos['pos']['lat']) + " , the current ac is at " + str(last_pos['AC']) + ", the car range is sitting at " + str(last_pos["range"]) \
                + " miles, the car is running at " + str(last_pos['MPH']) + " miles per hour. The vehicle is currently on" + str(last_pos['Mileage']) + " miles. \
                    Do not include * in the text. Keep the response under 20 seconds as if a person reads it out loud."
    reply = palm.chat(context=context, messages = transcribe_file("backend/static/Recording.mp3"))
    response = make_sound(reply.last)
    return jsonify(response)

def get_latest_car_position():
    try:
        latest_position = car_positions_collection.find().sort('datetime', -1).limit(1)
        return latest_position[0] 
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/status', methods =['POST'])
#check for vehicle current status
def vehicle_status():
    if request.method =='GET':
        if car_position_data['status']:
            return "The car is currently running"
        else:
            return "Turning car on"
        
if __name__ == "__main__":
    app.run(debug=True)

