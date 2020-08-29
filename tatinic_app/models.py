from django.db import models


class Passenger(models.Model):
    PassengerId = models.CharField(max_length = 100)
    Survived = models.CharField(max_length = 100)
    Pclass = models.CharField(max_length = 100)
    Name = models.CharField(max_length = 100)
    Sex = models.CharField(max_length = 100)
    Age = models.CharField(max_length = 100, blank =True)
    SibSp = models.CharField(max_length = 100)
    Parch = models.CharField(max_length = 100)
    Ticket = models.CharField(max_length = 100)
    Fare = models.CharField(max_length = 100)
    Cabin = models.CharField(max_length = 100)
    Embarked = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.Name} ---- {self.Age}"