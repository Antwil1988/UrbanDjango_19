from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    # Используем PositiveIntegerField, чтобы возраст был неотрицательным
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    # добавление метода __str__ может улучшить читаемость объектов модели


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(
        'Buyer', related_name='games')  # Связь с моделью Buyer

    def __str__(self):
        return self.title
