from django import forms 

class contactformemail(forms.form):
    fromeemail=forms.EmailField(required=True)
    subject=form.Charfield(required=True)
    message=form.charfiled(required=True)