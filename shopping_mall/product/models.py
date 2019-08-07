from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name ="상품명")
    price = models.IntegerField(verbose_name="가격")
    description = models.TextField(verbose_name="설명")
    stock = models.IntegerField(verbose_name="재고")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name = "등록시간")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"
        verbose_name="상품"
        verbose_name_plural = "상품"