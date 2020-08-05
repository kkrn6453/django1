from django.db import models

class yjf(models.Model):
    # db_table = "yjf"
    user = models.CharField(max_length=32,primary_key=True)
    email = models.CharField(max_length=32)

    class Meta:
        db_table= "yjf"