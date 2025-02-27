from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
from django.conf import settings
import re

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
        if (museuminfo == None):
            return HttpResponse(400)

        for key in museuminfosorted[request.GET.get("wing").capitalize()]:
            for key2 in museuminfosorted[request.GET.get("wing").capitalize()][key]:
                total += 1
                if key2.lower() in museuminfo.keys() and museuminfo[key2.lower()] == "YES":
                    obtained += 1
    return HttpResponse(round(obtained/total, 2) if total>0 else 0)

@csrf_exempt
def bundles(request):
    if request.method == 'GET' and (request.GET.get("wing", "").lower() == "archeology"
                                    or request.GET.get("wing", "").lower() == "fish"
                                    or request.GET.get("wing", "").lower() == "flora"
                                    or request.GET.get("wing", "").lower() == "insects"):
        p = Path(__file__).with_name('museuminfosorted.json')
        with p.open('r') as f:
            museuminfosorted = json.load(f)
        return JsonResponse(list(museuminfosorted[request.GET.get("wing").capitalize()].keys()), safe=False)
    return HttpResponse(400)
    
def capitalizeChars(s):
    ls = len(s)
    lc = -1
    
    sr = ''
    for i in range(0, ls):
        if lc == -1 or (not lc.isalpha() and s[i].isalpha()):
            sr += s[i].upper()
        else:
            sr += s[i]
        lc  = sr[i]
            
    return sr

@csrf_exempt
def bundleItems(request):
    if request.method == 'GET' and (request.GET.get("wing", "").lower() == "archeology"
                                    or request.GET.get("wing", "").lower() == "fish"
                                    or request.GET.get("wing", "").lower() == "flora"
                                    or request.GET.get("wing", "").lower() == "insects"):
        p = Path(__file__).with_name('museuminfosorted.json')
        with p.open('r') as f:
            museuminfosorted = json.load(f)        

        bundle = capitalizeChars(request.GET.get("bundle",""))
        if bundle in list(museuminfosorted[request.GET.get("wing").capitalize()].keys()):
            return JsonResponse(list(museuminfosorted[request.GET.get("wing").capitalize()][bundle]), safe=False)
    return HttpResponse(400)