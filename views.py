from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template.context_processors import csrf
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CH.forms import RequestForm
import pprint
# Create your views here.
@csrf_exempt
def main(request):
    def get_clickhouse_data(query, host, connection_timeout=1500):
        """Метод для обращения к базе данных CH"""
        r = requests.post(host, params={'query': query}, timeout=connection_timeout)
        return r.text
    if request.method=="POST":
        city=json.loads(request.body.decode('utf-8'))['city']
        q=""" SELECT KOD,ADDRESS,NAIM,NAIM_FULL,COMMENT  FROM test_fns.test WHERE match(ADDRESS,'{city}') FORMAT JSON
        """.format(city=city)
        resp=json.loads(get_clickhouse_data(q, 'http://85.143.172.199:8123'))['data']
        pprint.pprint(resp)
        return JsonResponse(resp, safe=False)