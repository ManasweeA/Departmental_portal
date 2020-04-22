# Generated by Django 2.2 on 2019-05-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_login_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='FILES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='static/uploads/')),
            ],
        ),
    ]