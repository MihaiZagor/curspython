from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'https://api.waqi.info/feed/{}/?token=862501b61e60df4698fb3c1a11bbb08c3d97071c'


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    air_data =[]

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_air = {
            'cityname': city.name,
            'air_quality':r['data']['aqi'],
        }

        air_data.append(city_air)

    def air_level():
        for i in [city_air.get('air_quality')]:
            if i>=0 and i<=50:
                a = print(f'Air pollution level: Good')
            elif i>=51 and i<=100:
                a = print(f'Air pollution level:Moderate')
            elif i>=101 and i<=150:
                a = print(f'Air pollution level:Unhealthy for sensitive groups')
            elif i>=151 and i<=200:
                a = print(f'Air pollution level:Unhealthy')
            elif i>=201 and i<=300:
                a = print(f'Air pollution level: Very unhealthy')
            elif i>=300:
                a = print(f'Air pollution level:Hazardous')
        return a

    airlvl = {'lvl':air_level()}
    context = {'air_data' : air_data, 'form' : form}

    print(city_air)

    return render(request, 'air/air.html', context)