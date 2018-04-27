from django import forms
from pustakalaya_apps.document.models import Document


from django.forms import formsets
from django.forms.models import BaseInlineFormSet

# ##########remove later **********************
# class BaseDocumentFormSet(BaseInlineFormSet):
#     def __init__(self, *args, **kwargs):
#         """
#         Grabs the curried initial values and stores them into a 'private'
#         variable. Note: the use of self.__initial is important, using
#         self.initial or self._initial will be erased by a parent class
#         """
#         self.__initial = kwargs.pop('initial', [])
#         super(BaseDocumentFormSet, self).__init__(*args, **kwargs)
#
#     def total_form_count(self):
#         return len(self.__initial) + self.extra
#
#     def _construct_forms(self):
#         return formsets.BaseFormSet._construct_forms(self)
#
#     def _construct_form(self, i, **kwargs):
#         if self.__initial:
#             try:
#                 kwargs['initial'] = self.__initial[i]
#             except IndexError:
#                 pass
#         return formsets.BaseFormSet._construct_form(self, i, **kwargs)
#
# DocumentFormSet = formsets.formset_factory(Document, formset=BaseDocumentFormSet)
#*******************upto here***********


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'collections', 'document_file_type', 'languages',
                  'document_interactivity', 'publisher',
                  'keywords', 'document_series', 'document_type', 'license_type']


