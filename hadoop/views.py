from django.http import Http404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from hadoop.models import Job
from rest_framework import serializers
from hadoop.serializer import JobSerializer
from hadoop.serializer import RequestSerializer
import requests
import os.path, subprocess, time
import sys
from subprocess import STDOUT, PIPE

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def update(self, id, result):
    job = Job.objects.get(id=id)
    job.result = result
    job.save()
    return HttpResponse("Saved")
class JobInit(APIView):
    serializer_class = JobSerializer
    def post(self, request):
        url = 'http://52.221.255.33/hadoop/all/' # Set destination URL here
        post_fields = {"input": request.data['input'], "result": ''}     # Set POST fields here
        # request2 = Request(url, urlencode(post_fields).encode())
        r = requests.post(url,post_fields)
        return HttpResponse(r.text)


class JobView(APIView):
    serializer_class = JobSerializer

    def get(self, request, id):
        job = Job.objects.get(id=id)
        response = self.serializer_class(job)
        return Response(response.data)


class JobViewList(APIView):
    serializer_class = JobSerializer

    def get(self, request):
        job = Job.objects.all()
        response = self.serializer_class(job,many=True)
        return Response(response.data)


    def post(self, request):
        serializer = JobSerializer(data=request.data)
        os.chdir("/home/ubuntu")
        if serializer.is_valid():
            job = serializer.save()
            file = open(str(job.id)+'.txt', 'w')
            file.write(request.data['input'])
            command = str("pig -x local -param user_input=\"/home/ubuntu/WebAppStupidServer/"+str(job.id)+".txt\" -param output_path=/home/ubuntu/output/"+str(job.id)+" -f /home/ubuntu/sentence_search.pig")
            file.close()
            self.execute(command)
            job = Job.objects.get(id=job.id)
            
            gatcom = "cat /home/ubuntu/output/"+str(job.id)+" /* >> /home/ubuntu/output/output"+str(job.id)+".txt"
            self.execute(gatcom)
            with open('/home/ubuntu/output/output'+str(job.id)+".txt", 'r') as myfile:
                data=myfile.read()

            job.result = data
            job.save()
            return HttpResponse(data)

        return HttpResponse("Error!!")
        

    def execute(self, command):
        print (command + "\n")
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = p.communicate()
        print (stdout)
        return p.returncode