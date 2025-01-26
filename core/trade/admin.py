from django.contrib import admin
from .models import User, Transaction

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username","balance_rial","balance_gold")

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("user","id","status","price_per_gram")
    readonly_fields = ("gold_weight_gram","date")

