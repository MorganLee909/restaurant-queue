from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def registerAndLogin(request):
    #Display register/login page
    return render(request, "users/index.html")

def newUser(request):
    return render(request, 'users/user.html')

def createUser(request):
    #POST
    #Validate user data
    #Create new user
    #Redirect to user dashboard
    errors = User.objects.validateUser(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')

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
    return redirect('/users/dashboard') 

def editUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Get user
    #Render the user edit page
    if request.session['user'] != int(userId):
        return redirect('/users/dashboard')

    context = {
        'user' : User.objects.get(id = userId)
    }
    return render(request, 'users/editUser.html', context)

def updateUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #POST
    #Validate data
    #Update the user
    #Redirect to view user
    if request.session['user'] != int(userId):
        return redirect('/users/dashboard')
    if request.method == "POST":

        errors = User.objects.validateUser(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/users/{ userId }/update')

        else:
            user = User.objects.get(id = userId)
            user.firstName = request.POST['firstName'] or user.firstName
            user.lastName = request.POST['lastName'] or user.lastName
            user.email = request.POST['email'] or user.email
            user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()) or user.password
            user.save()
            
    return redirect('/users/dashboard')

def deleteUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Delete user from database
    #Redirect to index
    if request.session['user'] != int(userId):
        return redirect('/users/dashboard')
    
    delUser = User.objects.get(id = userId)
    delUser.delete()
    return redirect ('/')

def login(request):
    #POST
    #Validate user
    #log user in (don't forget session)
    #Redirect to dashboard
    errors = User.objects.validateLogin(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['user'] = user.id
        request.session['firstName'] = user.firstName
        return redirect('/users/dashboard')


def logout(request):
    #Remove user from session
    #Return to index
    request.session.clear()
    return redirect('/')

def userDashboard(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Renders the main page for the user
    if 'user' not in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['user'])
    context = {
        'user' : user
    }
    return render(request, 'users/dashboard.html', context)

def deleteLine(request, userId):
    if request.session['user'] != int(userId):
        return redirect('/users/dashboard')

    delLine = LineMember.objects.get(members = userId)
    delLine.delete()
    return redirect('/users/dashboard')
