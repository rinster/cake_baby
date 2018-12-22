from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from twilio.rest import Client


from apps.cake_baby.models import *

def index(request):
    
    return render(request, 'cake_baby/index.html')

def portfolio(request):
    context = {
        "images" : Photo.objects.all()
    }
    return render(request, 'cake_baby/portfolio.html', context)

def cakeRequest(request):
    Inquiry.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], telephone=request.POST['telephone'], event=request.POST['event'], event_date=request.POST['event_date'], order_desc=request.POST['order_desc'])
    
    #########Email Below
    # form_email = request.POST["email"]
    # form_tel = request.POST["telephone"]
    # form_first_name = request.POST["first_name"]

    # subject = "New Inquiry"
    # from_email = settings.EMAIL_HOST_USER
    # to_email = ['enatnat.08@gmail.com']
    # contact_message = "You have a new inquiry! Please login to your website account"
    
    # send_mail(subject,
    #         contact_message,
    #         from_email,
    #         to_email,
    #         fail_silently=False)

    #####TWILIO Notification Below
    account_sid = 'AC6ee1cb8d9a65c84eaf8bb0d89b5561fc'
    auth_token = '471e816811a19f8beb336a8fbff36717'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                    body="You have a new inquiry on your website!",
                                    from_='+14158535016',
                                    to='+15104278060'    
                                    )
    print(message.sid)
    return redirect('/success')

def success(request):
    
    return render( request, 'cake_baby/success.html')
    
def login(request):

    return render(request, 'cake_baby/adminLogin.html')

def loginProcess(request):
    if request.method != 'POST':
        return redirect('/login')
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect("/login")
    user = User.objects.filter(email=request.POST["email_login"])
    u1 = user[0] 
    if u1.password != request.POST["password_login"]:
        messages.error(request, "Invalid Login", extra_tags="password_login")
        return redirect('/login')
    else:    
        request.session["cur_user_email"] = u1.email
        return redirect("/admin_page")

def admin_page(request):
    if "cur_user_email" in request.session:
        email = request.session["cur_user_email"]
        user = User.objects.filter(email=email)
        u1 = user[0]
        if u1.role == "admin":
            context = {
                "inquiries" : Inquiry.objects.all(),
                "images" : Photo.objects.all()
            } 
            return render(request, 'cake_baby/admin.html', context)
    return redirect("/login")

###AJAX Search process Here####
def search(request):
    inquiries = Inquiry.objects.filter(first_name__contains=request.POST['search_info'])|Inquiry.objects.filter(last_name__contains=request.POST['search_info'])|Inquiry.objects.filter(email__contains=request.POST['search_info'])|Inquiry.objects.filter(event__contains=request.POST['search_info'])|Inquiry.objects.filter(order_desc__contains=request.POST['search_info'])
    return render(request, "cake_baby/all_orders.html", {'inquiries': inquiries })

def delete(request, id):
    order = Inquiry.objects.get(id = id)
    order.delete()
    return redirect("/admin_page")

def logout(request):
    request.session.clear()
    return redirect("/login")

def img_upload(request):
    Photo.objects.create(title=request.POST['caption'], desc=request.POST['desc'], photo_image=request.FILES['photo_image'])
    return redirect('/img_page')


####UPLOAD IMAGES TEST

def img_page(request):
    context = {
        "images" : Photo.objects.all()
    }
    return render(request, 'cake_baby/file_upload.html', context)

def test(request):
    context = {
        "images" : Photo.objects.all()
    }
    return render(request, 'cake_baby/test.html', context)