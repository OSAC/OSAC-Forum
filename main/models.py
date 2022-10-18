from django.db import models

# Create your models here.

post_type = (('Help','Help'),
            ('Discussion','Discussion'),
            ('Announcement','Announcement'),
            ('Rant','Rant'),
            ('Casual','Casual'),
            ('Other','Other'))

tag_choice = (('General','General'),
            ('Academics','Academics'),
            ('Career','Career'),
            ('Health','Health'),
            )  #have to add more interesting ones


class Post(models.Model):
    user = models.CharField(max_length=100) #until authentication is implemented, user will be a string
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    votes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    is_anonymous = models.BooleanField(default=False)
    type = models.CharField(max_length=12, choices=post_type)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    tag0 = models.CharField(max_length=100, choices= tag_choice, blank=True, null=True)
    tag1 = models.CharField(max_length=100, choices= tag_choice, blank=True, null=True)

    def __str__(self):
        string = str(self.id)+": "+self.user
        return string

class Vote(models.Model):
    user = models.CharField(max_length=100) #until authentication is implemented, user will be a string
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_upvote = models.BooleanField(default=True)

    def __str__(self):
        string = str(self.id)+": "+self.user
        return string

class Comment(models.Model):
    user = models.CharField(max_length=100) #until authentication is implemented, user will be a string
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        string = str(self.id)+": "+self.user
        return string