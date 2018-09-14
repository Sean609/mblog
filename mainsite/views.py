# -*- coding: utf-8 -*-
from django.template.loader import get_template
#from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Post
from datetime import datetime

from django.shortcuts import render
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)