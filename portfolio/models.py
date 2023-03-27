from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio', blank=True)
    url = models.URLField(blank=True)
    # Todo fill this field
    test_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio', blank=True)

    def __str__(self):
        return f'{self.project} - {self.description[0:30]}...'
