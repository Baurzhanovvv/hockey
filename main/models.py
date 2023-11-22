from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class Player(models.Model):
    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

    first_name = models.CharField('Имя', max_length=256)
    second_name = models.CharField('Фамилия', max_length=256)
    surname = models.CharField('Отчество', max_length=256)
    birth_date = models.DateField('Дата рождения')
    image = models.ImageField(upload_to='media/players/', null=True)
    address = models.CharField(max_length=256)
    identificator = models.CharField('ИИН', max_length=12)
    email = models.EmailField(max_length=256)
    phone_number = models.CharField(max_length=11)

    @property
    def img_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""

    @property
    def img_preview2(self):
        if self.image:
            return mark_safe(
                '<img src="{}" width="70" height="70" style="transform: scale(1); transition: transform 0.3s;" onmouseover="this.style.transform=\'scale(1.7)\'" onmouseout="this.style.transform=\'scale(1)\'" />'.format(self.image.url)
            )
        return ""


    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.identificator}'


class Competition(models.Model):
    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"

    name = models.CharField('Название', max_length=256)

    def __str__(self):
        return self.name


class Stage(models.Model):
    class Meta:
        verbose_name = "Стадия"
        verbose_name_plural = "Стадий"

    name = models.CharField('Название', max_length=256)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'

    name = models.CharField('Название', max_length=256)
    comp = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StructureTournament(models.Model):
    class Meta:
        verbose_name = 'Структура Турнира'
        verbose_name_plural = 'Структура Турниров'

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    def __str__(self):
        return self.tournament.name


class Calendar(models.Model):
    class Meta:
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календари'

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.tournament.name


class Teams(models.Model):
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    name = models.CharField('Название', max_length=256)

    def __str__(self):
        return self.name


class Match(models.Model):
    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'

    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    teams_in = models.ManyToManyField(Teams)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


class Structure(models.Model):
    class Meta:
        verbose_name = 'Состав на матч'
        verbose_name_plural = 'Составы на матчи'

    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    player = models.ManyToManyField(Player)

    def __str__(self):
        return str(self.calendar.pk)


class Connect(models.Model):
    class Meta:
        verbose_name = 'Привязка команды'
        verbose_name_plural = 'Привязка команд'

    teams = models.ManyToManyField(Teams)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.calendar.pk)

