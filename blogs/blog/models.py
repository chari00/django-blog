# from django.db import models

# # Create your models here.
from django.db import models

# ----------------------------
# Example: Defining a Simple Model
# ----------------------------

# Here is an example of a basic model class that represents a 'Post' in the blog:
class Post(models.Model):
    title = models.CharField(max_length=100)  # Title of the post
    content = models.TextField()  # Content of the post
    published_date = models.DateTimeField(auto_now_add=True)  # Date of publication

    def __str__(self):
        return self.title