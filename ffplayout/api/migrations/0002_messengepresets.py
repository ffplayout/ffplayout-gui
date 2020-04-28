# Generated by Django 3.0.5 on 2020-04-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessengePresets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the preset name', max_length=255)),
                ('message', models.CharField(blank=True, default='', max_length=1024, null=True)),
                ('x', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('y', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('font_size', models.IntegerField(default=24)),
                ('font_spacing', models.IntegerField(default=4)),
                ('font_color', models.CharField(default='#ffffff', max_length=12)),
                ('font_alpha', models.FloatField(default=1.0)),
                ('show_box', models.BooleanField(default=True)),
                ('box_color', models.CharField(default='#000000', max_length=12)),
                ('box_alpha', models.FloatField(default=0.8)),
                ('border_width', models.IntegerField(default=4)),
                ('overall_alpha', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]
