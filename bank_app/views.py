
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from bank_app.models import Account, Details_info


def home(request):

    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':

        password=request.POST['password']
        username=request.POST['username']
        if Account.objects.filter(username=username).exists():
            messages.success(request, 'username already exists')
            return redirect('register')
        else:
            user=Account.objects.create_user(username=username, password=password,)
            user.save()
            messages.success(request, 'Thank you for registering with us.')

        return redirect('/login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            request.session['username']=username
            if user.is_admin:
                return redirect('admin/')
            else:
                return redirect('home')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



from django.http import JsonResponse
from django.shortcuts import render
from .models import Branch


def get_branches(request):
    district = request.GET.get('district')
    branches = Branch.objects.filter(district=district).values_list('name', flat=True)
    data = {'branches': list(branches)}
    return JsonResponse(data)

def add(request):
    district="Ernakulam"
    name="Edapally"
    addd=Branch(district=district,name=name)
    addd.save()
    redirect('home')


@login_required(login_url='login')
def details(request):
    if request.method=="POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        address = request.POST.get('address')
        acc_type = request.POST.get('acc_type')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        debit = request.POST.get('debit')
        credit = request.POST.get('credit')
        cheque = request.POST.get('cheque')
        detail=Details_info(name=name,gender=gender,dob=dob,age=age,email=email,tel=tel,address=address,acc_type=acc_type,
                            district=district,branch=branch,debit=debit,credit=credit,cheque=cheque)
        detail.save()
        messages.success(request, 'Your application is accepted...!')

        return redirect('home')


    return render(request, 'details.html')


