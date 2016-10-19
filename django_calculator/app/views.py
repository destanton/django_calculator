from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Operation, Profile


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"
#
#
# def drop_down(num_input, choice, num_input2):
#         if choice == "+":
#             return int(num_input) + int(num_input2)
#         elif choice == "-":
#             return int(num_input) - int(num_input2)
#         elif choice == "*":
#             return int(num_input) * int(num_input2)
#         elif choice == "/":
#             return int(num_input) / int(num_input2)


class CreateView(CreateView):
    model = Operation
    success_url = "/"
    fields = ('num_1', "operator", "num_2")

    def get_context_data(self):
        context = super().get_context_data()
        context["operation"] = Operation.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.operator = ''
        if instance.operator == "Addition":
            return instance.num_1 + instance.num_2
        elif instance.operator == "Subtract":
            return instance.num_1 - instance.num_2
        elif instance.operator == "Multiply":
            return instance.num_1 * instance.num_2
        elif instance.operator == "Divide":
            return instance.num_1 / instance.num_2
        return super().form_valid(form)
