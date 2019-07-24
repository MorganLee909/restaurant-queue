from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from apps.restaurants.models import Restaurant
import bcrypt
import datetime

def registerAndLogin(request):
    #Display register/login page
    return render(request, "users/index.html")

def newUser(request):
    return render(request, 'users/user.html')

def createUser(request):
    #Validate user data
    errors = User.objects.validateUser(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')

    #POST
    if request.method == 'POST':

        #Create new user
        newUser = User.objects.create(
            firstName = request.POST['firstName'],
            lastName = request.POST['lastName'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        newUser.save()
        user = User.objects.get(email = request.POST['email'])
        request.session['user'] = user.id
        request.session['firstName'] = user.firstName

        #Redirect to user dashboard
        return redirect('/users/dashboard') 

def editUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
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
    if request.session['user'] != int(userId):
        messages.error(request, 'You can not edit someone else\'s page.')
        return redirect(f'/users/dashboard')

    #POST
    if request.method == "POST":

        #Validate data
        errors = User.objects.validateUserEdit(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/users/{ userId }/edit')

        #Update the user
        user = User.objects.get(id = userId)
        user.firstName = request.POST['firstName'] or user.firstName
        user.lastName = request.POST['lastName'] or user.lastName
        user.email = request.POST['email'] or user.email
        user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()) or user.password
        user.save()

    #Redirect to view user
    return redirect('/users/dashboard')

def deleteUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
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
    errors = User.objects.validateLogin(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    #POST
    if request.method == 'POST':

        #log user in (don't forget session)
        user = User.objects.get(email = request.POST['email'])
        request.session['user'] = user.id
        request.session['firstName'] = user.firstName

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
    currentUser = User.objects.get(id = request.session['user'])

    context = {
        "user" : currentUser
    }
    
    if hasattr(currentUser, "line"):
        userLine = LineMember.objects.get(member = currentUser)
        userRestaurant = Restaurant.objects.get(line = userLine)
        users = LineMember.objects.filter(restaurant = userRestaurant)

        waitTime = (datetime.datetime.now() - currentUser.line.joined.replace(tzinfo = None)).total_seconds()
        waitTime = round(waitTime // 60)
        
        position = 1
        for user in users:
            if user.joined < currentUser.line.joined:
                position += 1

        context["members"] = users
        context["waitTime"] = waitTime
        context["position"] = position

    return render(request, 'users/dashboard.html', context)

def deleteLine(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if request.session['user'] != int(userId):
        messages.error(request, "You do not have authorization to do that")
        return redirect('/users/dashboard')

    #Delete user from database
    delLine = LineMember.objects.get(member = userId)
    delLine.delete()

    #Return to dashboard
    return redirect('/users/dashboard')
