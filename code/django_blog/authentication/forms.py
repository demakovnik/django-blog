from django.contrib.auth.forms import UserCreationForm

from authentication.models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'birth_date',
                  'email',
                  'username',
                  'password1',
                  'password2')


