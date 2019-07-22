from django.shortcuts import render, redirect
<<<<<<< HEAD
import bcrypt
from django.contrib import messages
from .models import User
=======
from django.contrib import messages
from .models import *
import bcrypt
>>>>>>> models-routes

def registerAndLogin(request):
    #Display register/login page
    return render(request, "users/index.html")

def newUser(request):
<<<<<<< HEAD
    return render(request, "users/user.html")
=======
    return render(request, 'users/user.html')
>>>>>>> models-routes

def createUser(request):
    #POST
    #Validate user data
    #Create new user
    #Redirect to user dashboard
<<<<<<< HEAD
    pass
   
=======
    errors = User.objects.validateUser(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
>>>>>>> models-routes

    else:
        newUser = User.objects.create(
            firstName = request.POST['firstName'],
            lastName = request.POST['lastName'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        newUser.save()
        user = User.objects.get(email = request.POST['email'])
        request.session['user'] = user.id
        request.session['first_name'] = user.first_name
        return redirect('/dashboard/user') 

def editUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Get user
    #Render the user edit page
    if request.session['user'] != User.objects.get(id = userId):
        return redirect('/users/dashboard')

    context = {
        'user' : User.objects.get(id = userId)
    }
    return render(request, 'users/showUser.html', context)

def updateUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #POST
    #Validate data
    #Update the user
    #Redirect to view user
    if request.session['user'] != User.objects.get(id = userId):
        return redirect('/users/dashboard')

    errors = User.objects.validateUser(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/users/{ userId }/update')

    else:
        user = User.objects.get(id = userId)
        user.firstName = request.POST['firstName']
        user.lastName = request.POST['lastName']
        user.email = request.POST['email']
        user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        
    return redirect('/users/dashboard')

def deleteUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Delete user from database
    #Redirect to index
    if request.session['user'] != User.objects.get(id = userId):
        return redirect('/users/dashboard')
    
    else:
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
    pass