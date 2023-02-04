def product_sale_post_save(sender, instance, *args, **kwargs):
    total = 0 
    products = instance.sale.product_sale_set.all() 
    for product in products: 
        total += product.product.price * product.quantity
    instance.sale.total = total
    instance.sale.save()
    instance.price = instance.product.price
    instance._meta.auto_created = True
    instance.save()
    instance._meta.auto_created = False
