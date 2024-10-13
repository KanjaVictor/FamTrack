from django.contrib import admin
from .models import Family, FamilyMember

# Register your models here.
#admin.site.register(Family)
#admin.site.register(FamilyMember)

class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'type_of_member', 'family_id')


admin.site.register(FamilyMember, FamilyMemberAdmin)

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'family_name', 'address')