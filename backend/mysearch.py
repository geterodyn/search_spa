import requests
import celery
from django.conf import settings

app = celery.Celery(
    'search-tasks',
    backend=settings.CELERY_RESULT_BACKEND,
    broker=settings.BROKER_URL,
)


@app.task
def word_count(url, word):
    try:
        response = requests.get(url)
        words_list = [x.lower() for x in response.text.split()]
        return words_list.count(word.lower())
    except requests.exceptions.RequestException:
        return 'unavailable'


