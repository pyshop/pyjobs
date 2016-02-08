from django.db import models
from pyjobs2.settings import AUTH_USER_MODEL
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL)
    location = models.CharField(max_length=120, blank=True, null=True)
    # picture = ?
    # TODO не уверен что должны быть раздельные профайлы
    # может быть фулстак девелопер и себе ищет работу и сразу
    # предлагает студентам подработку
    # удобнее было бы управлять всем в одном профайле

    def __str__(self):
        return self.user.username
