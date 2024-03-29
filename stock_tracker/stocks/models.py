from django.db import models

class Share(models.Model):
    name = models.CharField(max_length=100)
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2)
    current_cost = models.DecimalField(max_digits=10, decimal_places=2)
    num_shares = models.IntegerField(default=0)

    class Meta:
        app_label = 'stocks'
