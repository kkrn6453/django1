from django.http import HttpResponse
from test1.models import yjf
import random

def hello(request):
    return HttpResponse("aaa")


def add_data(request):
    Yjf = yjf()
    Yjf.user='jack%d' % random.randrange(100)
    Yjf.save()
    return HttpResponse("success %s" % Yjf.user)


def get_data(request):
    yjfs = yjf.objects.all()

    for aa in yjfs:
        print(aa.user)
    return HttpResponse("ss LIST")





