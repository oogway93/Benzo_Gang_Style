from django.contrib.auth.models import AbstractUser
from django.db import models

#//////////////
# from django.conf import settings
# from django.contrib.auth.models import AbstractUser
# from django.core.mail import send_mail
# from django.db import models
# from django.urls import reverse
# from django.utils.timezone import now


class User(AbstractUser):
    images = models.ImageField('Photo User', upload_to='user_photos', default='default_user_photo/default_photo.jpg')
    is_verified_email = models.BooleanField('Is verified email', default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'User'

#//////////////////////////////////////////////////////
# class EmailVerification(models.Model):
#     code = models.UUIDField(unique=True)
#     user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
#     created = models.DateTimeField('Time created', auto_now_add=True)
#     expiration = models.DateTimeField()
#     def __str__(self):
#         return f'EmailVerification object for {self.user.email}'
#
#     def send_verification_email(self):
#         link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
#         verification_link = f'{settings.DOMAIN_NAME}{link}'
#         subject = f'Подверждение учетной записи для {self.user.username}'
#         message = 'Для подверждения учетной записи для {} перейдите по ссылке: {}'.format(
#             self.user.email,
#             verification_link
#         )
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[self.user.email],
#             fail_silently=False,
#         )
#
#     def is_expired(self):
#         return True if now() >= self.expiration else False
