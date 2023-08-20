from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
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

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.creates_at.date() == timezone.now().date():
            created_time = self.creates_at.time().strftime("%H:%M:%S")
            return format_html("<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time)
        return self.creates_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Дата обновления")
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html("<span style='color: blue; font-weight: bold;'>Сегодня в {}</span>", updated_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    class Meta:
        db_table = 'advertisement'
