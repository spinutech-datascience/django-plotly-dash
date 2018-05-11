# Generated by Django 2.0.5 on 2018-05-10 23:26

from django.db import migrations

def getDA(apps):
    return apps.get_model("django_plotly_dash","DashApp")

def forward(apps, schema_editor):
    DashApp = getDA(apps)
    da = DashApp(app_name="SimpleExample",
                 instance_name="SimpleExample-1",
                 slug="simpleexample-1",
                 base_state='{"dropdown-color":{"value":"blue"},"dropdown-size":{"value":"small"}}')
    da.save()

def backward(apps, schema_editor):
    DashApp = getDA(apps)
    DashApp.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('django_plotly_dash', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]