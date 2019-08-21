from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . webhook_challenge import webhook_challenge
from . scullery import *
import json

class webhook(APIView):
    def get(self,request):
        crc_token = request.GET.get('crc_token')
        if (crc_token == None or len(crc_token) == 0):
            return JsonResponse({'message':'Please provide a crc token'},status=400)
        else:
            return JsonResponse(webhook_challenge(crc_token))
    
    def post(self,request):
        activity = list(json.loads(request.body).keys())[1]
        print('activity received : '+activity)
        if(activity=='tweet_create_events'):
            mention=json.loads(request.body)['tweet_create_events'][0]['text']
            mentionId=json.loads(request.body)['tweet_create_events'][0]['id']
            print(mention + ' '+str(mentionId))
            inspiredFactory(mention,mentionId)
        return JsonResponse({
            'msg':'post request received'
        })