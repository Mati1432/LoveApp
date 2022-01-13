# Generated by Django 3.2.8 on 2022-01-11 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Thread',
                'verbose_name_plural': 'Threads',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='chat')),
                ('text_body', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('sender_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.thread')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=45)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_one', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_one', to=settings.AUTH_USER_MODEL)),
                ('user_two', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_two', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.CreateModel(
            name='DashboardMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_message_send', models.IntegerField()),
                ('count_message_take', models.IntegerField()),
                ('create_date', models.DateField()),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dashboard Message',
                'verbose_name_plural': 'Dashboards Messages',
            },
        ),
        migrations.CreateModel(
            name='DashboardMatched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_matched', models.IntegerField()),
                ('create_date', models.DateField()),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_one_matched', to=settings.AUTH_USER_MODEL)),
                ('custom_user2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_two_matched', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'DashboardMatched',
                'verbose_name_plural': 'DashboardsMatched',
            },
        ),
        migrations.CreateModel(
            name='DashboardLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_like', models.IntegerField()),
                ('count_dislike', models.IntegerField()),
                ('create_date', models.DateField()),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dashboard Like',
                'verbose_name_plural': 'Dashboards Likes',
            },
        ),
    ]
