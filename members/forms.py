from django import forms
from .models import Member
from chapters.models import Region, Province, Municipality, Barangay


class MemberForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        empty_label="Select Region",
        required=False,
        widget=forms.Select(attrs={"class": "form-select", "hx-get": "/members/provinces/", "hx-target": "#id_province", "hx-include": "[name='region']"}),
    )
    province = forms.ModelChoiceField(
        queryset=Province.objects.none(),
        empty_label="Select Province",
        required=False,
        widget=forms.Select(attrs={"class": "form-select", "hx-get": "/members/municipalities/", "hx-target": "#id_municipality", "hx-include": "[name='province']"}),
    )
    municipality = forms.ModelChoiceField(
        queryset=Municipality.objects.none(),
        empty_label="Select Municipality",
        required=False,
        widget=forms.Select(attrs={"class": "form-select", "hx-get": "/members/barangays/", "hx-target": "#id_barangay", "hx-include": "[name='municipality']"}),
    )
    barangay = forms.ModelChoiceField(
        queryset=Barangay.objects.none(),
        empty_label="Select Barangay",
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Member
        fields = [
            'first_name', 'middle_name', 'last_name', 'suffix',
            'gender', 'birthdate', 'civil_status',
            'mobile', 'email', 'facebook',
            'street', 'region', 'province', 'municipality', 'barangay',
            'id_photo', 'status',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'suffix': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'civil_status': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'id_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
