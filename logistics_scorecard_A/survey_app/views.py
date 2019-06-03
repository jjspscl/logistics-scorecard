from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import smtplib



# Create your views here.


def index(request, cid):
    scorecard = Scorecard.objects.get(cid=cid)
    categories = scorecard.category_list.all()
    ratings = scorecard.rating.all()
    context = {
        "scorecard": scorecard,
        "categories": categories,
        "ratings": ratings,
    }
    
    if request.method == 'POST':
        answer1 = request.POST.get('cat-A-row-2')
        return HttpResponse(answer1)
    else:
        return render(request, "try.html", context)

def email_view(request):
    send_mail('test','test','realtantan7@gmail.com', ['Alvin.Panganiban@artesyn.com'])
    return HttpResponse("OK")

