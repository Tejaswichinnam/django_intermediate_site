from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import Useradd,Contact
class ContactAdmin(admin.ModelAdmin):

    list_display=("firstname","email","is_resolved","created_at")
    list_filter=("is_resolved","created_at")



admin.site.register(Useradd)


admin.site.register(Contact,ContactAdmin)