from django.db import models
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

    def validateLineMember(self, lineMemberData):
        errors = {}

        #Email
        try:
            user = User.objects.get(email = lineMemberData["partyEmail"])
        except:
            errors["noUser"] = f"User does not exist for {lineMemberData['partyEmail']}"
            return errors

        #Party size
        try:
            int(lineMemberData["partySize"])
        except ValueError:
            errors["notNumber"] = "Must enter an integer"

        #Uniqueness
        if hasattr(user, "line"):
            errors["inLine"] = "User is already in a line"

        return errors

class User(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    objects = DataManager()

class LineMember(models.Model):
    joined = models.DateTimeField(auto_now_add = True)
    partySize = models.IntegerField()
    member = models.OneToOneField(User, related_name = "line", null = True)
    objects = DataManager()

class SeatedUser(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    member = models.OneToOneField(User, related_name = "seatUser", null = True)
    objects = DataManager()