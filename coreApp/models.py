from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255, null=True)
    postDate = models.DateField("дата и время публикации", default=datetime.now)
    postContent = models.TextField("Контент", null=True)
    postImage = models.TextField("Картинка", null=True)

    def __str__(self):
        return f'{self.title}. Date: {self.postDate}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Character(models.Model):
    name = models.CharField('Имя персонажа', max_length=255, null=True)
    characterDesc = models.TextField('Инфо', null=True)
    characterAge = models.IntegerField('Возраст', null=True)
    characteImage = models.TextField('Картинка', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
