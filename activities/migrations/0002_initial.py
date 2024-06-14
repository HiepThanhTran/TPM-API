# Generated by Django 4.2.13 on 2024-06-13 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0002_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('activities', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingactivityreport',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='users.student'),
        ),
        migrations.AddField(
            model_name='bulletin',
            name='poster_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='activityregistration',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='activities.activity'),
        ),
        migrations.AddField(
            model_name='activityregistration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='users.student'),
        ),
        migrations.AddField(
            model_name='activity',
            name='bulletin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activities', to='activities.bulletin'),
        ),
        migrations.AddField(
            model_name='activity',
            name='criterion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activities', to='schools.criterion'),
        ),
        migrations.AddField(
            model_name='activity',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='schools.faculty'),
        ),
        migrations.AddField(
            model_name='activity',
            name='organizer_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='activity',
            name='participants',
            field=models.ManyToManyField(related_name='activities', through='activities.ActivityRegistration', to='users.student'),
        ),
        migrations.AddField(
            model_name='activity',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='schools.semester'),
        ),
        migrations.AlterUniqueTogether(
            name='missingactivityreport',
            unique_together={('student', 'activity')},
        ),
        migrations.AddIndex(
            model_name='bulletin',
            index=models.Index(fields=['poster_type', 'poster_id'], name='activities__poster__deee01_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='activityregistration',
            unique_together={('student', 'activity')},
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['organizer_type', 'organizer_id'], name='activities__organiz_6df93a_idx'),
        ),
    ]
