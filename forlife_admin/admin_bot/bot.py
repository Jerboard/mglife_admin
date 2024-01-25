import logging

import telebot
import logger
from telebot import types
from forlife_admin.settings import TOKEN_BOT
from admin_bot.models import Chat

# создаёт бот с искомым токеном
bot = telebot.TeleBot(TOKEN_BOT)


def get_url_kb():
    print('get_url_kb')
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton (
            text='Получить доступ',
            url="https://t.me/addlist/blMG7Iz-gstjOGNi")
        )


def ban_user_chats(user_id: int):
    all_chats = Chat.objects.all ()
    for chat in all_chats:
        try:
            bot.ban_chat_member(chat_id=chat.chat_id, user_id=user_id)
        except:
            pass


def send_gold_list(user_id: int):
    all_chats = Chat.objects.all ()
    for chat in all_chats:
        try:
            bot.unban_chat_member (
                chat_id=chat,
                user_id=user_id,
                only_if_banned=True)
        except:
            pass

    text = ('Поздравляю с покупкой ЗОЛОТОЙ КАРТЫ\n\n'
            'Для получения доступа нажмите на кнопку 👇🏻')

    try:
        bot.send_message(
            chat_id=user_id,
            text=text,
            disable_web_page_preview=True,
            reply_markup=get_url_kb ()
        )
    except Exception as ex:
        logging.warning(f'Не отправил сообщение {user_id}\n{ex}')

