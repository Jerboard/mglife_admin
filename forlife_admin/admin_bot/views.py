from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

from admin_bot.models import User
from admin_bot.bot import ban_user_chats, send_gold_list
from forlife_admin.settings import API_KEY
from logger import save_log

tariff_dict = {3297203: 'gold', 3325243: 'silver', 3329565: 'part-gold'}


# приём запросов
def api_view(request: HttpRequest):
    if request.GET:
        data = request.GET
        # print(data)
        # если кривой ключ
        if data['key'] != API_KEY:
            save_log (f'{data}\nInvalid API key')
            return JsonResponse({'error': 'Invalid API key'}, status=403)

        else:
            # добавляет пользователя
            if data['add_user'] == '1':
                tariff = tariff_dict.get(int(data['list_id']))
                if tariff == 'gold':
                    try:
                        user = User.objects.filter(gc_id=int(data['gc_id'])).first()
                    except Exception as ex:
                        return JsonResponse ({'info': f'invalid gc_id: {data.get("gc_id")}'}, status=403)

                    if user and user.list != 'gold':
                        send_gold_list(user.tg_id)
                        user.list = 'gold'
                        user.save()
                        save_log (f'{data}\nstatus user {user.tg_id} updated')
                        return JsonResponse ({'info': f'status user {user.tg_id} updated'}, status=200)

                    elif user:
                        return JsonResponse ({'info': f'user already exist {user.tg_id}'}, status=200)

                if tariff:
                    user_info = User.objects.filter(email=data['email']).first()
                    if not user_info:

                        User.objects.create(
                            status='free',
                            list=tariff,
                            email=data['email'],
                            gc_id=data['gc_id']
                        )

                        save_log (f'{data}\nuser gc {data["gc_id"]} added')
                        return JsonResponse ({'info': f'user gc {data["gc_id"]} added'}, status=200)

                save_log (f'{data}\nInvalid list ID  {data ["list_id"]}')
                return JsonResponse ({'info': f'Invalid list ID  {data ["list_id"]}'}, status=403)

            # удаляет пользователя
            elif data['add_user'] == '0':
                del_user = User.objects.filter(gc_id=int(data['gc_id']))
                if del_user:
                    del_user_id = del_user.tg_id
                    del_user.delete()
                    ban_user_chats(user_id=del_user_id)
                    save_log (f'{data}\nuser {del_user_id} deleted')
                    return JsonResponse ({'info': f'user {del_user_id} deleted'}, status=200)

                else:
                    save_log (f'{data}\nuser for delete not found')
                    return JsonResponse ({'info': f'user for delete not found'}, status=403)

            save_log (f'{data}\nlist ID invalid')
            return JsonResponse({'info': 'list ID invalid'}, status=403)

    else:
        save_log (f'Invalid request method')
        return JsonResponse({'error': 'Invalid request method'}, status=400)
