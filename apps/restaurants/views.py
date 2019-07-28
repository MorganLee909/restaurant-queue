from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
import datetime
from .models import Restaurant, Table
from apps.users.models import User

def newRestaurant(request):
    #Render the page to show form to create new restaurant
    return render(request, "restaurants/newRestaurant.html")

def createRestaurant(request):
    #POST
    if request.method == "POST":

        #Validate all data
        postData = request.POST.copy()
        postData["email"] = postData["email"].lower()
        errors = Restaurant.objects.validateRestaurant(postData)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/restaurants/new')

        #Create and add new restaurant to database
        newRestaurant = Restaurant(
            name = postData["name"],
            email = postData["email"],
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
        postData = request.POST.copy()
        postData["email"] = postData["email"].lower()
        errors = Restaurant.objects.validateLogin(postData)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/restaurants')

        #Log in restaurant
        restaurant = Restaurant.objects.get(email = postData["email"])
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
        "restaurant" : restaurant,
        "tables" : Table.objects.filter(restaurant = restaurant),
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
        postData = request.POST.copy()
        postData["email"] = postData["email"].lower()
        errors = Restaurant.objects.validateRestaurantEdit(postData)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/restaurants/{ restaurantId }/edit')

        #Update the data
        restaurantUpdate = Restaurant.objects.get(id=restaurantId)
        restaurantUpdate.name = postData["name"] or restaurant.name
        restaurantUpdate.email = postData["email"] or restaurant.email
        if request.POST["password"] != "":
            restaurantUpdate.password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        restaurantUpdate.save()
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

def createTables(request):
    #USER VALIDATION, WHO DO I WANT TO ALLOW ON THIS ROUTE?
    if "restaurant" not in request.session:
        messages.error(request, "You must be logged in to do that")
        return redirect(f"/restaurants")
    #POST
    if request.method == "POST":

        #Validate data
        errors = Table.objects.validateTable(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/restaurants/{request.session['restaurant']}/edit")

        #Create new table
        newTable = Table(
            name = request.POST["tableName"],
            size = int(request.POST["tableSize"]),
            restaurant = Restaurant.objects.get(id = request.session["restaurant"])
        )

        newTable.save()
        restaurant = Restaurant.objects.get(id = request.session["restaurant"])
        context = {
            "tables" : Table.objects.filter(restaurant = restaurant),
        }
        messages.success(request, f"Table '{newTable.name}' with Capacity of {newTable.size} successfully added to restaurant floor")

    #redirect to restaurant dashboard
    return redirect(f"/restaurants/{request.session['restaurant']}/edit", context)

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
    restaurant = Restaurant.objects.get(id = request.session["restaurant"])
    parties = User.objects.filter(restaurant = restaurant)
    print(parties)

    for party in parties:
        print("%" * 100)
        print(party.restaurant)
        difference = datetime.datetime.now() - party.time.replace(tzinfo = None)
        party.waitTime = round(int(difference.total_seconds()) / 60)

    context = {
        "restaurant" : restaurant,
        "tables" : Table.objects.filter(restaurant = restaurant),
        "parties" : parties
    }

    return render(request, "restaurants/dashboard.html", context)

def addParty(request):
    if request.method == "POST":
        postData = request.POST.copy()
        postData["partyEmail"] = postData["partyEmail"].lower()
        user = User.objects.get(email = postData["partyEmail"])
        user.restaurant = Restaurant.objects.get(id = request.session["restaurant"])
        user.time = datetime.datetime.now()
        user.partySize = postData["partySize"]
        user.save()

    return redirect("/restaurants/dashboard")

def assignTable(request, tableId):
    table = Table.objects.get(id = tableId)
    customers = User.objects.filter(restaurant = Restaurant.objects.get(id = request.session["restaurant"]))
    
    customer = findCorrectUser(customers, table.size)
    if customer == None:
        messages.success(request, "No parties to assign to this table")
        return redirect("/restaurants/dashboard")

    customer.restaurant = None
    customer.table = table
    customer.time = datetime.datetime.now()
    customer.save()

    messages.success(request, f"{customer.lastName} assigned to table {table.name}")
    return redirect("/restaurants/dashboard")

def removeParty(request, partyId):
    user = User.objects.get(id = partyId)
    user.restaurant = None
    user.table = None
    user.save()
    return redirect("/restaurants/dashboard")

def checkout(request, partyId):
    user = User.objects.get(id = partyId)
    user.restaurant = None
    user.table = None
    user.save()
    return redirect("/restaurants/dashboard")

#Not a route
def findCorrectUser(lineMembers, tableSize):
    correctMember = None
    for obj in lineMembers:
        if obj.partySize <= tableSize:
            if correctMember == None:
                correctMember = obj
            elif obj.time < correctMember.time:
                correctMember = obj

    return correctMember