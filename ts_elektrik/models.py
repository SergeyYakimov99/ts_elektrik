from django.db import models


class Contacts(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    email = models.EmailField(verbose_name="email address", blank=True)
    land = models.CharField(verbose_name="Страна", max_length=50, unique=True)
    city = models.CharField(verbose_name="Город", max_length=50)
    street = models.CharField(verbose_name="Улица", max_length=100)
    house = models.CharField(verbose_name="Дом", max_length=10)


class Products(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    title = models.CharField(verbose_name="Наименование", max_length=100)
    brand = models.CharField(verbose_name="Брэнд", max_length=20, blank=True)
    release_date = models.DateTimeField(verbose_name="Дата выхода на рынок", blank=True)


"""
базовая модель, класс Basic с полями наименование, контакты ссылается (ForeignKey) на таблицу контакты, продукты 
ссылаются (ForeignKey) не таблицу продукты, сотрудники ссылается  (ForeignKey) на таблицу сотрудники, задолженность и 
дата создания. Отдельно модель класс Contact с полями email и адрес, который ссылается (ForeignKey) на таблицу адрес. 
Отдельно модель класс Address с полями страна, город, улица и номер дома. И отдельно модель класс Products с полями 
наименование, модель товара и дата выхода на рынок. Не знаю, может слишком заморочено получилось, как вы сделали?
Ну и модели завод, дистрибьютор, дилерский центр, крупная розничная сеть и индивидуальный предприниматель, которые 
наследуются от базовой модели. И здесь же я и ссылаюсь на поставщика.
"""


class BaseModel(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255, unique=True)
    contacts = models.ForeignKey(Contacts, verbose_name="Контакты", on_delete=models.PROTECT)
    products = models.ForeignKey(Products, verbose_name="Продукты", on_delete=models.PROTECT)
    # staff = models.ForeignKey(Staff, verbose_name="Сотрудники", on_delete=models.PROTECT)
    debt = models.FloatField(verbose_name="Задолженность")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


class Factory(BaseModel):
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class Retail_network(BaseModel):
    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    supplier = models.ForeignKey(Factory, verbose_name="Поставщик", on_delete=models.PROTECT)


class Sole_trader(BaseModel):
    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    supplier = models.ForeignKey(Retail_network, verbose_name="Поставщик", on_delete=models.PROTECT)
