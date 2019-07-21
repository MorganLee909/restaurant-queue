from django.shortcuts import render
from .models import Restaurant, Table
#Possibly need to import from users

def newRestaurant(request):
    #Render the page to show form to create new restaurant
    pass

def createRestaurant(request):
    #POST
    #Validate all date
    #Create and add new restaurant to database
    #redirect to restaurant dashboard
    pass

def showRestaurant(request, restaurantId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Render page to display restaurant information
    pass

def editRestaurant(request, restaurantId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Render page with form to edit restaurant information
    pass

def updateRestaurant(request, restaurantId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Validate all data
    #Update the data
    #Redirect to restaurant dashboard
    pass

def destroyRestaurant(request, restaurantId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Delete from database
    #Redirect to index(?)
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

def restaurantDashboard(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #Renders the main page for the restaurant
    pass