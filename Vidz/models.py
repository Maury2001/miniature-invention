from django.db import models


# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " " + self.description
    
    
    
class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.video.title} - {self.comment_text[:50]}'