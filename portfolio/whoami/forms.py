from django import forms

from .models import Me


class MeForm(forms.ModelForm):
    #image = forms.ImageField(label='image', required=False, widget=forms.FileInput)
    class Meta:
        model = Me

        #These are from blog, fix for this case
        fields = ('image',
                  'title_shortInfo','text_shortInfo',
                  'title_education','text_education',
                  'title_thesis','text_thesis',
                  'title_workExperience','text_workExperience',
                  'title_currentPosition','text_currentPosition',
                  'title_skills','text_skills',
                  'title_codingTechnologies','text_codingTechnologies',
                  'title_hobbies','text_hobbies')

        widgets = {
            'title_shortInfo': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_shortInfo': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'title_education': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_education': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'title_thesis': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_thesis': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'title_workExperience': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_workExperience': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'title_currentPosition': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_currentPosition': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'title_skills': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_skills': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'title_codingTechnologies': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_codingTechnologies': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'title_hobbies': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_hobbies': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
