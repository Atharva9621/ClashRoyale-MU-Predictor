from django.shortcuts import render
from django.http import HttpResponse
from .prediction import predictionModel

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    print(request.body)
    result = 0
    if(request.method == "POST"):
        print('here')
        cards = request.POST.get('cards')
        opp_cards = request.POST.get('rcards')
        print(cards)
        print(opp_cards)
        cards=cards.split(',')
        opp_cards=opp_cards.split(',')
        cards = [int(i) for i in cards]
        opp_cards = [int(i) for i in cards]
        print(cards)
        result = predictionModel(cards, opp_cards)
    return render(request, 'result.html', {
        'MU_result' : result
    })


