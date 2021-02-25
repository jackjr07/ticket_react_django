from django.contrib import admin
from .models import ticket

# Register your models here.
class ticket_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(ticket, ticket_admin)

