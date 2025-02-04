from django.shortcuts import render
import urllib.request
import json
from urllib.error import HTTPError, URLError

def index(request):
    data = {}
    api_key = 'c55b9abe4b1a1c77ca5289c0d1101131'

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            data = fetch_weather_data(url)
            return render(request, "main/index.html", data)
        else:
            return render(request, "main/index.html", {"error": "Please enter a city name."})

    elif request.method == 'GET' and request.GET.get('lat') and request.GET.get('lon'):
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
        data = fetch_weather_data(url)
        return render(request, "main/index.html", data)

    return render(request, "main/index.html", data)

def fetch_weather_data(url):
    try:
        source = urllib.request.urlopen(url).read()
        list_of_data = json.loads(source)

        if list_of_data.get("cod") != 200:
            error_message = list_of_data.get("message", "Unknown error")
            return {"error": f"API Error: {error_message}"}

        return {
            "country_code": list_of_data['sys']['country'],
            "coordinate": f"{list_of_data['coord']['lon']}, {list_of_data['coord']['lat']}",
            "temp": list_of_data['main']['temp'],
            "pressure": list_of_data['main']['pressure'],
            "humidity": list_of_data['main']['humidity'],
            "main": list_of_data['weather'][0]['main'],
            "description": list_of_data['weather'][0]['description'],
            "icon": list_of_data['weather'][0]['icon'],
        }

    except HTTPError as e:
        return {"error": f"HTTP Error: {e.code} - {e.reason}"}
    except URLError as e:
        return {"error": f"Network Error: {e.reason}"}
    except Exception as e:
        return {"error": f"Unexpected Error: {str(e)}"}
