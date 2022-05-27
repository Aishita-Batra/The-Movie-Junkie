

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_auto_20200609_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrating',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
