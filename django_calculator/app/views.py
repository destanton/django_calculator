from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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


def index_view(request):
    # print(request.POST)
        # if request.GET != "" or request.GET == int:
        if request.GET:
            num_input = request.GET["num_input"]
            num_input2 = request.GET["num_input2"]
            operator = request.GET["operator"]
            print(request.GET)
        else:
            num_input = 1
            num_input2 = 1
            operator = "+"
        context = {
            "num": (num_input),
            "oper": (operator),
            "num2": (num_input2),
            "output": drop_down(num_input, operator, num_input2)
        }
        return render(request, "index.html", context)
