from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tag'  
        ordering = ['id'] 
    
class Post(models.Model):
    post_id = models.CharField(max_length=255, primary_key=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag) 
    
    def __str__(self):
        return self.post_id
    
    class Meta:
        db_table = 'post'  
        indexes = [
            models.Index(fields=['post_id']),  
        ]
        ordering = ['post_id']  
        
class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    tags = models.JSONField(blank=True, null=True)  
    preferences = models.JSONField(blank=True, null=True)  
    
    def __str__(self):
        return self.user_id
    
    class Meta:
        db_table = 'user'  
        indexes = [
            models.Index(fields=['user_id']),  
        ]
        ordering = ['user_id']  


class Interaction(models.Model):
    interaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    interaction_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_id} - {self.post_id} - {self.interaction_type}"
    
    class Meta:
        db_table = 'interaction'
        ordering = ['-interaction_time']