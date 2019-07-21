from django.shortcuts import render

def registerAndLogin(request):
    #Display register/login page
    return render(request, "users/index.html")

def createUser(request):
    #POST
    #Validate user data
    #Create new user
    #Redirect to user dashboard
    pass

def viewUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Get user
    #Render the user data page
    pass

def editUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Get user
    #Render the user edit page
    pass

def updateUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #POST
    #Validate data
    #Update the user
    #Redirect to view user
    pass

def deleteUser(request, userId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Delete user from database
    #Redirect to index
    pass

def login(request):
    #POST
    #Validate user
    #log user in (don't forget session)
    #Redirect to dashboard
    pass

def logout(request):
    #Remove user from session
    #Return to index
    pass

def userDashboard(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Renders the main page for the user
    pass