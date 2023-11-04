from flask import Flask, request, jsonify
import google.generativeai as palm
import random
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
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

app = Flask(__name__)

#listen from user and send back reply using Bard AI
@app.route('/listen', methods=['GET'])
def listen():
    #print(request.json["messages"])
    #return "Bye world"
    reply = palm.chat(context="Speak like a toyota assistant", messages = request.json["messages"])
    return jsonify(reply.last)

@app.route('/')
def index():
    return "Vehicle testing supreme"

# test data
vehicle_description = {
    'make':'Toyota',
    'model':'Supra',
    'year': '2023',
    'status': True
}
@app.route('/car/status', methods =['GET'])
#check for vehicle current status
def vehicle_status():
    if request.method =='GET':
        if vehicle_description['status']:
            return "The car is currently ON"
        else:
            return "Turning car on"
        
if __name__ == "__main__":
    app.run(debug=True)

