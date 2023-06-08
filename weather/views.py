from django.shortcuts import render
import requests

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '204398eb7b6ccc74608a64b67e589304'  # Replace with your actual API key

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather = data.get('weather', [])
            if weather:
                description = weather[0].get('description')
            
            main = data.get('main', {})
            temperature = main.get('temp')
            if temperature is not None:
                temperature_celsius = temperature - 273.15
                temperature_celsius = round(temperature_celsius, 2)
                temp = str(temperature_celsius) + "°C"
            
            humidity = str(main.get('humidity')) + "%"

            context = {
                'city': city,
                'temperature': temp if 'temperature_celsius' in locals() else None,
                'description': description if 'description' in locals() else None,
                'humidity': humidity if 'humidity' in locals() else None
            }

            return render(request, 'weather/index.html', context)

    return render(request, 'weather/index.html')
