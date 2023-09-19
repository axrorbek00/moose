from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from .models import Blog
from django.dispatch import receiver
from django.utils.text import slugify


@receiver(pre_save, sender=Blog)
def pre_create_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

