from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class BlogOptions(models.Model):
    about = models.TextField()
    phone = models.CharField(max_length=18)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    telegram = models.URLField()

    class Meta:
        verbose_name_plural = 'Blog Options'


class Category(models.Model):
    title = models.CharField(max_length=30)
    order = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/blog/files', blank=True)
    slug = models.SlugField(null=False, db_index=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = [['parent', 'slug']]

    def save(self, *args, **kwargs):
        counter = 2
        if not self.slug:
            slug = slugify(self.title)
            exists = Category.objects.filter(slug=slug)
            while exists:
                newslug = slug + '-' + str(counter)
                exists = Category.objects.filter(slug=newslug)
                counter += 1
                if not exists:
                    slug = newslug
                    break
        else:
            slug = self.slug
            exists = Category.objects.filter(slug=slug).exclude(pk=self.id)
            while exists:
                newslug = slug + '-' + str(counter)
                exists = Category.objects.filter(slug=newslug)
                counter += 1
                if not exists:
                    slug = newslug
                    break

        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        if self.parent == None:
            return self.title
        else:
            return f'{self.parent} -> {self.title}'

    def get_category_posts(cat_slug):
        catpost = Category.objects.get(slug=cat_slug)
        category_posts = catpost.categories.all()
        return category_posts


class Tag(models.Model):
    title = models.CharField(max_length=40)
    order = models.PositiveIntegerField(default=1)
    slug = models.SlugField(null=False, db_index=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        counter = 2
        if not self.slug:
            slug = slugify(self.title)
            exists = Tag.objects.filter(slug=slug)
            while exists:
                newslug = slug + '-' + str(counter)
                exists = Tag.objects.filter(slug=newslug)
                counter += 1
                if not exists:
                    slug = newslug
                    break
        else:
            slug = self.slug
            exists = Tag.objects.filter(slug=slug).exclude(pk=self.id)
            while exists:
                newslug = slug + '-' + str(counter)
                exists = Tag.objects.filter(slug=newslug)
                counter += 1
                if not exists:
                    slug = newslug
                    break

        self.slug = slug
        super().save(*args, **kwargs)

    def get_tag_posts(tagid):
        tagpost = Tag.objects.get(id=tagid)
        tag_posts = tagpost.tags.all()
        return tag_posts

    def get_tag_count(self):
        tagpost = Tag.objects.get(id=self.id)
        tag_posts_count = tagpost.tags.all().count()
        return tag_posts_count

    def get_absolute_url(self):
        return reverse("tag_page", args=[self.slug])


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='categories')
    image = models.ImageField(upload_to='static/blog/files', blank=True)
    is_special = models.BooleanField(default=False)
    excerpt = models.CharField(max_length=100, default='')
    content = RichTextField(null=True)
    posttag = models.ManyToManyField(
        Tag, blank=True, default=None, related_name='tags')
    slug = models.SlugField(null=False, db_index=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        counter = 2
        if not self.slug:
            slug = slugify(self.title)
            exists = Post.objects.filter(slug=slug)
            while exists:
                newslug = slug + '-' + str(counter)
                exists = Post.objects.filter(slug=newslug)
                counter += 1
                if not exists:
                    slug = newslug
                    break
        else:
            slug = self.slug
            exists = Post.objects.filter(slug=slug).exclude(pk=self.id)
            while exists:
                newslug = slug + '-' + str(counter)
                exists = Post.objects.filter(slug=newslug)
                counter += 1
                if not exists:
                    slug = newslug
                    break

        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title}, {self.posttag}'
    
