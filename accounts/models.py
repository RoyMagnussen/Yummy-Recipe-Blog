from django.db.models import ImageField
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Account(User):
    
    profile_picture = ImageField(upload_to='profile_pictures')
    
    def __str__(self) -> str:
        return self.username