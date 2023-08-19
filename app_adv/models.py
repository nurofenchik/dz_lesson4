from django.db import models

# Create your models here.
class Cats(models.Model):
    name = models.CharField(max_length=50),
    age = models.IntegerField(),
    breed = models.CharField(max_length=50)

class Advertisement(models.Model):
    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описвние',)
    price = models.DecimalField('Цена', max_digits=10 , decimal_places=2)
    auction = models.BooleanField('Торг', help_text="Отметьте,если торг уместен")
    creates_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'advertisement'
