from django.db import models
from accounts.models import User


class Advert(models.Model):
    class Meta:
        verbose_name = "объявление"
        verbose_name_plural = "объявления"

    title = models.CharField(verbose_name="название вакансии", max_length=120, blank=False,
                             help_text="название вакансии, например, 'требуется самый лучший питонист'")
    description = models.TextField(verbose_name="описание вакансии", blank=True)
    requirements = models.TextField(verbose_name="требования к соискателю", blank=True)
    salary = models.CharField(verbose_name="зарплата", blank=False, max_length=120,
                              help_text="сумма цифрами или, например, по договоренности")
    city = models.CharField(verbose_name="город", blank=False, max_length=120,
                            help_text="", null=True)
    is_remote = models.BooleanField(verbose_name="удаленно", default=False)
    timestamp = models.DateTimeField(verbose_name="дата публикации", auto_now=False,
                                     auto_now_add=True, null=True)
    author = models.ForeignKey(User, verbose_name='автор вакансии', blank=True, null=True)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'advert_detail', (self.pk,)
