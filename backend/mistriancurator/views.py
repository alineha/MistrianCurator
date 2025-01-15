from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
from django.conf import settings

@csrf_exempt
def import_data(request):
    if request.method == 'POST' and request.FILES['gamedata']:
        json_file = request.FILES['gamedata']
        museuminfo = {}
        gamedata = json.load(json_file)

        for key in gamedata["t2_world_facts"]:   
            if "donated" in key: 
                itemname = " ".join(key.split("_")[2:])
                if gamedata["t2_world_facts"][key]:
                    museuminfo[itemname] = "YES"
                else:
                    museuminfo[itemname] = "NO"
        return JsonResponse(museuminfo)
    return HttpResponse("Failure")

@csrf_exempt
def percentage(request):
    total = 0
    obtained = 0
    if request.method == 'POST' and (request.GET.get("wing", "").lower() == "archeology"
                                    or request.GET.get("wing", "").lower() == "fish"
                                    or request.GET.get("wing", "").lower() == "flora"
                                    or request.GET.get("wing", "").lower() == "insects"):
        p = Path(__file__).with_name('museuminfosorted.json')
        with p.open('r') as f:
            museuminfosorted = json.load(f)
        jsoninfo = request.body.decode('utf-8')
        museuminfo = json.loads(jsoninfo)

        for key in museuminfosorted[request.GET.get("wing").capitalize()]:
            print(key)
            for key2 in museuminfosorted[request.GET.get("wing").capitalize()][key]:
                total += 1
                print(key2)
                if key2.lower() in museuminfo.keys() and museuminfo[key2.lower()] == "YES":
                    print("AAAAAAAAAAAAAAAAA")
                    obtained += 1
    return HttpResponse(obtained/total if total>0 else 0)
