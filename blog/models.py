from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.urls import reverse
from django.contrib.auth.models import Permission

class AdminUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password):
        if not email:
            raise ValueError("Users must have an email address")

        adminuser = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            password=password
            )

        adminuser.set_password(password)
        adminuser.save(using=self._db)
        return adminuser

    def create_superuser(self, email, first_name, last_name,username,password):
        """
        Creates and saves a superuser with the given email, first name, last name and password.
        """
        adminuser = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email = email,
            password=password
        )
        adminuser.is_admin = True
        adminuser.save(using=self._db)
        return adminuser


class AdminUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50,unique=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AdminUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','username','last_name', 'password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name_plural = "Administrators"



CATEGORY_CHOICES = (('Bud Solutionz','Bud Solutionz'),('Lifestyle','Lifestyle'),('Music','Music'))
class Article(models.Model):
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to='blog-images/', null=True)
	text = models.TextField()
	featured = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
	writer = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	def summary(self):
		return self.text[:100]

	def pub_date(self):
		return self.date.strftime('%b %e %Y')
	def __str__(self):
		return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email


class Blogger(AdminUser):
    objects = AdminUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','username','last_name', 'password']

    def __str__(self):
        return self.email

    def has_perm(self, add, obj=Article):
        return True
    def has_perm(self, change, obj=Article):
        return True
    def has_perm(self, delete, obj=Article):
        return True
    def has_perm(self, add, obj=AdminUser):
        return False
    def has_perm(self, change, obj=AdminUser):
        return False
    def has_perm(self, delete, obj=AdminUser):
        return False
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return True

    class Meta:
        verbose_name_plural = "Bloggers"

# Create your models here.