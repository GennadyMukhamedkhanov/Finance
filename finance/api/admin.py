from django.contrib import admin

from api.models import User, Transaction


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'registration_date',)
    ordering = ('registration_date',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'type', 'category')
    ordering = ('date',)