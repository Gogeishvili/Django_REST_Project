from django.db.models import signals
from django.dispatch import receiver
from . import models
from . import custom_signals

@receiver(signal=custom_signals.product_sold_signal)
def on_product_sold(sender, **kwargs):
    product = kwargs.get('instance')
    if product:
        print(f"signali shemovida: {product.name}")


@receiver(signals.pre_save, sender=models.Category)
def on_categoy_save(sender, **kwargs):
    print("Category saved")
    category = kwargs["instance"]
    print(category)
