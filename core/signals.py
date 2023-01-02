def user_pre_save(sender, instance, **kwargs):
    instance.username = instance.email
