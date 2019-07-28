from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from apps.restaurants.models import Restaurant, Table
import bcrypt
import datetime

def registerAndLogin(request):
    #Display register/login page
    return render(request, "users/index.html")

def newUser(request):
    return render(request, 'users/user.html')

def createUser(request):
    #Validate user data
    postData = request.POST.copy()
    postData["email"] = postData["email"].lower()
    errors = User.objects.validateUser(postData)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')

    #POST
    if request.method == 'POST':

        #Create new user
        newUser = User.objects.create(
            firstName = postData['firstName'],
            lastName = postData['lastName'],
            email = postData['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        newUser.save()
        user = User.objects.get(email = postData['email'])
        request.session['user'] = user.id

        #Redirect to user dashboard
        return redirect('/users/dashboard') 

def businessCard(request):
    return render(request, 'users/businessCard.html')

def editUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if 'user' not in request.session:
        messages.error(request, 'You must be logged in.')
        return redirect('/')
    if request.session['user'] != int(userId):
        messages.error(request, 'You cannot edit someone else\'s page.')
        return redirect('/users/dashboard')

    #Get user
    context = {
        'user' : User.objects.get(id = userId)
    }

    #Render the user edit page
    return render(request, 'users/editUser.html', context)

def updateUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if 'user' not in request.session:
        messages.error(request, 'You must be logged in.')
        return redirect('/')
    if request.session['user'] != int(userId):
        messages.error(request, 'You cannot edit someone else\'s page.')
        return redirect(f'/users/dashboard')

    #POST
    if request.method == "POST":

        #Validate data
        postData = request.POST.copy()
        postData["email"] = postData["email"].lower()
        errors = User.objects.validateUserEdit(postData)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/users/{ userId }/edit')

        #Update the user
        user = User.objects.get(id = userId)
        user.firstName = postData['firstName'] or user.firstName
        user.lastName = postData['lastName'] or user.lastName
        user.email = postData['email'] or user.email
        if postData["password"] != "":
            user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()

    #Redirect to view user
    return redirect('/users/dashboard')

def deleteUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if 'user' not in request.session:
        messages.error(request, 'You must be logged in.')
        return redirect('/')
    if request.session['user'] != int(userId):
        messages.error(request, 'You can not delete someone else\'s page.')
        return redirect('/users/dashboard')
    
    #Delete user from database
    delUser = User.objects.get(id = userId)
    delUser.delete()

    #Redirect to index
    return redirect ('/')

def login(request):
    #Validate user
    postData = request.POST.copy()
    postData["email"] = postData["email"].lower()
    errors = User.objects.validateLogin(postData)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    #POST
    if request.method == 'POST':

        #log user in (don't forget session)
        user = User.objects.get(email = postData["email"])
        request.session['user'] = user.id

        #Redirect to dashboard
        return redirect('/users/dashboard')

def logout(request):
    #Remove user from session
    request.session.clear()

    #Return to index
    return redirect('/')

def userDashboard(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if 'user' not in request.session:
        messages.error(request, 'You must be logged in.')
        return redirect('/')

    #Renders the main page for the user
    user = User.objects.get(id = request.session['user'])

    context = {
        "user" : user,
    }
    
    if user.restaurant != None:
        users = User.objects.filter(restaurant = user.restaurant)

        waitTime = (datetime.datetime.now() - user.time.replace(tzinfo = None)).total_seconds()
        waitTime = round(waitTime // 60)
        
        position = 1
        for lineMember in users:
            if lineMember.time < user.time:
                position += 1

        context["members"] = users
        context["waitTime"] = waitTime
        context["position"] = position
        context["restaurant"] = Restaurant.objects.get(user = user).name

    if user.table != None:
        context["restaurant"] = Table.objects.get(user = user).restaurant.name

    return render(request, 'users/dashboard.html', context)

def deleteLine(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if 'user' not in request.session:
        messages.error(request, 'You must be logged in.')
        return redirect('/')
    if request.session['user'] != int(userId):
        messages.error(request, "You do not have authorization to do that")
        return redirect('/users/dashboard')

    #Remove user from restaurant
    user = User.objects.get(id = userId)
    user.restaurant = None
    user.save()

    #Return to dashboard
    return redirect('/users/dashboard')
