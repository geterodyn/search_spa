import json
from urllib.parse import urlparse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, reverse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import UpdateView
from jobs.models import JobItem
from mysearch import word_count


class Job_API(UpdateView, View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(Job_API, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        jobs = [job.to_dict() for job in JobItem.objects.all()]
        return JsonResponse({'jobs': jobs})

    def post(self, request, *args, **kwargs):
        params = json.loads(request.body)
        url = params['url']
        word = params['search_word']
        u = urlparse(url)
        url = url if u.scheme else 'http://' + url
        job = word_count.delay(url, word)
        JobItem.objects.create(
            uuid = job.id,
            status = job.status,
            url = params['url'],
            search_word = word
        )
        return HttpResponse(status=201)


def jobs_update(request):
    for entry in JobItem.objects.exclude(status='SUCCESS'):
        job = entry.get_job()
        entry.status = job.status
        entry.result = job.result
        entry.save()
    return HttpResponse(status=201)

def jobs_delete(request):
    JobItem.objects.all().delete()
    return HttpResponse(status=201)

#test
