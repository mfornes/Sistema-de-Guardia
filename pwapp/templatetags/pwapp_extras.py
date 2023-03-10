# from django import template

# register = template.Library() 

# @register.filter(name='has_group') 
# def has_group(user, group_name):
#     return user.groups.filter(name=group_name).exists() 

from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False