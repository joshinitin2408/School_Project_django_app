from django.shortcuts import render
from datetime import datetime
from Web.models import Admission, Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        msg = request.POST.get('msg')
        contact = Contact(Name=name, Mobile=mobile, Message=msg)
        contact.save()

    return render(request,'contact.html')

def admission(request):
    if request.method == 'POST':
        father = request.POST.get('father')
        fo = request.POST.get('fo')
        mother = request.POST.get('mother')
        mo = request.POST.get('mo')
        child = request.POST.get('child')
        age = request.POST.get('age')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        division = request.POST.get('division')
        desc = request.POST.get('desc')
        admission = Admission(Father=father, FatherOccupation=fo, Mother=mother, MotherOccupation=mo, Child=child, Age=age, Address=address, Mobile=mobile, Division=division, Description=desc, Date=datetime.today() )
        admission.save()
    return render(request,'admission.html')

def facilities(request):
    return render(request,'facilities.html')

def infrastructure(request):
    return render(request,'infrastructure.html')

def achievments(request):
    return render(request,'achievments.html')

def gallary(request):
    return render(request,'gallary.html')
