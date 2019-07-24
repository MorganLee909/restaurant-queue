from django.db import models
import bcrypt
from apps.users.models import User, LineMember

class RestaurantManager(models.Manager):
    def validateRestaurant(self, restaurantData):
        errors = {}

        #Name
        if len(restaurantData["name"]) < 3:
            errors["nameLength"] = "Name of restaurant must contain at least 3 characters"
        elif len(restaurantData["name"]) > 254:
            errors["nameLength"] = "Name is too long"

        #Email
        if len(restaurantData["email"]) > 99:
            errors["emailLength"] = "All emails must be less than 100 characters"
        if Restaurant.objects.filter(email = restaurantData['email']):
            errors['emailInUse'] = 'Email address already in use.'

        #Password
        if len(restaurantData["password"]) < 8:
            errors["passwordlength"] = "Password must contain at least 8 characters"
        elif len(restaurantData["password"]) > 49:
            errors["passwordlength"] = "Password too long"

        if not any(char.isdigit() for char in restaurantData["password"]):
            errors["passwordNums"] = "Password must contain at least one number and one extra character"

        specChars = "!@#$%^&*()_-=+/><;:'][}{"
        if not any(char in specChars for char in restaurantData["password"]):
            errors["passwordNums"] = "Password must contain at least one number and one extra character"

        if restaurantData['password'] != restaurantData['passwordConfirm']:
            errors['notPassword'] = 'Password does not match.'

        return errors

    def validateLogin(self, restaurantData):
        errors = {}
        try: 
            restaurant = Restaurant.objects.get(email = restaurantData['email'])
        except:
            errors['email'] = f'No email matching {restaurantData["email"]}.'
            return errors

        if not bcrypt.checkpw(restaurantData["password"].encode(), restaurant.password.encode()):
            errors["password"] = "Password does not match email"

        return errors

    def validateRestaurantEdit(self, restaurantData):
        errors = {}

        #Name
        if len(restaurantData["name"]) < 3 and len(restaurantData["name"]) > 0:
            errors["nameLength"] = "Name of restaurant must contain at least 3 characters"
        elif len(restaurantData["name"]) > 254:
            errors["nameLength"] = "Name is too long"

        #Email
        if len(restaurantData["email"]) > 99:
            errors["emailLength"] = "All emails must be less than 100 characters"
        if Restaurant.objects.filter(email = restaurantData['email']):
            errors['emailInUse'] = 'Email address already in use.'

        #Password
        if len(restaurantData["password"]) < 8 and len(restaurantData["password"]) > 0:
            errors["passwordlength"] = "Password must contain at least 8 characters"
        elif len(restaurantData["password"]) > 49:
            errors["passwordlength"] = "Password too long"

        if len(restaurantData["password"]) > 0 and not any(char.isdigit() for char in restaurantData["password"]):
            errors["passwordNums"] = "Password must contain at least one number and one extra character"

        specChars = "!@#$%^&*()_-=+/><;:'][}{"
        if len(restaurantData["password"]) > 0 and not any(char in specChars for char in restaurantData["password"]):
            errors["passwordNums"] = "Password must contain at least one number and one extra character"

        if restaurantData['password'] != restaurantData['passwordConfirm']:
            errors['notPassword'] = 'Password does not match.'

        return errors

    def validateTable(self, tableData):
        errors = {}

        #Name
        if len(tableData["tableName"]) > 49:
            errors["nameLength"] = "Name must be less than 50 characters"
        
        #Size
        try:
            size = int(tableData["tableSize"])
        except ValueError:
            errors["sizeNotInt"] = "Must enter an integer for size"
        
            if size < 1:
                errors["sizeTooSmall"] = "Size of table must be 1 or greater"

        return errors

class Restaurant(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    line = models.ManyToManyField(LineMember, related_name = "restaurant")
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    objects = RestaurantManager()

class Table(models.Model):
    name = models.CharField(max_length = 50)
    size = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, related_name = "tables")
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    objects = RestaurantManager()