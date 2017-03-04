from __future__ import unicode_literals
from ..loginApp.models import User
from django.db import models
import re
from datetime import datetime, date

class PlannerManager(models.Manager):

    def addPlan(self, postData, userID):
        errors = []
        modelResponse = {}

        if len(postData['destination']) == 0 :
            errors.append('Destination can not be empty!')
        elif len(postData['destination']) < 3:
            errors.append('Destination must be at least 3 charactor long!')

        if len(postData['description']) == 0 :
            errors.append('Description can not be empty!')
        elif len(postData['description']) < 3:
            errors.append('Description must be at least 3 charactor long!')

        if len(postData['trDateFrom']) < 1:
            errors.append('Travel Date From must be selected!')
        if len(postData['trDateTo']) < 1:
            errors.append('Travel Date To must be selected!')
        if len(errors) == 0:
            travelDatesFrom = datetime.strptime(postData['trDateFrom'], '%Y-%m-%d').date()
            if travelDatesFrom < datetime.now().date():
                errors.append('Please select current or future date!')


            userTravel = self.filter(trDateFrom = postData['trDateTo'])
            if userTravel:
                errors.append('End date can not be same as start date!')


        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors

        # else create
        else:
            user = User.objects.get(id=userID)
            plan = Planner.objects.create(destination = postData['destination'], description = postData['description'], trDateFrom = postData['trDateFrom'], trDateTo = postData['trDateTo'], creator = user)
            user.plans.add(plan)

            print postData['destination']

            modelResponse['status'] = True

        return modelResponse



# Create your models here.
class Planner(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    trDateFrom = models.DateField()
    trDateTo = models.DateField()
    users = models.ManyToManyField(User, related_name="plans")
    creator = models.ForeignKey(User, related_name = 'created_plans')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = PlannerManager()
