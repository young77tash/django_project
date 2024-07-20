from django.db import models


class Articles(models.Model):
    title = models.CharField('Название Курса', max_length=50)
    anons = models.CharField('Анонс Курса', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'