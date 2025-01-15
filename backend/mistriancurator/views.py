from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path

@csrf_exempt
def import_data(request):
    if request.method == 'POST' and request.FILES['gamedata']:
        response = HttpResponse("Success")
        json_file = request.FILES['gamedata']
        museuminfo = {}
        gamedata = json.load(json_file)

        for key in gamedata["t2_world_facts"]:   
            if "donated" in key: 
                itemname = " ".join(key.split("_")[2:])
                if gamedata["t2_world_facts"][key]:
                    museuminfo[itemname] = "YES"
                    response.set_cookie("".join(key.split("_")[2:]), 'YES')
                else:
                    museuminfo[itemname] = "NO"
                    response.set_cookie("".join(key.split("_")[2:]), 'NO')
        return JsonResponse(museuminfo)
    return HttpResponse("Failure")

@csrf_exempt
def percentage(request):
    if request.method == 'GET' and (request.GET.get("wing").lower() == "archeology"
                                    or request.GET.get("wing").lower() == "fish"
                                    or request.GET.get("wing").lower() == "flora"
                                    or request.GET.get("wing").lower() == "insects"):
        
        p = Path(__file__).with_name('museuminfosorted.json')
        with p.open('r') as f:
            museuminfo = json.load(f)

        total = 0
        obtained = 0
        for key in museuminfo[request.GET.get("wing").capitalize()]:
            for key2 in museuminfo[request.GET.get("wing").capitalize()][key]:
                total += 1
                if request.COOKIES.get("".join(key2.split(" ")).lower(), False):
                    obtained += 1
    return HttpResponse(obtained/total)
