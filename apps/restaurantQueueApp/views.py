from django.shortcuts import render

def index(request):
    return redirect("/user/new")

def registerAndLogin(request):
    #Display register/login page
    pass

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

def displayTables(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Display all tables
    pass
    
def newTable(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Display form to create a new table
    #Redirect to create route
    pass

def createTable(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #POST
    #Validate data
    #Create new table
    #redirect to restaurant dashboard
    pass

def editTable(request, tableId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Render page to show/edit specific table
    pass

def updateTable(request, tableId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Validate new table data
    #Update the table
    #Redirect back to restaurant dashboard
    pass

def deleteTable(request, tableId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Remove table from database
    #Redirect to restaurant dashboard
    pass

def userDashboard(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Renders the main page for the user
    pass

def restaurantDashboard(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Renders the main page for the restaurant
    pass