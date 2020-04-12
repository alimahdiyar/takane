from django.shortcuts import render,redirect

def register(request):
    if request.method=='POST':
        print("SUBMITED REG")
        return redirect('register')
    else:
        return render(request,'Accounts/register.html')

def login(request):
    if request.method=='POST':
        print("SUBMITED LOGIN")
        return redirect('login')
    else:
        return render(request,'Accounts/login.html')
    

def logout(request):
    return redirect('home')