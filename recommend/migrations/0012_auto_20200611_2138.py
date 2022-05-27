

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0011_movie_watch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watch',
        ),
        migrations.AddField(
            model_name='myrating',
            name='watch',
            field=models.BooleanField(default=False),
        ),
    ]
