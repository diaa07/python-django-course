from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 300)
    done = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey("categories.Category" , on_delete = models.CASCADE , related_name = "tasks")

    def __str__ (self):
        return self.title