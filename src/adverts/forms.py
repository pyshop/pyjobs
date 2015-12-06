from django import forms
from .models import Advert, User, UsersProfiles
#http://djbook.ru/examples/19/ форму UserLoginForm сделал по этому примеру
from django.utils.translation import ugettext as _ # это функция указывающая переводимую строку подробнее тут http://djbook.ru/rel1.5/topics/i18n/translation.html


class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ('title', 'description', 'requirements', 'salary', 'city')


class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(help_text='еще раз', widget=forms.PasswordInput(), label=_(u'Password'),)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']

    def if_username_exists(self): # эта функция проверяет не используется ли уже имя пользователя
        username = self.cleaned_data['username'] # переменная принимает параметр имя пользователя после получения формы
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists(): # проверяется по праймари кейс и если такой же как уже существующий
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)  # то райзится ошибка юзернейм уже используется
        return username

    def if_email_exists(self): # эта функция проверяет не используется ли уже адрес почты
        email = self.cleaned_data['email'] # переменная принимает параметр email после получения формы
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists(): # проверяется по праймари кейс и если такой же как уже существующий
            raise forms.ValidationError(u'email "%s" is already in use.' % email)  # то райзится ошибка email уже используется
        return email

    def if_password_didnt_match(self):
        cleaned_data = super(UserRegistrationForm, self).clean() # метод возвращает данные в словарь
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data: # проверка есть ли данные из нужных нам полей в словаре
            if self.cleaned_data['password'] != self.cleaned_data['password2']: # если пароли не совпадают
                raise forms.ValidationError(_("Passwords don't match. Please enter both fields again.")) # рейзится ошибка несовпадения паролей
        return self.cleaned_data

#  http://blackglasses.me/2013/09/17/custom-django-user-model/ кусок кода взял отсюда
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password']) # применяем метод сет_пассворд чтобы правильно сохранилось именно как пароль
        if commit: # если фиксируем изменения в базе данных
            user.save() # то сохраняем пользователя
        return user


class UserLoginForm(forms.Form):  # сырая форма
    username = forms.CharField(label=_(u'Username'), max_length=30)  # поле формы, аттрибут "лейбл" будет локализирован при возможности
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)


class EditUsersProfilesForm(forms.Form):
    first_name = forms.CharField(label=_(u'first name'), max_length=30, required=False)
    last_name = forms.CharField(label=_(u'last name'), max_length=30, required=False)
    email = forms.CharField(label=_(u'mail'), max_length=30, required=False)
    phone = forms.CharField(label=_(u'phone'), max_length=30, required=False)
