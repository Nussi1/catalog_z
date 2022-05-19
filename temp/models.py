from django.db import models

class Post(models.Model):
    file = models.FileField( # models.ImageField - > FileField
        upload_to='files/%Y/%m/%d',
        blank=True,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    views = models.IntegerField(
        blank=True,
    )
    tags = models.ForeignKey(
        'Tags',
        on_delete=models.CASCADE,
    )
    license = models.TextField(
        blank=True,
    )
    dimension = models.CharField(
        max_length=255,
        blank=True
    )
    format = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.pk

class Tags(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.pk

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True
    )
    email = models.EmailField(
        blank=True
    )
    CHOICES = (
        ('Python', 'Python'),
        ('Java', 'Java'),
    )
    choice = models.CharField(
        max_length=255,
        choices=CHOICES,
        blank=True,
    )
    text = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.pk