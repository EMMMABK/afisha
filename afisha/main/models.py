from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField('Название:', max_length=50)
    description = models.TextField('Информация про фильм')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Director(models.Model):
    name = models.CharField('Имя режиссёра:', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"



class Review(models.Model):
    text = models.CharField('Отзывы:', max_length=100)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Предосмотр'
        verbose_name_plural = 'Предосмотры'
