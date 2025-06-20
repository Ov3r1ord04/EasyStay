from django import forms
from .models import Apartment, Booking, ApartmentImage
from users.models import User
class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'address', 'price_per_month', 'price_per_day',
                  'status', 'description', 'image']


class ApartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = [
            'title', 'address', 'complex', 'rooms', 'area', 'floor',
            'price_per_month', 'price_per_day', 'status', 'description',
            'image', 'bathrooms', 'latitude', 'longitude',
            'min_age', 'max_age', 'musical_instruments',
            'gender_preference', 'pets_allowed', 'tenant_type',
            'smoking_policy', 'guest_policy', 'amenities'
        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'status', 'type_of_booking', 'comment']
        widgets = {
            'status': forms.RadioSelect,
            'type_of_booking': forms.RadioSelect,
        }


class StudentIDUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_id_photo']
        widgets = {
            'student_id_photo': forms.ClearableFileInput(attrs={
                'style': 'display:none;',
                'id': 'id_student_id_photo'
            })
        }


