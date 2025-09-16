from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(unique=True)  # uniqie=True means now duplicate emails

    # AbstractUser already has: username, password, is_active, is_staff, is_superuser

    groups = models.ManyToManyField(
        Group,
        related_name="accounts_user_set",  # change reverse accessor
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="accounts_user_permissions_set",  # change reverse accessor
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    def __str__(self):
        return self.username


# Profile model (1:1 with User)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 1:1 means : each user has one profile
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


class Role(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True, null=True)


class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)


class RolePermission(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
