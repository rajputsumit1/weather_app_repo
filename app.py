from flask import Flask,request,jsonify,render_template
import requests

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('weather.html')

@app.route('/get_weather',methods =['POST'])
def take_input():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    para = {'q' : request.form['city'],
    'units' : request.form['units'],
    'appid' : request.form.get('appid')
   }

    data = requests.get(url,params=para).json()
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
