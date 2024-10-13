from django.db import models

# Create your models here.
class Family(models.Model):
    #Fields
    family_name = models.CharField(max_length=50, help_text="Enter family name")
    address = models.CharField(max_length=50, help_text="Enter residence address")
   
    class Meta:
        ordering = ['family_name']

    def __str__(self):
        return self.family_name

class FamilyMember(models.Model):
    PARENT = 'PR'
    SON = 'SN'
    DAUGHTER = 'DT'
    OTHER = 'OT'

    MEMBER_TYPE_CHOICES = [
        (PARENT, 'Parent'),
        (SON, 'Son'),
        (DAUGHTER, 'Daughter'),
        (OTHER, 'Other'),
    ]

    first_name = models.CharField(max_length=50, help_text="Enter your first name")
    last_name = models.CharField(max_length=50, help_text="Enter your last name")
    date_of_birth = models.DateField(help_text="Enter date of birth")
    type_of_member = models.CharField(max_length=2, choices=MEMBER_TYPE_CHOICES, default=OTHER)
    family_id = models.ForeignKey(Family, related_name='members', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name