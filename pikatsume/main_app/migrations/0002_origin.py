# Generated by Django 3.0.4 on 2020-03-19 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(choices=[('A', 'Anime'), ('G', 'Game'), ('F', 'Fan-made')], default='A', max_length=1)),
                ('pika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Pika')),
            ],
        ),
    ]
