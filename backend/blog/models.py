from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
  # user is mapped with the Django user
  # website is optional URL to know more about the user
  # bio means biography
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.PROTECT,
  )
  website = models.URLField(blank=True)
  bio = models.CharField(max_length=240, blank=True)

  # __str__ method will echo specific info, 
  # more understandable to human.
  def __str__(self):
    return self.user.get_username()

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name

class Post(models.Model):
  # title: The title of the post
  # subtitle: optional clarifier
  # slug: a unique, readable identifier for the posts to use in URLs
  # body: post's content
  # meta_description: optional description for SEO
  # date_created: timestamp for post's creation
  # date_modified: timestamp for post's latest change
  # publish_date: optional timestamp for post going live
  # published: whether or not available to readers
  # author: reference to the author
  # tags: list of tags
  class Meta:
    ordering = ["-publish_date"]

  title = models.CharField(max_length=255, unique=True)
  subtitle = models.CharField(max_length=255, blank=True)
  slug = models.SlugField(max_length=255, unique=True)
  meta_description = models.CharField(max_length=150, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)
  publish_date = models.DateTimeField(blank=True, null=True)
  published = models.BooleanField(default=False)
  # models.PROTECT prevent you accidentally delete author
  # who still has posts
  author = models.ForeignKey(Profile, on_delete=models.PROTECT)
  # ManyToMany Relationship allows you asscociate a post
  # with zero or more tags
  tags = models.ManyToManyField(Tag, blank=True)
    

