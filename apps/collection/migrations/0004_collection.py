# Generated by Django 4.1 on 2023-11-04 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('uuid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.customuser')),
            ],
        ),
    ]
