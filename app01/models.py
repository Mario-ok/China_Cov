from django.db import models
# Create your models here.
class App01Cities(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=10,null=True)
    date = models.DateField(auto_now=True,null=True)
    class Meta:
        db_table = 'city'

class App01Detail(models.Model):
    city = models.ForeignKey(App01Cities,on_delete=models.CASCADE)
    updateDate = models.DateField()
    diagnosis = models.IntegerField()
    cure = models.IntegerField()
    dead = models.IntegerField()
    new_diagnosis = models.IntegerField()
    class Meta:
        db_table = 'city_detail'

class App01News(models.Model):
    title = models.CharField(max_length=100,null=True)
    url = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=25,null=True)
    class Meta:
        db_table = 'news'
