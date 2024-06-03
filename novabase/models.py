from django.db import models

class Youtube_videos(models.Model):
    video_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.video_id