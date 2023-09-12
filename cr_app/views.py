from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    print(request.body)
    if(request.method == "POST"):
        print('here')
        context = request.POST.get('cards')
        dummy_var = request.POST.get('dummy')
        print(context)
        print(dummy_var)
    return render(request, 'result.html', {
        'MU_result' : 3
    })
