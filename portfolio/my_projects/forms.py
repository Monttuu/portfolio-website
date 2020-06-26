from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    #image = forms.ImageField(label='image', required=False, widget=forms.FileInput)
    class Meta:
        model = Project

        #These are from blog, fix for this case
        fields = ('title', 'text','description','image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
