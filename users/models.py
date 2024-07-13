from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    pass # For now we do nothinng

    def __str__(self):
        return str(self.username)