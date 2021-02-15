from django.db import models


class Merged(models.Model):
    m_img = models.ImageField(default='d.png', upload_to='merged_pic')

    def __str__(self):
        return f'{self.id} merged'

class Frame(models.Model):
    frame = models.ImageField(default='d.png', upload_to='frames_pic')

    def __str__(self):
        return f'{self.id} frame'

class Uimg(models.Model):
    img = models.ImageField(default='d.png', upload_to='user_img')

    def __str__(self):
        return f'{self.id} user pic'
        