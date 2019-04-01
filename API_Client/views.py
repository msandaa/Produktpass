

from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
import requests


# Create your views here.

def produktpass_search(request):

#Notiz: To-Do Validation
#Notiz: Struktur des Produktpasses-Json Links und Massnahmenname macht wahrscheinlich mehr sinn, statt nur Links
#Notiz: Wie kann man sich extra Massnahmen anzeigen lassen?
        #ggf: ExelTabllen anschauen!

    if request.method == 'GET':

        id = request.GET.get('produktpass_search', '')

        if id == '':
            return render(request, 'API_Client/search_form.html', {})

        else:

#What happens when there isnt a PP with this ID??

            urlstr_redirect = '/produktpass/' + id
            return redirect(urlstr_redirect)


def produktpass_show(request, id):

    urlstr = 'http://127.0.0.1:8000/produktpass/' + id
    response = requests.get(urlstr)
    produktpass = response.json()

    return render(request, 'API_Client/produktpass_show.html', produktpass)

def massnahmen_show(request, id):

    url_filter = '/?produktpass=' + id
    url = 'http://127.0.0.1:8000/massnahmen' + url_filter
    response = requests.get(url)
    massnahmen = response.json()
    print(massnahmen)

    return render(request, 'API_Client/massnahmen_show.html',{'massnahmen' : massnahmen})
