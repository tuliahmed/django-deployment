from django.shortcuts import render
from First_app.forms import UserForm,UserinfoForm
from django.contrib.auth.models import User 
from First_app.models import Userinfo

from django.contrib.auth import authenticate,login,logout
from  django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    dic={}
    if request.user.is_authenticated:
        current_user = request.user
        us_id=current_user.id
        user_basic_info=User.objects.get(pk=us_id)
        user_more_info=Userinfo.objects.get(user__pk=us_id)
        dic={'userbasic_info': user_basic_info,'userMoreInfo': user_more_info}
    return render(request, 'First_app/index.html',context=dic)



def register(request):
    register=False 
    if request.method=='POST':
        usform=UserForm(data=request.POST)
        u_I_F=UserinfoForm(data=request.POST)
        if usform.is_valid() and u_I_F.is_valid():
            vuser=usform.save()
            vuser.set_password(vuser.password)
            # the above code  convert the pain text password into a incrypted password 
            vuser.save()

            #  user info field 
            user_info=u_I_F.save(commit=False)
            user_info.user=vuser
            if "Profile_Picture" in request.FIELS:
                user_info.Profile_P=request.FILES['Profile_Picture']
                

            user_info.save()

            register=True

    else:
        usform=UserForm()
        u_I_F=UserinfoForm()

    diction={'usform':usform,'u_I_F':u_I_F,'Register':register}
    return render(request, 'First_app/Register.html', context= diction)




# _________________________________________________________________________losg in page views for User login _____________________________________________________________


def login_page(request):
    return render(request, 'First_app/login.html',context={})



def user_login(request):
    if request.method=='POST':
        User_Name_V=request.POST.get('User_Name')
        User_Password_V=request.POST.get('User_Password')

        user=authenticate(username=User_Name_V,password=User_Password_V)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('relative:index'))
                # return render(request, 'First_app/index.html',context={})
                # return index(request)
 
            else:

                return HttpResponse("Account is not active")
        else:
            return HttpResponse("Invalid login details")
    
    else:
        return HttpResponseRedirect(reverse('relative:login'))
        # return render(request, 'First_app/login.html',context={})
    



# _________________________________________________________________________end Log in  _________________________________________________________________


# _______________________________________________________________logout_______________________________________________________________
@login_required
def usr_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('relative:login'))
    # return render(request, 'First_app/login.html',context={})