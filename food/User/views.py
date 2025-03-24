from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from posts.models import Post

# Create your views here.
def Homepage(request):
    return render(request,'home.html')

def registers(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)#this
        if form.is_valid():                #and this validates the form and stops if there also anyone trying to register using same username as it exists already
            login(request,form.save())
            return redirect("users:Home")#here users:Home == {app_name defined in urls.py:name of the path}
    else:
        form=UserCreationForm()
    return render(request,'User/user_register.html',{"form":form})#we use this to add form in our template

def login_view(request):
    if request.method =="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())#we login 
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else:
        form=AuthenticationForm()    
    return render(request,'User/user_login.html',{"form":form})


def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect("posts:Home")


def user_profile(request):
    posts = Post.objects.all()  
    context = {
        'posts': posts,  
    }
    return render(request, 'User/user_login.html', context)








