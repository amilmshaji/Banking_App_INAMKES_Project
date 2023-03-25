from django.contrib import admin

# Register your models here.
from bank_app.models import Account, Branch

admin.site.register(Account)

admin.site.register(Branch)

