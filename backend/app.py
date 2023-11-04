from flask import Flask, request, jsonify
import google.generativeai as palm
API_KEY = 'AIzaSyDmZnz_tzgyL6GotLqDdSsKYWymhn0c1v4'

palm.configure(api_key=API_KEY)
    
#response = palm.chat(messages='Hello')
#response.last
#response = response.reply("Just chillin'")
#print(response.last)


app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"

# test data
vehicle_status ={
    'id':1,
    'make':'Toyota',
    'model':'Supra',
    'year': '2023',
    'status':'parking'
}
@app.route('/car/status', methods =['GET', 'POST'])

def vehicle_status():
    if request.method =='GET':
        return jsonify(vehicle_status)
    elif request.method == 'POST':
        data = request.get_json()
        if 'status' in data:
            car_status['status'] = data['status']
            return jsonify({'message': 'Car status updated successfully'})
        else:
            return jsonify({'error': 'Status field is required in the request data'}), 400

if __name__ == "__main__":
    app.run(debug=True)

