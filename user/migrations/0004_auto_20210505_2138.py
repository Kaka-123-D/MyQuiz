# Generated by Django 3.2.1 on 2021-05-05 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_question_order_in_pack'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='required',
            field=models.ManyToManyField(related_name='required', to='quiz.QuizPack'),
        ),
        migrations.AddField(
            model_name='courses',
            name='student',
            field=models.ManyToManyField(related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courses',
            name='manageTeacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='QUser',
        ),
    ]
