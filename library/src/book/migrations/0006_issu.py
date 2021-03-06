# Generated by Django 2.0.7 on 2018-11-16 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField()),
                ('expired_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('fine', models.IntegerField(blank=True, null=True)),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Borrower')),
            ],
        ),
    ]
