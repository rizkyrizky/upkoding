# Generated by Django 3.1.6 on 2021-03-17 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import forum.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20210317_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('description', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], db_index=True, default=1, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forum_threads', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ThreadAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], db_index=True, default=1, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.threadanswer')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Project'), (1, 'Custom')], db_index=True, default=1, verbose_name='Type')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='Status')),
                ('description', models.TextField(blank=True, default='')),
                ('thread_count', models.IntegerField(default=0)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=forum.models.topic_image)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forum_topic', to='projects.project')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ThreadStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, 'View Count'), (1, 'Message Count')], db_index=True, default=0)),
                ('value', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed', models.BooleanField(db_index=True, default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThreadAnswerStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, 'Reply Count')], db_index=True, default=0)),
                ('value', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('thread_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.threadanswer')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadAnswerParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed', models.BooleanField(db_index=True, default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('thread_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.threadanswer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='threadstat',
            constraint=models.UniqueConstraint(fields=('thread', 'type'), name='forum_thread_stat_unique_thread_type'),
        ),
        migrations.AddConstraint(
            model_name='threadparticipant',
            constraint=models.UniqueConstraint(fields=('user', 'thread'), name='forum_thread_participant_unique_user_thread'),
        ),
        migrations.AddConstraint(
            model_name='threadanswerstat',
            constraint=models.UniqueConstraint(fields=('thread_answer', 'type'), name='forum_thread_answer_stat_unique_thread_answer_type'),
        ),
        migrations.AddConstraint(
            model_name='threadanswerparticipant',
            constraint=models.UniqueConstraint(fields=('user', 'thread_answer'), name='forum_thread_answer_participant_unique_user_thread_answer'),
        ),
    ]
