from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable1' : 'This is a sent',
        'variable2' : 'This is a sent'
    }
    return render(request,'index.html',context)
    # return HttpResponse('This is a black body')

def about(request):
    return render(request,'about.html')

    # return HttpResponse('This is a about page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request,'contact.html')

    # return HttpResponse('This is a contact page')

def services(request):
    return render(request,'services.html')


def singleProductPage(request):
    return render(request, "singleProduct.html")

def Helloproduct(request):
    return render(request,"Helloproduct")
#     # return HttpResponse('This is a services page')

# def single_product(request, id):
#     product = request.objects.get(id=id)
#     relevant = request.objects.filter(product=product)

#     return render(request, "singleproduct.html", {
#         "product": product,
#         "relevant_images": relevant
#     })





