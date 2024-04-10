from http.client import HTTPResponse
from urllib import request
from django import views
# from django.http import HttpResponse
# from ssl import _PasswordType
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Milk
# from django.contrib.auth.hashers import User,make_password
from .models import register
# from .user import register
from .views import register
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views import View





# Create your views here.
def home(request):
    return render(request,'home.html')

def product(request):
    return render(request,'product.html')


def bread(request):
    return render(request,'bread.html', {'price':700})

def milk(request):
    
    # Milk1=Milk()
    # Milk1.name='Buffalo milk'
    # Milk1.desc='Country Delight is delighted to present the brand of desi eggs that has become a quick favourite among our egg connoisseurs'
    # Milk1.liter=250
    # Milk1.price=350
    # Milk1.img='apple.jpeg'
    
    # Milk2=Milk()
    # Milk2.name='Buffalo milk'
    # Milk2.desc='Country Delight is delighted to present the brand of desi eggs that has become a quick favourite among our egg connoisseurs'
    # Milk2.liter=250
    # Milk2.price=350
    # Milk2.img='android.png'
    
    # Milk3=Milk()
    # Milk3.name='Buffalo milk'
    # Milk3.desc='Country Delight is delighted to present the brand of desi eggs that has become a quick favourite among our egg connoisseurs'
    # Milk3.liter=250
    # Milk3.price=350
    # Milk3.img='apple(1).png'
    
    # milks=[Milk1]
    # return render(request,'milk.html',{'milks':milks})
    milks=Milk.objects.all()
    return render(request,'milk.html',{'milks':milks})
  
  
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
     return render(request,'login.html')
 
def register(request):
    if request.method == 'POST':
#         #  user = register(request) 
#         #  if user.is_valid():
#         #     user.save()
            
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')
        

        
        #validation
            value={
            'first_name':first_name,'last_name':last_name,'username':username,'password1':password1,'password2':password2,' email': email}
        
            if password1 != password2:
             return HttpResponse("password not match")
        
            user = User.objects.create_user(username=username,email=email, password=password1,
                                        first_name=first_name, last_name=last_name)
            user.save()
            print('user created')
            return render(request, 'home.html')
    
   
    else:
     return render(request, 'register.html') 
  
    


# def buffalo_milk(request):
#     return render(request,'buffalo_milk.html',{'price':700})
# def add(request):
#     val1=int(request.POST['num1'])
#     val2=int(request.POST['num2'])
#     res=val1+val2
#     return render(request,'result.html',{'result':res})

# class register(View):
#     def get(self, request):
#         return render(request, 'register.html')

#     def post(self, request):
#         postData = request.POST
#         first_name = postData.get('firstname')
#         last_name = postData.get('lastname')
#         # user = postData.get('user')
#         # phone = postData.get('phone')
#         # email = postData.get('email')
#         # password = postData.get('password')
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         email = request.POST.get('email')
        
#         user = User(username=username,first_name=first_name, last_name=last_name, password1=password1,password2=password2,email=email)
#         error_message = self.validateUser(user)

#         if not error_message:
#             user.password = make_password(user.password)
#             user.register()
#             return redirect('homepage')
#         else:
#             data = {'error': error_message, 'values': {'first_name': first_name, 'last_name': last_name, 'password': password1,'password': password2,'email': email}}
#             return render(request, 'register.html', data)

#     def validateUser(self,user):
#         error_message = None
#         if not user.first_name:
#             error_message = "First Name Required !!"
#         elif len(user.first_name) < 4:
#             error_message = 'First Name must be 4 char long or more'
#         # Add more validations as needed
#         return error_message