

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0010_remove_movie_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watch',
            field=models.BooleanField(default=False),
        ),
    ]
