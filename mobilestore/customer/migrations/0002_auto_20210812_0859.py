# Generated by Django 3.2 on 2021-08-12 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_mobile_brand'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('incart', 'incart'), ('order_placed', 'order_placed'), ('order_cancelled', 'order_cancelled')], default='in_cart', max_length=40)),
                ('user', models.CharField(max_length=40)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.mobile')),
            ],
        ),
        migrations.DeleteModel(
            name='Mobile',
        ),
    ]