from django.db import models
from django.utils.text import slugify

import uuid


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SluggedModel (models.Model):
    slug = models.SlugField(max_length=255, unique=True,
                            blank=True, editable=False)
    slug_source = "name"

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if (not self.slug):
            source_value = getattr(self, self.slug_source, "")
            base_slug = (slugify(source_value, allow_unicode=True)
                         or "item")[:241]
            base_uuid = str(uuid.uuid4())[:8]
            self.slug = f"{base_slug}-{base_uuid}"

        super().save(*args, **kwargs)
