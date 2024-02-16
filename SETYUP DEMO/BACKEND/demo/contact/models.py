from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_first_name = models.CharField(max_length = 25)
    contact_last_name = models.CharField(max_length= 25)
    contact_email = models.CharField(max_length=60) 
    contact_phone = models.IntegerField(default = 0)
    contact_desc = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return self.contact_first_name