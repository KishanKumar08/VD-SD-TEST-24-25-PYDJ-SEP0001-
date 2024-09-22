

from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def get_top_5_customers_last_6_months(cls):
        six_months_ago = now() - timedelta(days=6 * 30)
        top_customers = (
            cls.objects.filter(order_date__gte=six_months_ago)
            .values('customer')
            .annotate(total_spent=Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )
        return top_customers
