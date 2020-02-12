from django.db import models
from celery.result import AsyncResult

# Create your models here.
class JobItem(models.Model):
    uuid = models.UUIDField(default=None, blank=True)
    status = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField()
    search_word = models.CharField(max_length=100)
    result = models.CharField(max_length=11, default='-')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.url

    def to_dict(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'status': self.status,
            'url': self.url,
            'word': self.search_word,
            'result': self.result,
            'created':  self.created.strftime('%d/%m/%Y - %H:%M:%S'),
            'updated': self.updated.strftime('%d/%m/%Y - %H:%M:%S'),
        }

    def get_job(self):
        return AsyncResult(str(self.uuid))
