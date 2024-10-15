# blog/widgets.py
from django import forms

class TagWidget(forms.CheckboxSelectMultiple):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom widget logic if needed
