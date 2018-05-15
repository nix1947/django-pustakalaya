from django import template
from  pustakalaya_apps.core.models import EducationLevel


register = template.Library()

@register.inclusion_tag('_partials/educationlevel.html')
def show_results():
    list_education_level = EducationLevel.objects.all()
    return { "education_level" : list_education_level }


