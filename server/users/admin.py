from django.contrib.auth.models import Group, User
from django.contrib import admin

from .models import Users

admin.site.site_header = 'Scotland Yard'
admin.site.site_title = 'Login system background'
admin.site.index_title = 'back-stage management'

admin.site.unregister(Group)
admin.site.unregister(User)


# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    # list_display sets the fields to display in the list (the ID field is the default primary key for the Django model)
    list_display = ('id', 'userId', 'sex', 'phone', 'password')

    # list_per_page sets how many records are displayed on each page. The default is 100 records
    list_per_page = 50
