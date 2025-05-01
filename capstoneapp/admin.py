from django.contrib import admin

from capstoneapp.models import Booking, Menu


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "inventory")


class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "no_of_guests", "booking_date")


admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)
