from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email,username, first_name, last_name,address, phone, password=None ):
        if not email:
            raise ValueError('User must have an email address ')
        if not username:
            raise ValueError('User must have an username ')
        if not first_name:
            raise ValueError('User must have a first_name ')
        # if not last_name:
        #     raise ValueError('User must have a last_name ')
        if not address:
            raise ValueError('User must have an address ')
        if not phone:
            raise ValueError('User must have a phone number ')
        if not password:
            raise ValueError('User must have a password ')

        user = self.model(
            email = self.normalize_email(email), 
            username = username,
            first_name = first_name,
            last_name = last_name,
            address = address,
            phone = phone,
            password = password,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, username, first_name, last_name, address, phone, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
            address = address,
            phone = phone, 
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user



class User(AbstractUser):
    email               = models.EmailField(verbose_name='email', max_length=60,unique=True)
    username            = models.CharField(max_length=30,unique=True)
    date_joined         = models.DateTimeField(verbose_name='date joined',auto_now_add=True )
    last_login          = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    first_name          = models.CharField(max_length=30)
    last_name           = models.CharField(max_length=30)
    address             = models.CharField(max_length=1024)
    phone               = models.CharField(max_length=11)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','address', 'phone', 'password']

    object = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


