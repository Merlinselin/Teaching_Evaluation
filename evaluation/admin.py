from django.contrib import admin

# Register your models here.
from .models import TeachersDetails,StudentFeedback,register_table


# Register your models here.

class TeachersDetailsAdmin(admin.ModelAdmin):
    search_fields=('Firstname','Qualification','Experience')
admin.site.register(TeachersDetails,TeachersDetailsAdmin)


class StudentFeedbackAdmin(admin.ModelAdmin):
    search_fields=('Name_of_The_Teacher',)
admin.site.register(StudentFeedback,StudentFeedbackAdmin)


admin.site.register(register_table)
