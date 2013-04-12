from django.db import models

# Create your models here.
class MonitorCache(models.Model):
    MICROBLOG_TYPE = (
    ('P', 'Post'),
    ('C', 'Comment'),
    ('O', 'Origin'),
)
#prefix "mb" means "micro blog"
    monitor_id = models.CharField(max_length = 50)
    mb_id = models.CharField(max_length = 50)
    u_id = models.CharField(max_length = 50)
    mb_type = models.CharField(max_length = 1, choices = MICROBLOG_TYPE)
    comment_mbid = models.CharField(max_length = 50)
    comment_uid = models.CharField(max_length = 50)
    media_html = models.CharField(max_length = 100)
    text_html = models.CharField(max_length = 100) 
    time_stamp = models.DateTimeField(auto_now = False, auto_now_add = False)
    is_guest = models.BooleanField(default = 0)#for BBS
    author_name = models.CharField(max_length = 50)#for BBS
    platform = models.CharField(max_length = 50)
    is_deleted = models.BooleanField(default = 0)
    version = models.CharField(max_length = 50)
    v_time = models.DateTimeField(auto_now_add = False, auto_now = False)
    topic_id = models.CharField(max_length = 50)#non sense
    category = models.CharField(max_length = 50)#non sense
    sentiment_score = models.CharField(max_length = 50)#non sense
    province = models.CharField(max_length =50)
    city = models.CharField(max_length = 50)
    sensitive_word = models.CharField(max_length = 50)
    url = models.CharField(max_length = 50)
    relation =models.CharField(max_length = 50)
































