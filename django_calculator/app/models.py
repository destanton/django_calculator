from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


OPERATORS = [
    ('+', '+'),
    ('-', '-'),
    ('*', '*'),
    ('/', '/')
]


class Operation(models.Model):
    created_by = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    num_1 = models.SmallIntegerField()
    operator = models.CharField(max_length=1, choices=OPERATORS, default='+')
    num_2 = models.SmallIntegerField()
    answer = models.SmallIntegerField()

    def __str__(self):
        return self.created_by.username

    @property
    def get_answer(self):
        return "{} {} {} = {}".format(self.num_1, self.operator, self.num_2, self.answer)

    class Meta:
        ordering = ("-created", )

    @property
    def is_owner(self):
        return self.access_level == 'o'

ACCESS_LEVEL = [
    ('o', 'Owner'),
    ('u', 'User')
]


# @receiver(post_save, sender='auth.User')
# def create_user_profile(**kwargs):
#     created = kwargs.get('created')
#     instance = kwargs.get('instance')
#     if created:
#         Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVEL, default='u')

    def __str__(self):
        return self.user.username

    @property
    def is_owner(self):
        return self.access_level == 'o'
