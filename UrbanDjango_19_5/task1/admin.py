from django.contrib import admin
from .models import Buyer, Game, News

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'balance', 'age')  # Поля, которые будут отображаться в списке объектов
    search_fields = ('name',)  # Поля, по которым можно будет искать объекты
    list_filter = ('balance', 'age')  # Поля, по которым можно будет фильтровать объекты
    list_per_page = 30  # Ограничение количества записей до 30
    readonly_fields = ('balance',)  # Поле, доступное только для чтения
    

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    search_fields = ('title',)
    list_filter = ('size', 'cost')
    list_per_page = 20 

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    search_fields = ('title', 'content')
    list_filter = ('date',)
