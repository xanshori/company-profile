from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomBaseUser(BaseUserManager):
    def create_user(self,username,email,password = None,**extra_fields):
        if  not email:
            raise ValueError('harus memiliki alamat email')

        if not username:
            raise ValueError('harus memiliki username')
        
        user = self.model(
            email       = self.normalize_email(email),
            username    = username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)


        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username,email, password, **extra_fields)