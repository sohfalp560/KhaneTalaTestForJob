from django.contrib import admin
from .models import User, Transaction


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("user", "id", "status", "price_per_gram")
    readonly_fields = ("gold_weight_gram", "date")
