from flask import Flask, render_template, request


# import json to load JSON data to a python dictionary

import json
import requests
  

app = Flask(__name__)



@app.route('/', methods =['POST', 'GET'])

def weather():

    if request.method == 'POST':

        city = request.form['city']

    else:

        # for default name mathura

        city = 'chennai'
    # your API key will come here

    api = "b9806932f470507d678f17919a8c1445"
    try:
      response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api)
    except:
      return abort(404)
    # converting JSON data to a dictionary

    list_of_data = json.loads(response.text)

    print(list_of_data)

    # data for variable list_of_data

    data = {
        "cityname":str(city),

        "country_code": str(list_of_data['sys']['country']),

        "coordinate": str(list_of_data['coord']['lon']) + ' ' 

                    + str(list_of_data['coord']['lat']),

        "temp": str(list_of_data['main']['temp']) + 'k',

        "pressure": str(list_of_data['main']['pressure']),

        "humidity": str(list_of_data['main']['humidity']),

    }

    print(data)

    return render_template('index.html', data = data)

  

  

  

if __name__ == '__main__':

    app.run(debug = True)
