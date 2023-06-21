from django import forms


class InputForm(forms.Form):
    text = forms.CharField(required=False, widget=forms.Textarea)
    file = forms.FileField(required=False)
    topics = forms.CharField(required=True)
    
    def clean(self):
        #check if either text or file is given
        if not self.cleaned_data.get('text') and not self.cleaned_data.get('file'):   
            raise forms.ValidationError("Please upload file or enter text.")
        
        if self.cleaned_data.get('text') and self.cleaned_data.get('file'):   
            raise forms.ValidationError("Please only upload file or only enter text.")
        
        # check if uploaded files are in valid formats
        files = self.cleaned_data.get('files')
        allowed_extensions = ['.doc', '.docx', '.pdf', '.txt']

        if files:
            for file in files:
                file_extension = file.name.lower().split('.')[-1]
                if not file_extension in allowed_extensions:
                    raise forms.ValidationError("Only DOC, PDF, or TXT files are allowed.")

        return files
    