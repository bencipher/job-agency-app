from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from users.tech_stack_enum import TechStack, TechStackGroup


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a new superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_owner = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'recruiter'
        verbose_name_plural = 'recruiters'

    def __str__(self):
        return self.user.email


class TechnologyStack(models.Model):
    technology_stack = models.CharField(choices=[(tech.name, tech.value) for tech in TechStack],
                                        max_length=100,
                                        default=TechStack.OTHER.name)

    class Meta:
        verbose_name = 'technology stack'
        verbose_name_plural = 'technology stacks'

    def __str__(self):
        return self.technology_stack


class TechnologyStackGroup(models.Model):
    tech_stack_group = models.CharField(choices=[
        (tech.name, tech.value) for tech in TechStackGroup],
        max_length=100, default=TechStack.OTHER.name)

    class Meta:
        verbose_name = 'technology stack group'
        verbose_name_plural = 'technology stack groups'

    def __str__(self):
        return self.tech_stack_group


class Applicant(models.Model):
    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='applicant_profile')
    technology_stack = models.ManyToManyField(TechnologyStack, related_name='tech_stack')
    tech_stack_group = models.ManyToManyField(TechnologyStackGroup, related_name='stack_group')
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    resume = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
