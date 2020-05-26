from django.contrib import admin

# Register your models here.
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(Ticket, TicketAdmin)