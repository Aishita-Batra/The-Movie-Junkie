

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0007_movie_watch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watch',
        ),
    ]
