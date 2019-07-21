from django.db import models

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

        return errors

    def validateTable(self, tableData):
        errors = {}

        #Name
        if len(tableData["name"]) > 49:
            errors["nameLength"] = "Name must be less than 50 characters"
        
        #Size
        try:
            size = int(tableData["size"])
        except ValueError:
            errors["sizeNotInt"] = "Must enter an integer for size"
        
            if size < 1:
                errors["sizeTooSmall"] = "Size of table must be 1 or greater"

        return errors  

class Restaurant(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
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