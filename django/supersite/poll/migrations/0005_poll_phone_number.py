from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_poll_post_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='phone_number',
            field=models.IntegerField(default=912222222),
            preserve_default=False,
        ),
    ]
