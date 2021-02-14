from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=250, verbose_name='ТГ токен')
    tg_chat_id = models.CharField(max_length=100, verbose_name='Чат ID')
    tg_text = models.TextField(max_length=4096, verbose_name='Текст', help_text='Не более 4096 символов!')

    def __str__(self):
        return self.tg_chat_id

    class Meta:
        verbose_name = 'Настройки ТГ'
        verbose_name_plural = 'Настройки ТГ'