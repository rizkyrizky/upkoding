# Generated by Django 3.1.6 on 2021-09-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.SmallIntegerField(choices=[(63, 'javascript'), (71, 'python'), (60, 'go'), (72, 'ruby')], default=63, verbose_name='Language')),
                ('block_1_title', models.CharField(blank=True, default='', max_length=100, verbose_name='#1 Title')),
                ('block_1_desc', models.TextField(blank=True, default='', help_text='Markdown', verbose_name='#1 Description')),
                ('block_1_hint', models.CharField(blank=True, default='', max_length=250, verbose_name='#1 Hint')),
                ('block_1_code', models.TextField(blank=True, default='', verbose_name='#1 code')),
                ('block_1_ro', models.BooleanField(default=True, verbose_name='#1 Readonly')),
                ('block_2_title', models.CharField(blank=True, default='', max_length=100, verbose_name='#2 Title')),
                ('block_2_desc', models.TextField(blank=True, default='', help_text='Markdown', verbose_name='#2 Description')),
                ('block_2_hint', models.CharField(blank=True, default='', max_length=250, verbose_name='#2 Hint')),
                ('block_2_code', models.TextField(blank=True, default='', verbose_name='#2 code')),
                ('block_2_ro', models.BooleanField(default=True, verbose_name='#2 Readonly')),
                ('block_3_title', models.CharField(blank=True, default='', max_length=100, verbose_name='#3 Title')),
                ('block_3_desc', models.TextField(blank=True, default='', help_text='Markdown', verbose_name='#3 Description')),
                ('block_3_hint', models.CharField(blank=True, default='', max_length=250, verbose_name='#3 Hint')),
                ('block_3_code', models.TextField(blank=True, default='', verbose_name='#3 code')),
                ('block_3_ro', models.BooleanField(default=True, verbose_name='#3 Readonly')),
                ('block_4_title', models.CharField(blank=True, default='', max_length=100, verbose_name='#4 Title')),
                ('block_4_desc', models.TextField(blank=True, default='', help_text='Markdown', verbose_name='#4 Description')),
                ('block_4_hint', models.CharField(blank=True, default='', max_length=250, verbose_name='#4 Hint')),
                ('block_4_code', models.TextField(blank=True, default='', verbose_name='#4 code')),
                ('block_4_ro', models.BooleanField(default=True, verbose_name='#4 Readonly')),
                ('block_5_title', models.CharField(blank=True, default='', max_length=100, verbose_name='#5 Title')),
                ('block_5_desc', models.TextField(blank=True, default='', help_text='Markdown', verbose_name='#5 Description')),
                ('block_5_hint', models.CharField(blank=True, default='', max_length=250, verbose_name='#5 Hint')),
                ('block_5_code', models.TextField(blank=True, default='', verbose_name='#5 code')),
                ('block_5_ro', models.BooleanField(default=True, verbose_name='#5 Readonly')),
                ('run_count', models.IntegerField(default=0)),
                ('run_result', models.JSONField(blank=True, null=True, verbose_name='Result')),
                ('expected_output', models.TextField(blank=True, default='')),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
