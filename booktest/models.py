from django.db import models

class BookInfoManager(models.Manager):
    def get_quertset(self):
        return super(BookInfoManager, self).get_quertset().filter(isDelete=False)

    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle=btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    books = BookInfoManager()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', null=True, blank=True)
