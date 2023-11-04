from flask import Flask
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
if __name__ == "__main__":
    app.run(debug=False)

