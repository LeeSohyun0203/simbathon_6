# Generated by Django 3.2 on 2021-06-26 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question')),
            ],
        ),
    ]
