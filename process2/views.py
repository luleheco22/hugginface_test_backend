import os
import requests
from rest_framework.response import Response
import pandas as pd
from rest_framework.views import APIView
import time

from dotenv import load_dotenv
load_dotenv()
 
apiUrlEmotions = "https://api-inference.huggingface.co/models/finiteautomata/beto-emotion-analysis"
apiUrlSentiment = "https://api-inference.huggingface.co/models/finiteautomata/beto-sentiment-analysis"
headers = {"Authorization": "Bearer "+os.environ.get("TOKEN")}
global_emotions = []
global_sentiments = []
global_data = []

class MyClass(APIView):
    def post(self, request):
        data = request.data
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, '../data/data.csv')
        position = len(global_data)
        df = pd.read_csv(file_path)
        selected_row = df.iloc[position]
        queryEmotions = {
            "inputs": selected_row.to_dict()['text']
        }
        querySentiments = {
            "inputs": selected_row.to_dict()['text']
        }
        resEmotions = requests.post(apiUrlEmotions, headers=headers, json=queryEmotions)
        resEmotions = resEmotions.json()
        if 'error' in resEmotions and 'warnings' in resEmotions or 'error' in resEmotions and 'estimated_time' in resEmotions:
            print('Wait 20s for net Requests Emotions')
            time.sleep(21)
            resEmotions = requests.post(apiUrlEmotions, headers=headers, json=queryEmotions)
            resEmotions = resEmotions.json()
        else:
            data = {
                "text": queryEmotions,
                "emotion": resEmotions
            }
            global_emotions.append(data)
        time.sleep(2)
        resSentiments = requests.post(apiUrlSentiment, headers=headers, json=querySentiments)
        resSentiments = resSentiments.json()
        
        if 'error' in resSentiments and 'warnings' in resSentiments or 'error' in resSentiments and 'estimated_time' in resSentiments:
            print('Wait 20s for net Requests Sentiments')
            time.sleep(21)
            resSentiments = requests.post(apiUrlSentiment, headers=headers, json=querySentiments)
            resSentiments = resSentiments.json()
        else:
            data = {
                "text": querySentiments,
                "sentiment": resSentiments
            }
            global_sentiments.append(data)
        newData = {
            "position": position,
            "text": queryEmotions,
            "emotion": resEmotions,
            "sentiment": resSentiments
        }
        global_data.append(newData)
        newPosition = str(position+1) + '/' + str(len(df))
        return Response({'status':newPosition, "data": global_data})

    def get(self, request):
        return Response({'status': 'GET'})
