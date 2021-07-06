from django.db import models
from django.contrib.auth.models import User, auth


# Create your models here.
class TeachersDetails(models.Model):
    Firstname=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=20)
    Experience=models.CharField(max_length=50)

class StudentFeedback(models.Model):
    Name_of_The_Teacher=models.CharField(max_length=20)
    Subject=models.CharField(max_length=30)
    Punctuality=models.CharField(max_length=30)
    Portion_Completion=models.CharField(max_length=30)
    Doubt_Clearing=models.CharField(max_length=30)
    Other_Comments=models.CharField(max_length=200)



class register_table(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    phone_number = models.CharField(max_length=12)

    def _str_(self):
        return self.user.username

    

    





