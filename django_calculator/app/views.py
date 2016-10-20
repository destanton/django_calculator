from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView, DeleteView
from app.models import Operation, Profile


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class OperationCreateView(CreateView):
    model = Operation
    success_url = "/"
    fields = ('num_1', "operator", "num_2")

    def get_context_data(self):
        context = super().get_context_data()
        context["operation"] = Operation.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        # instance.operator = ''
        if instance.operator == "+":
            instance.answer = instance.num_1 + instance.num_2
        elif instance.operator == "-":
            instance.answer = instance.num_1 - instance.num_2
        elif instance.operator == "*":
            instance.answer = instance.num_1 * instance.num_2
        elif instance.operator == "/":
            instance.answer = instance.num_1 / instance.num_2
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation_detail"] = Operation.objects.all()
        return context

    def get_queryset(self):
        if self.request.user.profile.user.id:
            return Operation.objects.all()
        return Operation.objects.filter(created_by=self.request.user)


class ProfileCreateView(CreateView):
    model = Profile
    success_url = "/"
    fields = ('access_level', )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["operation_detail"] = Operation.objects.all()
    #     return context

    def get_queryset(self):
        if self.request.user.profile.user.id:
            return Operation.objects.all()
        return Operation.objects.filter(created_by=self.request.user)
