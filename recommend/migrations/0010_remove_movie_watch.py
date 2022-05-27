

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0009_movie_watch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watch',
        ),
    ]
