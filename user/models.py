from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone

# Create your models here.
class Manager(BaseUserManager):
    def create_user(self,email,username,password= None):
        if not email:
            raise ValueError('email thaapura munda')
        if not username:
            raise ValueError('kothaaga aallochinchu')
        user = self.model(email = self.normalize_email(email),username= username)
        user.set_password(password)
        user.save(using= self._db)
        return user
    def create_superuser(self,email,username,password):
        user = self.create_user(email=self.normalize_email(email),username= username,password= password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

        
class Account(AbstractBaseUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    image = models.ImageField(upload_to= 'satic/',blank = True)
    dob  = models.DateField(default= timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = Manager()
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

