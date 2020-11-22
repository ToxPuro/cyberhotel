from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Hotel
from .models import Receipt
from django.shortcuts import redirect
from .models import Card
from .models import Comment
from django.db import connection, transaction

@login_required(login_url='/login/')
def home(request):
    cursor=connection.cursor()
    search=request.GET.get('search','')
    message=request.POST.get('msg','')
    Comment.objects.create(content=message)
    messages=Comment.objects.all()
    Hotels=cursor.execute("SELECT * FROM shop_hotel WHERE name='%s'" %(search))
    Hotels2=''
    if search != '':
        Hotels2=Hotel.objects.filter(name__startswith=search)
    Receipts=Receipt.objects.filter(customer=request.user)
    return render(request, "shop/home.html", {"Receipts":Receipts,"Hotels":Hotels, "messages":messages, "Hotels2":Hotels2})    

# Create your views here.
@login_required(login_url='/login/')
def receipt(request, receipt_id):
    receipt=Receipt.objects.filter(id=receipt_id).first()
    user=request.user
    card=Card.objects.filter(owner=user).first()
    return render(request, "shop/receipt.html", {'Receipt':receipt, "Card":card})

@login_required(login_url='/login/')
def hotel(request, hotel_id):
    card=Card.objects.filter(owner=request.user).first()
    cardnumber=request.GET.get('number','')
    password=request.GET.get('password','')
    hotel=Hotel.objects.filter(id=hotel_id).first()
    false=''
    if not (password=='' and cardnumber==''):
        if password==card.password and cardnumber==card.cardnumber:
            Receipt.objects.create(customer=request.user,hotel=hotel)
            return redirect("/shop/")
        elif password !=card.password and cardnumber !=card.cardnumber:
            false='False cardnumber or password'
        elif password !=card.password:
            false="False password"
        else:
            false="False cardnumber"
    return render(request, "shop/hotel.html", {"Card":card,"False":false})

    