from django.db import models

class Good(models.Model):
    GOODS_TYPE = [
        ("G", "Товар"),
        ("S", "Услуга")
    ]
    goods_name = models.CharField(max_length=35, primary_key=True, unique=True)
    goods_type = models.CharField(max_length=1, choices=GOODS_TYPE)
    rat = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.goods_name}, {self.goods_type}, {self.rat}, {self.price}'

class Client(models.Model):
    name = models.CharField(max_length=50, default="aaa")
    phone_number = models.IntegerField(unique=True)

    def publish(self):
        self.save()

    def __str__(self):
        return f'{self.name}, {self.phone_number}'


class Order(models.Model):
    goods_name = models.OneToOneField(Good, on_delete= models.CASCADE)
    # goods_name = models.CharField(max_length=35, primary_key=True, unique=True)
    amount = models.IntegerField()
    name = models.OneToOneField(Client, on_delete= models.CASCADE)
    # name = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return f'{self.goods_name}, {self.amount}, {self.name}'