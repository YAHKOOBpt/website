# Generated by Django 4.2.2 on 2023-09-16 04:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='myimages/')),
                ('author', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Background_image9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mybg/')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('doctor', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField(blank=True)),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DentalSurgeryStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='surgery_images/')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='history_images/')),
            ],
            options={
                'ordering': ['year'],
            },
        ),
        migrations.CreateModel(
            name='Image_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('uploaded_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medical_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('post', models.IntegerField(blank=True, null=True, verbose_name=50)),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name=60)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('document_name', models.FileField(blank=True, null=True, upload_to='upload/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/')),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='myimages/')),
                ('review', models.TextField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='mystaffs/')),
                ('description', models.TextField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='myimages/')),
                ('description', models.TextField(blank=True)),
                ('know_more_link', models.URLField(blank=True)),
                ('youtube_link', models.URLField(blank=True)),
                ('uploaded_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Youtube_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('uploaded_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='YouTube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('youtube_link', models.URLField(blank=True)),
                ('uploaded_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nechuwebapp.youtube_category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='myimages/')),
                ('description', models.TextField(blank=True)),
                ('uploaded_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nechuwebapp.image_category')),
            ],
        ),
    ]
