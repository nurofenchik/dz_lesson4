from django.contrib import admin
from .models import Advertisement
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'title', 'description', 'price','auction' , 'created_date' , 'updated_date' ,  'image' , 'photo']
    list_filter = ['creates_at' ,'auction' ]
    actions = ['make_auction_as_false' , 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description','user','image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes' : ['collapse']
        }),


    )
    @admin.action(description= 'Убрать возможность торга')
    def make_auction_as_false(self, request , queryset):
        queryset.update(auction = False)
        self.update_with_last_modified_time(queryset)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
        self.update_with_last_modified_time(queryset)

admin.site.register(Advertisement, AdvertisementAdmin)