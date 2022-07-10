from django import forms
from .models import Visitor_Register


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor_Register
        fields = ('protected_area', 'zone', 'visit_date', 'choose_shift', 'vehicle_type', 'vehicle_type', 'member_name', 'gender', 'nationality', 'id_type', 'id_number', 'video_cam')