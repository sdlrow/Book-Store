# import json
# from django.http import JsonResponse
# from django.core import serializers
# from .models import *
# from django.views.decorators.csrf import csrf_exempt
#
#
# def createUser(request):
#
#     # def get(self, request, *args, **kwargs):
#     #     form = RegistrationForm(request.POST or None)
#     #     books = Book.objects.all()
#     #     context = {'form': form, 'books': books, 'cart': self.cart}
#     #     return render(request, 'registration.html', context)
#     #
#     # if request.method == "POST":
#     #
#     #     new_user = form.save(commit=False)
#     #     new_user.username = form.cleaned_data['username']
#     #     new_user.first_name = form.cleaned_data['first_name']
#     #     new_user.last_name = form.cleaned_data['last_name']
#     #     new_user.email = form.cleaned_data['email']
#     #     new_user.save()
#     #     new_user.set_password(form.cleaned_data['password'])
#     #     new_user.save()
#     #     customer = Customer(email=form.cleaned_data['email'], user=new_user)
#     #     cart = Cart.objects.filter(owner=customer).first()
#     #     if not cart:
#     #         cart = Cart.objects.create(owner=customer)
#     #     customer.save()
#     #     # Customer.objects.create(
#     #     #     user=new_user
#     #     # )
#     #     user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#     #     login(request, user)
#
#     respData = {}
#     if request.method == "POST":
#         newUserData = json.loads(request.body)
#         user = User.objects.create_user(
#             first_name=newUserData['first_name'],
#             last_name=newUserData['last_name'],
#             password=newUserData['password'],
#             username=newUserData['username']
#         )
#         customer = Customer(email=newUserData['email'], user=user)
#         cart = Cart.objects.filter(owner=customer).first()
#         if not cart:
#             cart = Cart.objects.create(owner=customer)
#         user.save()
#         customer.save()
#         cart.save()
#         respData['msg'] = "User has been successfully created!"
#         respData['userInfo'] = str(
#             user.first_name) + " " + str(user.last_name) + " (" + str(user.id) + ")"
#         respData['userId'] = str(user.id)
#     else:
#         respData['msg'] = "Oops! Something went wrong!"
#     return JsonResponse(respData, safe=False)
#
#
# def updateUser(request):
#     print("sdfsdfsdfsdfsdfsdf")
#     respData = {}
#     if request.method == "POST":
#         # newUserData = json.loads(request.body)
#         user = User.objects.get(username=newUserData['username'])
#         user.first_name = newUserData['first_name']
#         user.last_name = newUserData['last_name']
#         user.email = newUserData['email']
#         user.password = newUserData['password']
#         # user.player.age = newUserData['age']
#         # user.player.is_senior = True if newUserData['is_senior'].lower(
#         # ) == 'true' else False
#         # user.player.country = newUserData['country']
#         # user.player.balance = newUserData['balance']
#         # user.date_joined = newUserData['date_joined']
#         # user.player.with_amount = newUserData['with_amount']
#         # user.player.hotel_room = newUserData['hotel_room']
#         # user.player.username = newUserData['username']
#         # user.player.insurance = True if newUserData['insurance'].lower(
#         # ) == 'true' else False
#         customer = Customer(email=newUserData['email'], user=user)
#         cart = Cart.objects.filter(owner=customer).first()
#         if not cart:
#             cart = Cart.objects.create(owner=customer)
#         user.save()
#         customer.save()
#         cart.save()
#         respData['msg'] = "User data has been successfully updated!"
#     else:
#         respData['msg'] = "Oops! Something went wrong!"
#     return JsonResponse(respData, safe=False)
#
#
# def getUserDataById(request):
#     user = User.objects.get(username=request.POST['username'])
#     customer = Customer(user=user)
#     serialized_obj = serializers.serialize('json', [user, customer.user])
#     return JsonResponse(serialized_obj, safe=False)
#
#
# def deleteUser(request):
#     user = User.objects.get(id=request.POST['user_id'])
#     user.player.delete()
#     user.delete()
#     data = {
#         "msg": "User has been succesfully deleted"
#     }
#     return JsonResponse(data=data, safe=False)
#
#
# def updateBalance(request):
#     user = User.objects.get(id=int(request.POST['userId']))
#     data = {
#         "user": {
#             "fname": user.first_name,
#             "lname": user.last_name,
#             "balance": user.player.balance
#         },
#         "balanceChange": request.POST['balanceDifference'],
#         "newBalance": int(request.user.player.balance) + int(request.POST['balanceDifference'])
#     }
#     user.player.balance += int(request.POST['balanceDifference'])
#     if int(request.POST['balanceDifference']) > 0:
#         user.player.win += int(request.POST['balanceDifference'])
#     else:
#         user.player.lost += int(request.POST['balanceDifference'])
#     user.save()
#     user.player.save()
#     return JsonResponse(data=data, safe=False)
#
#
# ################################################################
#
#
#
# # def createBook(request):
#
#     # def get(self, request, *args, **kwargs):
#     #     form = RegistrationForm(request.POST or None)
#     #     books = Book.objects.all()
#     #     context = {'form': form, 'books': books, 'cart': self.cart}
#     #     return render(request, 'registration.html', context)
#     #
#     # if request.method == "POST":
#     #
#     #     new_user = form.save(commit=False)
#     #     new_user.username = form.cleaned_data['username']
#     #     new_user.first_name = form.cleaned_data['first_name']
#     #     new_user.last_name = form.cleaned_data['last_name']
#     #     new_user.email = form.cleaned_data['email']
#     #     new_user.save()
#     #     new_user.set_password(form.cleaned_data['password'])
#     #     new_user.save()
#     #     customer = Customer(email=form.cleaned_data['email'], user=new_user)
#     #     cart = Cart.objects.filter(owner=customer).first()
#     #     if not cart:
#     #         cart = Cart.objects.create(owner=customer)
#     #     customer.save()
#     #     # Customer.objects.create(
#     #     #     user=new_user
#     #     # )
#     #     user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#     #     login(request, user)
#
#     # respData = {}
#     # if request.method == "POST":
#     #     newUserData = json.loads(request.body)
#     #     user = User.objects.create_user(
#     #         first_name=newUserData['first_name'],
#     #         last_name=newUserData['last_name'],
#     #         password=newUserData['password'],
#     #         username=newUserData['username']
#     #     )
#     #     player.user = user
#     #     player.age = newUserData['age']
#     #     player.is_senior = True if newUserData['is_senior'].lower(
#     #     ) == 'true' else False
#     #     player.country = newUserData['country']
#     #     player.balance = newUserData['balance']
#     #     player.with_amount = newUserData['with_amount']
#     #     player.hotel_room = newUserData['hotel_room']
#     #     player.win = 0
#     #     player.lost = 0
#     #     player.insurance = True if newUserData['insurance'].lower(
#     #     ) == 'true' else False
#     #     player.save()
#     #     respData['msg'] = "User has been successfully created!"
#     #     respData['userInfo'] = str(
#     #         user.first_name) + " " + str(user.last_name) + " (" + str(user.id) + ")"
#     #     respData['userId'] = str(user.id)
#     # else:
#     #     respData['msg'] = "Oops! Something went wrong!"
#     # return JsonResponse(respData, safe=False)
#
#
# def updateBook(request):
#     print("sdfsdfsdfsdfsdfsdf")
#     respData = {}
#     if request.method == "POST":
#         newUserData = json.loads(request.body)
#         user = User.objects.get(username=newUserData['username'])
#         user.first_name = newUserData['first_name']
#         user.last_name = newUserData['last_name']
#         user.last_name = newUserData['email']
#         user.password = newUserData['password']
#         # user.player.age = newUserData['age']
#         # user.player.is_senior = True if newUserData['is_senior'].lower(
#         # ) == 'true' else False
#         # user.player.country = newUserData['country']
#         # user.player.balance = newUserData['balance']
#         # user.date_joined = newUserData['date_joined']
#         # user.player.with_amount = newUserData['with_amount']
#         # user.player.hotel_room = newUserData['hotel_room']
#         # user.player.username = newUserData['username']
#         # user.player.insurance = True if newUserData['insurance'].lower(
#         # ) == 'true' else False
#         customer = Customer(email=newUserData['email'], user=user)
#         cart = Cart.objects.filter(owner=customer).first()
#         if not cart:
#             cart = Cart.objects.create(owner=customer)
#         user.save()
#         customer.save()
#         respData['msg'] = "User data has been successfully updated!"
#     else:
#         respData['msg'] = "Oops! Something went wrong!"
#     return JsonResponse(respData, safe=False)
#
#
# def getBookDataByName(request):
#     book = Book.objects.get(name=request.POST['name'])
#     serialized_obj = serializers.serialize('json', [book])
#     return JsonResponse(serialized_obj, safe=False)
#
#
# def deleteBook(request):
#     user = User.objects.get(id=request.POST['user_id'])
#     user.player.delete()
#     user.delete()
#     data = {
#         "msg": "User has been succesfully deleted"
#     }
#     return JsonResponse(data=data, safe=False)
#
#
# def updateBook(request):
#     user = User.objects.get(id=int(request.POST['userId']))
#     data = {
#         "user": {
#             "fname": user.first_name,
#             "lname": user.last_name,
#             "balance": user.player.balance
#         },
#         "balanceChange": request.POST['balanceDifference'],
#         "newBalance": int(request.user.player.balance) + int(request.POST['balanceDifference'])
#     }
#     user.player.balance += int(request.POST['balanceDifference'])
#     if int(request.POST['balanceDifference']) > 0:
#         user.player.win += int(request.POST['balanceDifference'])
#     else:
#         user.player.lost += int(request.POST['balanceDifference'])
#     user.save()
#     user.player.save()
#     return JsonResponse(data=data, safe=False)


import json
from django.http import JsonResponse
from django.core import serializers
from .models import *
from django.views.decorators.csrf import csrf_exempt


def createUser(request):
    respData = {}
    if request.method == "POST":
        newUserData = json.loads(request.body)
        user = User.objects.create_user(
            first_name=newUserData['first_name'],
            last_name=newUserData['last_name'],
            email=newUserData['email'],
            password=newUserData['password'],
            username=newUserData['username']
        )
        customer = Customer(email=newUserData['email'], user=user)
        cart = Cart.objects.filter(owner=customer).first()
        if not cart:
            cart = Cart.objects.create(owner=customer)
        customer.save()
        cart.save()
        respData['msg'] = "User has been successfully created!"
        respData['userInfo'] = str(
            user.first_name) + " " + str(user.last_name) + " (" + str(user.id) + ")"
        respData['userId'] = str(user.id)
    else:
        respData['msg'] = "Oops! Something went wrong!"
    return JsonResponse(respData, safe=False)


def updateUser(request):
    respData = {}
    if request.method == "POST":
        print("asdsd")
        newUserData = json.loads(request.body)
        user = User.objects.get(username=newUserData['username'])
        user.username = newUserData['username']
        user.first_name = newUserData['first_name']
        user.last_name = newUserData['last_name']
        user.email = newUserData['email']
        user.password = newUserData['password']
        user.save()

        respData['msg'] = "User data has been successfully updated!"
    else:
        respData['msg'] = "Oops! Something went wrong!"
    return JsonResponse(respData, safe=False)


def getUserDataById(request):
    user = User.objects.get(id=request.POST['user_id'])
    serialized_obj = serializers.serialize('json', [user])
    return JsonResponse(serialized_obj, safe=False)


def deleteUser(request):
    user = User.objects.get(id=request.POST['user_id'])
    customer = Customer.objects.get(user=user)
    cart = Cart.objects.create(owner=customer)
    cart.delete()
    customer.delete()
    user.delete()
    data = {
        "msg": "User has been succesfully deleted"
    }
    return JsonResponse(data=data, safe=False)


def updateBalance(request):
    user = User.objects.get(id=int(request.POST['userId']))
    data = {
        "user": {
            "fname": user.first_name,
            "lname": user.last_name,
            "balance": user.player.balance
        },
        "balanceChange": request.POST['balanceDifference'],
        "newBalance": int(request.user.player.balance) + int(request.POST['balanceDifference'])
    }
    user.player.balance += int(request.POST['balanceDifference'])
    if int(request.POST['balanceDifference']) > 0:
        user.player.win += int(request.POST['balanceDifference'])
    else:
        user.player.lost += int(request.POST['balanceDifference'])
    user.save()
    user.player.save()
    return JsonResponse(data=data, safe=False)
