from django.db import models
from django.urls import reverse
from PIL import Image
import uuid

class Genres(models.Model):
    name            = models.CharField(max_length=50, help_text='Enter a genre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'

class Author(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    pseudonym       = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth   = models.DateField(null=True, blank=True)
    date_of_death   = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])
    
    def __str__(self):
        return f'{self.pseudonym} ({self.first_name} {self.last_name})'

class Category(models.Model):
    title           = models.CharField(max_length=150, help_text='Enter a title')
    author          = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    year            = models.DateField(help_text='Enter year of release', null=True, blank=True)
    link            = models.URLField(max_length=200, null=True, blank=True)
    genre           = models.ManyToManyField(Genres, help_text='Select genres for this media')
    image           = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='library')

    MEDIA_TYPE = (
        ('m', 'music'),
        ('f', 'films'), 
        ('s', 'series'),
        ('b', 'books'),
        ('g', 'games'),
        ('o', 'other'),
    )

    media_type = models.CharField(
        max_length=1,
        choices=MEDIA_TYPE,
        blank=True,
        default='0',
        help_text='Type of your media',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("kind-detail", args=[str(self.id)])

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 1000 or img.width > 1000:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    class Meta:
        verbose_name = 'Categorie'
    
class CategoryInstance(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular media')
    category        = models.ForeignKey(Category, on_delete=models.RESTRICT)

    RATING_OPTIONS = (
        ('10', '10stars'),
        ('09', '9stars'),
        ('08', '8stars'),
        ('07', '7stars'),
        ('06', '6stars'),
        ('05', '5stars'),
        ('04', '4stars'),
        ('03', '3stars'),
        ('02', '2stars'),
        ('01', '1stars'),
        ('00', '0stars')
    )

    rating = models.CharField(
        max_length=2,
        choices=RATING_OPTIONS,
        blank=True,
        default='00',
        help_text='Rating of your media',
    )

    class Meta:
        ordering = ['rating']

    def __str__(self):
        return f'{self.category.title} ({self.id})'

    