

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


def nutzflaechenmassnahmen_show(request, agrarProID):

    #Es wird die ID der Nutzfläche benötigt um die dazugehörigen Nutzflächenmaßnahmen anzufragen
    #So wird erst die Nutzfläche angefragt
    url_filter_Nutzfl = '/?agrarprodukt=' + agrarProID
    urlNutz = 'http://PPREST.pythonanywhere.com/nutzflaechen' + url_filter_Nutzfl
    #urlNutz = 'http://127.0.0.1:8000/nutzflaechen' + url_filter_Nutzfl
    response = requests.get(urlNutz)
    nutzflaeche = response.json()['results'][0]
    nutzid = str(nutzflaeche['id'])

    #Und mit der NutzflächenID werden die dazugehörigen Maßnahmen angefragt
    url_filter_NuMass = '/?ausgeführt_auf_nutzflaeche=' + nutzid
    urlstr = 'http://PPREST.pythonanywhere.com/nutzflaechenmassnahmen' + url_filter_NuMass
    #urlstr = 'http://127.0.0.1:8000/nutzflaechenmassnahmen' + url_filter_NuMass
    response = requests.get(urlstr)
    #print(urlstr)
    nutzflaechenmassnahmen = response.json()['results']

    return render(request, 'API_Client/massnahmen_show.html', { 'nutzflaechenmassnahmen' : nutzflaechenmassnahmen })



def produktpass_show(request, agrarProID):

    #Ressource Agrarprodukt wird angefragt
    urlstrAgrarPro = 'http://PPREST.pythonanywhere.com/agrarprodukte/' + agrarProID
    #urlstrAgrarPro = 'http://127.0.0.1:8000/agrarprodukte/' + agrarProID
    response = requests.get(urlstrAgrarPro)
    #print(response.json())
    agrarprodukt = response.json()

    #Ressource nutzfläche wird angefragt
    url_filter_Nutzfl = '/?agrarprodukt=' + agrarProID
    urlNutz = 'http://PPREST.pythonanywhere.com/nutzflaechen' + url_filter_Nutzfl
    #urlNutz = 'http://127.0.0.1:8000/nutzflaechen' + url_filter_Nutzfl
    response = requests.get(urlNutz)
    print(response.json()['results'][0])
    nutzflaeche = response.json()['results'][0]


    return render(request, 'API_Client/agrarprodukt_show.html',{'agpro' : agrarprodukt ,'nuzfla' : nutzflaeche})
