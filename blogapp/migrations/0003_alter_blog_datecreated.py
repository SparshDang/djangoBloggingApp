# Generated by Django 4.0.4 on 2022-05-09 09:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blog_datecreated_remove_blog_likes_blog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='dateCreated',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]