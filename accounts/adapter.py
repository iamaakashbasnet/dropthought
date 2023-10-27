import requests
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.files.base import ContentFile


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form):
        user = sociallogin.user
        user.is_active = True

        avatar_url = sociallogin.account.extra_data.get('picture')
        name = sociallogin.account.extra_data.get('name')
        res = requests.get(avatar_url)
        if res.status_code == 200:
            user.avatar.save(
                f'avatar_{name}.jpg', ContentFile(res.content))
            user.save()

        return super().save_user(request, sociallogin, form)
