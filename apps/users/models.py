from django.db import models
from apps.restaurants.models import LineMember
import bcrypt

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

class User(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    line = models.ForeignKey(LineMember, related_name='member', null=True)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    objects = DataManager()