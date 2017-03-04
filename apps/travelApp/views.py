from django.shortcuts import render, redirect
from django.contrib import messages
from ..loginApp.models import User
from .models import Planner
from datetime import datetime

# Create your views here.
def index(request):

    if not 'user_id' in request.session:
        messages.error(request, 'Must be logged in to continue!')
        return redirect('users:index')

    user = User.objects.get(id=request.session['user_id'])

    context = {
        # "curDate": datetime.now().date(),

        "yourPlanLists": user.plans.all(),
        # "yourPlanLists": Planner.objects.filter(users=user),

        # 'wishList': user.wishlists.all(),
        'othersPlans': Planner.objects.exclude(users=user),
        'user': user
    }
    return render(request, "travelApp/index.html", context)

def addTravelPlan(request):

    if not 'user_id' in request.session:
        messages.error(request, 'Must be logged in to continue!')
        return redirect('users:index')

    return render(request, "travelApp/newPlan.html")

def newPlan(request):
    if request.method == "POST":
        userID = request.session['user_id']
        # user = User.objects.get(id=userID)
        responseFromModel = Planner.objects.addPlan(request.POST, userID)

        if responseFromModel['status']:
            # created a user, send to success page

            return redirect('travels:travelPlanPage')
        # failed validations send messages to client
        else:
            for error in responseFromModel['errors']:
                messages.error(request, error)
            return redirect('travels:addTravel')

    return redirect("travels:travelPlanPage")

def show(request, id):

    if not 'user_id' in request.session:
        messages.error(request, 'Must be logged in to continue!')
        return redirect('users:index')

    wish_id = id
    context = {
        "itemInfo" : Planner.objects.get(id=id),
        "otherUsersList" : User.objects.filter(plans__id=wish_id)
    }
    return render(request, "travelApp/show.html", context)

def add(request, id):
    wish = Planner.objects.get(id=request.POST['wish_id'])
    user = User.objects.get(id=request.session['user_id'])
    user.plans.add(wish)
    return redirect("travels:travelPlanPage")
