from django.db import models
import bcrypt
from apps.restaurants.models import Restaurant, Table

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
        if User.objects.filter(email = userData['email']):
            errors['emailInUse'] = 'Email address already in use.'

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

        if userData['password'] != userData['confirm']:
            errors['notPassword'] = 'Password does not match.'

        return errors

    def validateLogin(self, postData):
        errors = {}
        try: 
            user = User.objects.get(email = postData['email'])
        except:
            errors['email'] = f'No email matching {postData["email"]}.'
            return errors

        if not bcrypt.checkpw(postData["password"].encode(), user.password.encode()):
            errors["password"] = "Password does not match email"

        return errors

    def validateUserEdit(self, userData):
        errors = {}

        #First Name
        if len(userData["firstName"]) < 3 and len(userData['firstName']) > 0:
            errors["firstNameLength"] = "First name must contain at least 3 characters"
        elif len(userData["firstName"]) > 49:
            errors["firstNameLength"] = "First name must contain less than 50 characters"

         #Last name
        if len(userData["lastName"]) < 3 and len(userData["lastName"]) > 0:
            errors["lastNameLength"] = "Last name must contain at least 3 characters"
        elif len(userData["firstName"]) > 49:
            errors["lastNameLength"] = "Last name must contain less than 50 characters"

        #Email
        if len(userData["email"]) > 99:
            errors["emailLength"] = "All emails must be less than 100 characters"
        if User.objects.filter(email = userData['email']):
            errors['emailInUse'] = 'Email address already in use.'

        #Password
        if len(userData["password"]) < 8 and len(userData["password"]) > 0:
            errors["passwordlength"] = "Password must contain at least 8 characters"
        elif len(userData["password"]) > 49:
            errors["passwordlength"] = "Password too long"

        if len(userData["password"]) > 0 and not any(char.isdigit() for char in userData["password"]):
            errors["passwordNums"] = "Password must contain at least one number and one extra character"

        specChars = "!@#$%^&*()_-=+/><;:'][}{"
        if len(userData["password"]) > 0 and not any(char in specChars for char in userData["password"]):
            errors["passwordNums"] = "Password must contain at least one number and one extra character"

        if userData['password'] != userData['confirm']:
            errors['notPassword'] = 'Password does not match.'
        
        return errors

class User(models.Model):
    firstName = models.CharField(max_length = 50, null = True)
    lastName = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100, null = True)
    password = models.CharField(max_length = 50, null = True)
    time = models.DateTimeField(null = True)
    partySize = models.IntegerField(default = 0)
    isTemp = models.BooleanField()
    restaurant = models.ForeignKey(
        Restaurant, 
        related_name = "user",
        null = True,
        on_delete = models.SET_NULL
    )
    table = models.OneToOneField(
        Table,
        related_name = "user",
        null = True,
        on_delete = models.SET_NULL
    )
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    objects = DataManager()