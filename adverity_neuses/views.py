from adverity_neuses.contentManager import ContentManager

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect


"""
Everything here is kept simple and straightforward due to time constraints

"""

#@cache_page(60*1)
def index(request, *args):
    parameters = {}
    return render(request, 'index.html', parameters)

def task1(request):
    parameters = {}
    return render(request, 'task1.html', parameters)

def task2(request):
    parameters = {}
    return render(request, 'task2.html', parameters)

def api_task1(request):
    contentManager = ContentManager()
    data= contentManager.buildTask1Content()
    if request.method == 'POST':
        return JsonResponse({"message": "Sorry, this is currently not supported!", "data": request.data})
    return JsonResponse(data)

def api_task2(request):
    keyword = request.GET['keyword']
    contentManager = ContentManager()
    data= contentManager.buildTask2Content(keywords=keyword)
    if request.method == 'POST':
        return JsonResponse({"message": "Sorry, this is currently not supported!", "data": request.data})
    return JsonResponse(data)


"""

#Initially, I wanted to build a nice connection between front and backend but in the end, I did not finish it due to time constraints

class MyApiViewSet(viewsets.ViewSet):

    #A simple ViewSet for listing or retrieving the dynamic data needed.

    def task1(self, request):
        queryset = User.objects.all()
        serializer = Task1Serializer(queryset, many=True)
        return Response(serializer.data)

    def task2(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = Task2Serializer(user)
        return Response(serializer.data)
"""
