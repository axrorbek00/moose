from django.db import models
from django.utils.text import slugify


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True)

    author = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

            while self.__class__.objects.filter(slug=self.slug).exists():
                slug = self.__class__.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']


class ContactModel(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-created_at']


class CommentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    website = models.CharField(max_length=70, blank=True, null=True)
    message = models.TextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} :: {self.email}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']
