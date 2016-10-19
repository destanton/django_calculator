from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Operation, Profile


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


def drop_down(num_input, choice, num_input2):
        if choice == "+":
            return int(num_input) + int(num_input2)
        elif choice == "-":
            return int(num_input) - int(num_input2)
        elif choice == "*":
            return int(num_input) * int(num_input2)
        elif choice == "/":
            return int(num_input) / int(num_input2)


class CreateView(CreateView):
    model = Operation
    success_url = "/"
    fields = ('num_1', "operator", "num_2")
