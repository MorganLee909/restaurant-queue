from django.db import models

class DataManager(models.Manager):
    def validateUser(self, userData):
        errors = {}

        #First Name
        if len(userData["firstName"]) < 3:
            errors["firstNameLength"] = "First name must contain at least 3 characters"
        elif len(userData["firstName"]) > 49:
            errors["firstNameLength"] = "First name must contain less than 50 characters"

        #Last name
        if len(userData["lastName"]) < 3:
            errors["lastNameLength"] = "Last name must contain at least 3 characters"
        elif len(userData["firstName"]) > 49:
            errors["lastNameLength"] = "Last name must contain less than 50 characters"

        #Email
        if len(userData["email"]) > 99:
            errors["emailLength"] = "All emails must be less than 100 characters"

        #Password
        if len(userData["password"]) < 8:
            errors["passwordlength"] = "Password must contain at least 8 characters"
        elif len(userData["password"]) > 49:
            errors["passwordlength"] = "Password too long"

        if not any(char.isdigit() for char in userData["password"]):
            errors["passwordNums"] = "Password must contain at least one number and one extra character"

        specChars = "!@#$%^&*()_-=+/><;:'][}{"
        if not any(char in specChars for char in userData["password"]):
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

class User(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    objects = DataManager()

class Restaurant(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    objects = DataManager()

class Table(models.Model):
    name = models.CharField(max_length = 50)
    size = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, related_name = "tables")
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    objects = DataManager()