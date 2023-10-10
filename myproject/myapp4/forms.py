from django import forms
import datetime


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    #проверка валидности поля на мин длину поля = 3
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Имя должно содержать не менее 3 символов')     # не роняет код, а просто выводит ошибку
        return name

    # проверка валидности поля ввод имени email
    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or email.endswith('corp.mail.ru')):
            raise forms.ValidationError('Используйте корпоративную почту ')
        return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)                      #False - нет галочки в этом поле
    birthdate = forms.DateField(initial=datetime.date.today)            # по умолчанию - текущая дата
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F','Female')])
    # в поле предлагается один из вариантов мужчина или женщина  : Male/M или F/Female
    # (Male, Female -для пользователя, M, F  -для сервера)


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Введите имя пользователя'}))
    #виджет для ввода текста
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


#  создания поля для сохранения  изображений и файлов
class ImageForm(forms.Form):
    image = forms.ImageField()              # для сохранен я файлов - image = forms.FileField()