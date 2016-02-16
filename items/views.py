# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from items.models import Item, Photo

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()


class ItemsView(generic.ListView):
    model = Item
    template_name = 'gallery/items_list.html'

    def get_queryset(self):
        return Item.objects.all()


class ItemView(generic.DetailView):
    model = Item
    template_name = 'gallery/items_detail.html'

    def get_queryset(self):
        return Item.objects.all()


class PhotoView(generic.DetailView):
    model = Photo
    template_name = 'gallery/photos_detail.html'
