from django.db import models
#Модель для города
class City(models.Model):
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    name = models.CharField(max_length=100, null=False,blank=False)

    def __str__(self):
        return self.name

#модель для улиц
class Street(models.Model):
    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'

    name = models.CharField(max_length=100, null=False,blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return self.name

#Модель для магазинов
class Shop(models.Model):
    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    name = models.CharField(null=False,blank=False,max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=False,blank=False)
    street = models.ForeignKey(Street, on_delete=models.CASCADE,null=False,blank=False)
    house =  models.CharField(null=False,blank=False,max_length=50)
    opening_time = models.TimeField()
    closing_time=models.TimeField()
    
    def __str__(self):
        return self.name

    
