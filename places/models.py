from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField('عنوان',max_length=100)
    description = models.TextField('توضیحات',blank=True)    
    image = models.ImageField('تصویر مکان', upload_to='places/',blank=True,null=True)
    date = models.DateTimeField('تاریخ ثبت', auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta():
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان ها'
