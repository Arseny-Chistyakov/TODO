from django.contrib.auth.forms import UserChangeForm

from users.models import User


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
