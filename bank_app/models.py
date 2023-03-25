
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            username=self.normalize_email(username),


        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password,):
        user = self.create_user(
            username=self.normalize_email(username),
            password=password,

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True

        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = MyAccountManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class Branch(models.Model):
    name = models.CharField(max_length=100,default="Aluva")
    district = models.CharField(max_length=100,default="Ernakulam")

    def __str__(self):
        return self.name


class Details_info(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    age=models.CharField(max_length=3)
    email = models.EmailField(max_length=100, unique=True)
    tel=models.CharField(max_length=12)
    address=models.CharField(max_length=50)
    acc_type=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    branch=models.CharField(max_length=50,null=True)
    debit=models.BooleanField(default=False,null=True)
    credit=models.BooleanField(default=False,null=True)
    cheque=models.BooleanField(default=False,null=True)


