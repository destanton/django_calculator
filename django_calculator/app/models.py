from django.db import models


OPERATORS = [
    ('+', 'Addition'),
    ('-', 'Subract'),
    ('*', 'Multiply'),
    ('/', 'Divide')
]


class Operation(models.Model):
    created_by = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    num_1 = models.SmallIntegerField()
    operator = models.CharField(max_length=1, choices=OPERATORS)
    num_2 = models.SmallIntegerField()

    def __str__(self):
        return self.created_by.username


ACCESS_LEVEL = [
    ('o', 'Owner'),
    ('u', 'User')
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVEL)

    def __str__(self):
        return self.user.username
