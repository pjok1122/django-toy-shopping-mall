from django.db import models

# Create your models here.
class Order(models.Model):
    #product.mdoels.Product --> product.Product로 생략가능
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="구매자")
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="상품")
    quantity = models.IntegerField(verbose_name = "수량")
    reg_date = models.DateField(auto_now_add=True, verbose_name="구매일자")

    def __str__(self):
        return (str(self.user) + ' ' + str(self.product))
    
    class Meta:
        db_table = 'orders'
        verbose_name = "주문"
        verbose_name_plural = "주문"
