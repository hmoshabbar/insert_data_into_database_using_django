from django.contrib import admin

# Register your models here.
from .models import Users

class UserModelAdmin(admin.ModelAdmin):
    list_display=('id','name','email','salary','phone','address') # list will display like this
    list_editable = ['id','name','email','salary','phone','address']
    search_fields=['name']  #This is for searching purpose
     # For filtering purpose like Today,anyday,like this way.
     
    
    class Meta:
        model=Users
        
admin.site.register(Users,UserModelAdmin)
