from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Source(models.Model):
    id = models.AutoField(primary_key=True)
    source_name = models.TextField()
    disqus_name = models.TextField(null=True)
    
    def __unicode__(self):
        return self.source_name

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    disqus_id = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(null=True)
    title = models.TextField()
    url = models.URLField(unique=True)
    source = models.ForeignKey('Source')

    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey('Article')
    author = models.ForeignKey('CommentAuthor')
    text = models.TextField()
    reply_to = models.ForeignKey('self', null=True, related_name="replies")
    disqus_id = models.CharField(max_length=15)
    reply_to_disqus = models.CharField(max_length=15, null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    reports = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    edited = models.BooleanField(default=False)
    spam = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    approved = models.BooleanField(default=True)
    
    def __unicode__(self):
        return 'Comment by %s on %s' % (self.author, self.article.title)
    
class CommentAuthor(models.Model):
    username = models.TextField(null=True)
    real_name = models.TextField()
    power_contrib = models.BooleanField(default=False)
    anonymous = models.BooleanField(default=False)
    reputation = models.FloatField(default=0.0)
    joined_at = models.DateTimeField(null=True)
    disqus_id = models.CharField(max_length=15, null=True)
    avatar = models.URLField()
    primary = models.BooleanField(default=False)
    
    def __unicode__(self):
        if self.anonymous:
            return self.real_name
        else:
            return self.username
    