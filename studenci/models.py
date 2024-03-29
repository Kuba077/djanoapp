from django.db import models

class Uczelnia(models.Model):
    nazwa = models.CharField(
        verbose_name='uczelnia',
        max_length=30,
        help_text='Nazwa uczelni')

    class Meta:
        verbose_name_plural = "uczelnie"

class Miasto(models.Model):
    nazwa = models.CharField(
        verbose_name='miasto',
        max_length=30,
        help_text='Nazwa miasta')
    kod = models.CharField(
        max_length=6,
        help_text='Kod pocztowy')

    class Meta:
        verbose_name_plural = "miasta"

class Student(models.Model):
    imie = models.CharField('imię', max_length=30)
    nazwisko = models.CharField(max_length=30)
    uczelnia = models.ForeignKey(Uczelnia, on_delete=models.SET_NULL, null=True)
    miasto = models.ForeignKey(Miasto, on_delete=models.SET_NULL, null=True)
    roks = models.CharField('rok studiów', max_length=3, blank=True, default='')
    dochod = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "studenci"