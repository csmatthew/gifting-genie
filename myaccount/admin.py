from django.contrib import admin
from .models import MyAccount

# Register your models here.
class MyAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'updated_on')
    search_fields = ('user__username', 'title')
    list_filter = ('updated_on',)
    ordering = ('-updated_on',)

admin.site.register(MyAccount, MyAccountAdmin)