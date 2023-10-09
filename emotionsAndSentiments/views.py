# from django.shortcuts import render

# Create your views here.
import requests
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dotenv import load_dotenv
load_dotenv()
 

apiUrlEmotions = "https://api-inference.huggingface.co/models/finiteautomata/beto-emotion-analysis"
apiUrlSentiment = "https://api-inference.huggingface.co/models/finiteautomata/beto-sentiment-analysis"
headers = {"Authorization": "Bearer "+os.environ.get("TOKEN")}


@api_view(['GET','POST'])
def getDataEmotions(request):
    if request.method == 'GET':
        return Response('hello emotions')
    elif request.method == 'POST':
        print('post emotions')
        query = request.data
        return emotions(query)
    
@api_view(['GET', 'POST'])
def getDataSentiment(request):
    if request.method == 'GET':
        print('hola bandera get sentiments')
        return Response('hey this its Get Sentiments')
    elif request.method == 'POST':
        print('post sentiments')
        query = request.data
        return sentiment(query)

def emotions(query):
    print(query)
    response = requests.post(apiUrlEmotions, headers=headers, json=query)
    return Response(data=response.json(), status=response.status_code)

def sentiment(query):
    print('find sentiments')
    response = requests.post(apiUrlSentiment, headers=headers, json=query)
    return Response(data = response.json(), status = response.status_code)