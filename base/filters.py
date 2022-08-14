import django_filters

from django import forms
from .models import *

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
    widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ['title', 'tags']