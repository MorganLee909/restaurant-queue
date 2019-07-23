from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import Restaurant, Table
#Possibly need to import from users

def newRestaurant(request):
    #Render the page to show form to create new restaurant
    return render(request, "restaurants/newRestaurant.html")

def createRestaurant(request):
    #POST
    if request.method == "POST":

        #Validate all data
        errors = Restaurant.objects.validateRestaurant(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/restaurants/new')

        #Create and add new restaurant to database
        newRestaurant = Restaurant(
            name = request.POST["name"],
            email = request.POST["email"],
            password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()),
        )
        newRestaurant.save()

    #redirect to restaurant dashboard
    request.session["restaurant"] = newRestaurant.id
    return redirect("/restaurants/dashboard")

def loginPage(request):
    #Render login page
    return render(request, "restaurants/login.html")

def restaurantLogin(request):
    #POST
    if request.method == "POST":

        #Validate restaurant
        errors = Restaurant.objects.validateLogin(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/restaurants')

        #Log in restaurant
        restaurant = Restaurant.objects.get(email = request.POST["email"])
        request.session["restaurant"] = restaurant.id

    #Redirect to dashboard
    return redirect("/restaurants/dashboard")

def showRestaurant(request, restaurantId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    restaurant = Restaurant.objects.get(id = restaurantId)
    if request.session["restaurant"] != restaurant.id:
        messages.error(request, "You do not have authorization to view that page")
        return redirect("/restaurants")

    #Render page to display restaurant information
    context = {
        "restaurant" : restaurant
    }

    return render(request, "restaurants/showRestaurant", context)

def editRestaurant(request, restaurantId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    restaurant = Restaurant.objects.get(id = restaurantId)
    if request.session["restaurant"] != restaurant.id:
        messages.error(request, "You do not have authorization to view that page")
        return redirect("/restaurants")

    #Render page with form to edit restaurant information
    context = {
        "restaurant" : restaurant
    }

    return render(request, "restaurants/editRestaurant.html", context)

def updateRestaurant(request, restaurantId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    restaurant = Restaurant.objects.get(id = restaurantId)
    if request.session["restaurant"] != restaurant.id:
        messages.error(request, "You do not have authorization to view that page")
        return redirect("/restaurants")

    #POST
    if request.method == "POST":

        #Validate all data
        errors = Restaurant.objects.validateRestaurant()
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

        #Update the data
        restaurant.name = request.POST["name"] or restaurant.name
        restaurant.email = request.POST["email"] or restaurant.email
        restaurant.password= bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()) or restaurant.password

    #Redirect to restaurant dashboard
    return redirect("/restaurants/dashboard")

def destroyRestaurant(request, restaurantId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    restaurant = Restaurant.objects.get(id = restaurantId)
    if request.session["restaurant"] != restaurant.id:
        messages.error(request, "You do not have authorization to view that page")
        return redirect("/restaurants")

    #Delete from database
    restaurant.delete()

    #Redirect to index(?)
    return redirect("/")

def displayTables(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if "restaurant" not in request.session:
        messages.error(request, "Must be logged in to view this page")
        return redirect("/restaurant")

    #Display all tables
    context = {
        "restaurant" : Restaurant.objects.get(id = request.session["restaurant"])
    }
    
    return render(request, "restaurants/showTables")
    
def newTable(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if "restaurant" not in request.session:
        messages.error(request, "Must be logged in to view this page")
        return redirect("/restaurant")

    #Display form to create a new table
    return render(request, "restaurants/newTable.html")

def createTables(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    #POST
    #Validate data
    #Create new table
    #redirect to restaurant dashboard
    pass

def editTables(request, tableId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if "restaurant" not in request.session:
        messages.error(request, "Must be logged in to view this page")
        return redirect("/restaurant")\

    #Render page to show/edit specific table
    return render(request, "restaurants/editTables.html")

def updateTables(request, tableId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    try:
        restaurant = Restaurant.objects.get(id = request.session["restaurant"])
    except:
        messages.error(request, "Must be logged in to do that")
        return redirect("/restaurants")

    table = Table.objects.get(id = tableId)
    if table.restaurant.id != restaurant.id:
        messages.error(request, "You do not have authorization to do that")
        return redirect("/restaurants/dashboard")

    #POST
    if request.method == "POST":

        #Validate new table data
        errors = Table.objects.validateTable(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
    
        #Update the table
        table.name = request.POST["name"] or table.name
        table.size = request.POST["size"] or table.size

    #Redirect back to restaurant dashboard
    return redirect("/restaurants/dashboard")

def deleteTable(request, tableId):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    try:
        restaurant = Restaurant.objects.get(id = request.session["restaurant"])
    except:
        messages.error(request, "Must be logged in to do that")
        return redirect("/restaurants")

    table = Table.objects.get(id = tableId)
    if table.restaurant.id != restaurant.id:
        messages.error(request, "You do not have authorization to do that")
        return redirect("/restaurants/dashboard")

    #Remove table from database
    table.delete()

    #Redirect to restaurant dashboard
    return redirect("/restaurants/dashboard")

def restaurantDashboard(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if "restaurant" not in request.session:
        messages.error(request, "Must be logged in to view this page")
        return redirect("/restaurants")

    #Renders the main page for the restaurant
    context = {
        "restaurant" : Restaurant.objects.get(id = request.session["restaurant"])
    }

    return render(request, "restaurants/dashboard.html", context)  ## add in context when complete
