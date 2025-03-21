from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin,Group

# Create your models here.
class custumusermanager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError('you did not enter vaild username')
        
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        return self.create_user(username,password,**extra_fields)

class custumuser(AbstractUser,PermissionsMixin):
        ROLE_CHOICE = [
            ('admin','admin'),
            ('gtu_cordinator','gtu_cordinator'),
            ('department','department')
        ]
        username = models.CharField(max_length=50,unique=True)
        full_name = models.CharField(max_length=200)
        role = models.CharField(max_length=50,choices=ROLE_CHOICE)

        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        objects = custumusermanager()

        USERNAME_FIELD = 'username'
        REQUIRED_FIELDS = []

        def  __str__(self):
            return self.username,self.role
        
