from django.db import models
from core.models import TimeStampedModel
# Create your models here.

class UserSettings(TimeStampedModel):
    """
    Model to store additional user settings and preferences. Extends User
    model.
    """
    def username(self):
        return self.user.username
    username.admin_order_field = 'user__username'
