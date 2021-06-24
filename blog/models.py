from django.db import models
from django.contrib.auth.models import User
class Blog(models.Model):
    status=(
        (0,"Draft"),
        (1,"publish")
    )
    title=models.CharField(max_length=100)
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=100)
    status = models.IntegerField(choices=status, default=0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self) :
        return self.title
    

    
