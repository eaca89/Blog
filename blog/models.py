from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True)
    help_text = 'A label for URL config.'

class Startup(models.Model):
    name = models.CharField(max_length=31)    
    slug = models.SlugField()
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()    
    website = models.URLField()
    tag = models.ManyToManyField(Tag)

class Post(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)

    def __str__(self):
        return self.title

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField()
    startup = models.ForeignKey(Startup)
