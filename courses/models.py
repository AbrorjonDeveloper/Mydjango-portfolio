from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     slug = models.SlugField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name + ' | ' + self.author

#     def get_absolute_url(self):
#         return reverse('blog-home')

#     class Meta:
#         # unique_together = ('slug')
#         verbose_name = "category"
#         verbose_name_plural = "categories"
    
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Category, self).save() 
    
#     def __str__(self):
#         full_path = [self.name]                  
#         k = self.parent
#         while k is not None:
#             full_path.append(k.name)
#             k = k.parent
#         return ' -> '.join(full_path[::-1])

class Course(models.Model):
    
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=300, default="uncategorized tutorial")
    content = models.TextField(blank=True)
    description = models.CharField(max_length=300, null=False)
    tutorial = models.FileField(default="", upload_to="tutorial_courses")
    thumbs_for_video = models.ImageField(default="", upload_to="tutorial_thumbs")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300, blank = False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs) 

    def get_absolute_url(self):
        return reverse('courses')
