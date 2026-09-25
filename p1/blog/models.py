from django.db import models

from common.models import TimeStampedModel, SluggedModel

# Create your models here.


class Author(TimeStampedModel, SluggedModel):
    name = models.CharField("name", max_length=100)
    bio = models.TextField("bio", blank=True, null=True)
    email = models.EmailField("email", unique=True)

    def __str__(self):
        return self.name


class Category(TimeStampedModel, SluggedModel):
    name = models.CharField("category", max_length=100)
    description = models.TextField("description", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]


class Tag(TimeStampedModel, SluggedModel):
    name = models.CharField("tag", max_length=100)
    description = models.TextField("description", blank=True)

    def __str__(self):
        return self.name


class Series(TimeStampedModel, SluggedModel):
    title = models.CharField("Series", max_length=100)
    description = models.TextField("description", blank=True)
    slug_source = "title"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "series"


class Post(TimeStampedModel, SluggedModel):
    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"
    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISHED, "Published")
    ]

    title = models.CharField("Title", max_length=150)
    slug_source = "title"
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="posts")
    series = models.ForeignKey(
        Series, on_delete=models.SET_NULL, related_name="posts", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class PostImage(TimeStampedModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="images")
    image = models.URLField()
    caption = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"image for {self.post}"
