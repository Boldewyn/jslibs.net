#
#
#


from django.http import HttpResponse
from libraries.models import LibraryModel, BrowserModel, KeywordModel


def detail(request, name):
    return HttpResponse('It Works, %s' % name)
