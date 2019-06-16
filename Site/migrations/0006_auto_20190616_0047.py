# Generated by Django 2.1.9 on 2019-06-16 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Site', '0005_auto_20190616_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='object_id',
            new_name='item_object_id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='content_type',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='category_content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cart_item_category', to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='category_object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item_content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cart_item_item', to='contenttypes.ContentType'),
            preserve_default=False,
        ),
    ]
