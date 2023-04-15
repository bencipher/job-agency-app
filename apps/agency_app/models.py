from django.db import models


# Create your models here.
class Job(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    contract_type = models.CharField(max_length=255, choices=[('contract', 'Contract'),
                                                              ('permanent', 'Permanent')])
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    date_posted = models.DateField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.title
