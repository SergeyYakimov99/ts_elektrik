from django.db import models


class Contacts(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    email = models.EmailField(verbose_name="email address", blank=True, unique=True)
    land = models.CharField(verbose_name="Страна", max_length=50)
    city = models.CharField(verbose_name="Город", max_length=50)
    street = models.CharField(verbose_name="Улица", max_length=100)
    house = models.CharField(verbose_name="Дом", max_length=10)

    def __str__(self):
        return self.email


class Products(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    title = models.CharField(verbose_name="Наименование", max_length=100)
    brand = models.CharField(verbose_name="Брэнд", max_length=20, blank=True)
    release_date = models.DateField(verbose_name="Дата выхода на рынок", blank=True)

    def __str__(self):
        return self.title


"""
базовая модель, класс BaseModel с полями: 
наименование, контакты - (ForeignKey) на таблицу контакты, продукты - (ForeignKey) не таблицу продукты, 
задолженность и дата создания. 
"""


class BaseModel(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255, unique=True)
    contacts = models.ForeignKey(Contacts, verbose_name="Контакты", on_delete=models.PROTECT)
    products = models.ForeignKey(Products, verbose_name="Продукты", on_delete=models.PROTECT)
    debt = models.FloatField(verbose_name="Задолженность")
    created = models.DateField(auto_now_add=True, verbose_name="Дата создания")


""" Модель завода на основе базовой """


class Factory(BaseModel):
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return self.title


""" Модель розничной сети на основе базовой """


class Retail_network(BaseModel):
    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    supplier = models.ForeignKey(Factory, verbose_name="Поставщик", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


""" Модель ИП на основе базовой """


class Sole_trader(BaseModel):
    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    supplier = models.ForeignKey(Retail_network, verbose_name="Поставщик", on_delete=models.PROTECT)

    def __str__(self):
        return self.title
