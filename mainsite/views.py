# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Post

from django.shortcuts import render
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.
def homepage(request):
    
    posts = Post.objects.all()
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
        post_lists.append("<small>" + str(post.body.encode('utf-8')) +"</small><br><br>")
    return HttpResponse(post_lists)