# Generated by Django 4.2.3 on 2023-08-30 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=20, verbose_name='username')),
                ('first_name', models.TextField(max_length=20, verbose_name='name')),
                ('last_name', models.TextField(max_length=20, verbose_name='surname')),
                ('password1', models.TextField(verbose_name='password')),
                ('password2', models.TextField(verbose_name='password confirmation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]