from django.forms import ModelForm
from .models import Announcement,Commission,Lesson,News,Sponsor



class AnnouncementForm(ModelForm):
    class Meta:
        model=Announcement
        fields = '__all__'


class CommissionForm(ModelForm):
    class Meta:
        model=Commission
        fields = '__all__'


class LessonForm(ModelForm):
    class Meta:
        model=Lesson
        fields = '__all__'



class NewsForm(ModelForm):
    class Meta:
        model=News
        fields = '__all__'

class SponsorForm(ModelForm):
    class Meta:
        model=Sponsor
        fields = '__all__'

