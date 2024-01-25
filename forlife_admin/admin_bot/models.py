from django.db import models


# таблица пользователи
class User(models.Model):
    id = models.AutoField('ID', primary_key=True)
    tg_id = models.IntegerField('ID пользователя', null=True, blank=True)
    full_name = models.CharField('Имя пользователя', max_length=255, null=True, blank=True)
    username = models.CharField('Username', max_length=64, null=True, blank=True)
    status = models.CharField('Статус', max_length=50, null=True, blank=True, default='free')
    gc_id = models.IntegerField('ID getcourse', null=True, blank=True)
    email = models.CharField('Почта', max_length=255, null=True, blank=True)
    list = models.CharField ('Список', max_length=255, null=True, blank=True)

    def __int__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'
        managed = False


# таблица пользователи
class Chat(models.Model):
    id = models.AutoField('ID', primary_key=True)
    chat_id = models.IntegerField('ID чата', null=True, blank=True)

    def __int__(self):
        return self.chat_id

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        db_table = 'chats'
        managed = False
