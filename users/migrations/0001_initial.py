# Generated by Django 4.2 on 2023-04-23 22:33

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(editable=False, max_length=255, unique=True)),
                ("address", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "organization",
                "verbose_name_plural": "organizations",
            },
        ),
        migrations.CreateModel(
            name="TechnologyStack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "technology_stack",
                    models.CharField(
                        choices=[
                            ("PYTHON", "Python"),
                            ("JAVA", "Java"),
                            ("JAVASCRIPT", "JavaScript"),
                            ("C_SHARP", "C#"),
                            ("PHP", "PHP"),
                            ("RUBY", "Ruby"),
                            ("SWIFT", "Swift"),
                            ("KOTLIN", "Kotlin"),
                            ("GO", "Go"),
                            ("TYPESCRIPT", "TypeScript"),
                            ("C_PLUS_PLUS", "C++"),
                            ("C", "C"),
                            ("OBJECTIVE_C", "Objective-C"),
                            ("SQL", "SQL"),
                            ("HTML_CSS", "HTML/CSS"),
                            ("PERL", "Perl"),
                            ("SHELL", "Shell"),
                            ("R", "R"),
                            ("MATLAB", "MATLAB"),
                            ("SCALA", "Scala"),
                            ("GROOVY", "Groovy"),
                            ("VB_NET", "VB.NET"),
                            ("VISUAL_BASIC", "Visual Basic"),
                            ("SWIFTUI", "SwiftUI"),
                            ("REACT", "React"),
                            ("ANGULAR", "Angular"),
                            ("VUE_JS", "Vue.js"),
                            ("NODE_JS", "Node.js"),
                            ("DJANGO", "Django"),
                            ("RAILS", "Ruby on Rails"),
                            ("SPRING", "Spring"),
                            ("LARAVEL", "Laravel"),
                            ("ASP_NET", "ASP.NET"),
                            ("EXPRESS_JS", "Express.js"),
                            ("FLASK", "Flask"),
                            ("REACT_NATIVE", "React Native"),
                            ("XAMARIN", "Xamarin"),
                            ("UNITY", "Unity"),
                            ("FLUTTER", "Flutter"),
                            ("ANDROID", "Android"),
                            ("IOS", "iOS"),
                            ("AWS", "Amazon Web Services (AWS)"),
                            ("AZURE", "Microsoft Azure"),
                            ("GOOGLE_CLOUD", "Google Cloud Platform (GCP)"),
                            ("DOCKER", "Docker"),
                            ("KUBERNETES", "Kubernetes"),
                            ("TERRAFORM", "Terraform"),
                            ("ELASTICSEARCH", "Elasticsearch"),
                            ("OTHER", "Other"),
                        ],
                        default="OTHER",
                        max_length=100,
                    ),
                ),
            ],
            options={
                "verbose_name": "technology stack",
                "verbose_name_plural": "technology stacks",
            },
        ),
        migrations.CreateModel(
            name="TechnologyStackGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tech_stack_group",
                    models.CharField(
                        choices=[
                            ("MEN", "MEAN/MERN"),
                            ("LAMP", "LAMP"),
                            ("FULL_STACK", "Full-Stack"),
                            ("BACKEND", "Backend"),
                            ("FRONTEND", "Frontend"),
                            ("DATA_SCIENCE", "Data Science"),
                            ("MOBILE", "Mobile Development"),
                            ("GAME_DEV", "Game Development"),
                            ("DEV_OPS", "DevOps"),
                            ("OTHER", "Other"),
                        ],
                        default="OTHER",
                        max_length=100,
                    ),
                ),
            ],
            options={
                "verbose_name": "technology stack group",
                "verbose_name_plural": "technology stack groups",
            },
        ),
        migrations.CreateModel(
            name="Recruiter",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("job_title", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("is_owner", models.BooleanField(default=False)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_recruiters",
                        to="users.organization",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "recruiter",
                "verbose_name_plural": "recruiters",
            },
        ),
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "expected_salary",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("hourly_rate", models.DecimalField(decimal_places=2, max_digits=10)),
                ("resume", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=20)),
                (
                    "tech_stack_group",
                    models.ManyToManyField(
                        related_name="stack_group", to="users.technologystackgroup"
                    ),
                ),
                (
                    "technology_stack",
                    models.ManyToManyField(
                        related_name="tech_stack", to="users.technologystack"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applicant_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
