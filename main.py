from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id
import vk_api
import random
import requests
import sys
from bs4 import BeautifulSoup
import time
def Image_DownLoad(data, count):
    x = 0
    url_img = ''
    data = data['photo']['sizes']
    for u in data:
        if u['width'] > x:
            x = u['width']
            url_img = u['url']
    r = requests.get(url_img)
    out = open(f'E:\VkBotD\memes\meme ({count + 1}).jpg', "wb")
    out.write(r.content)
    out.close()
    count += 1
    counttxt = open('count.txt', mode='w')
    counttxt.writelines(str(count))
    counttxt.close()

datatxt = open('data.txt', 'r')
token = str(datatxt.readline()[:-1])
vk_session = vk_api.VkApi(token=token)
cmdl = ['commandlist', 'ok, boomer', '~hate', '~donthate', 'справедливо', '~getmeme']
adcmdl = ['~die', '~addphrase', '~addmeme', '~addmute', '~delmute', 'da']
mutel = list(map(int, datatxt.readlines()[0:]))
adnicks = ['ferum', 'ferrum', '@ferwild']
datatxt.close()
Itself = 483032191
admin = 107442155
hid = 0
Valeria = 559330337
counttxt = open('count.txt', mode='r')
count = int(counttxt.readline())
counttxt.close()
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.USER_TYPING and event.user_id != admin and event.user_id*-1 not in mutel:
        vk.messages.send(user_id=event.user_id,
                         random_id=get_random_id(),
                         message="Чё пишешь, выбляд_Очка?")
    if event.type == VkEventType.MESSAGE_NEW and ((event.chat_id if event.from_chat else event.user_id*-1) not in mutel or event.user_id == admin):
        x = (vk.messages.getById(message_ids=event.message_id, preview_length=0)['items'])[0]
        if event.user_id == hid and not event.from_me:
            print(hid, '###', event.user_id)
            f = open('HPhrases.txt', mode='r', encoding='utf-8')
            phrases = f.readlines()
            if event.from_user:
                vk.messages.send(user_id=event.user_id,
                                 random_id=get_random_id(),
                                 message=phrases[random.randint(0, len(phrases)-1)],
                                 reply_to=event.message_id)
            elif event.from_chat:
                vk.messages.send(chat_id=event.chat_id,
                                 random_id=get_random_id(),
                                 message=phrases[random.randint(0, len(phrases)-1)],
                                 reply_to=event.message_id)
            f.close()
        elif ('reply_message' in x) and cmdl[2] == event.text.lower() and event.user_id != hid:
            hid = (x['reply_message'])['from_id']
            print(hid)
            if (hid == Itself) or (hid == admin) or (hid == Valeria):
                hid = event.user_id
                print(hid, '###', event.user_id)
            if event.from_user:
                vk.messages.send(user_id=event.user_id,
                                 random_id=get_random_id(),
                                 message="Ok",
                                 reply_to=event.message_id)
            elif event.from_chat:
                vk.messages.send(chat_id=event.chat_id,
                                 random_id=get_random_id(),
                                 message="Ok",
                                 reply_to=event.message_id)
        elif event.attachments and ('reply_message' not in x) and event.user_id != admin and event.to_me:
            print('yeah')
            if event.from_user:
                vk.messages.send(user_id=event.user_id,
                                 random_id=get_random_id(),
                                 message="Я бот, я видеть не могу, клоун&#129313;&#129313;&#129313;",
                                 reply_to=event.message_id)
            elif event.from_chat:
                vk.messages.send(chat_id=event.chat_id,
                                 random_id=get_random_id(),
                                 message="Я бот, я видеть не могу, клоун&#129313;&#129313;&#129313;",
                                 reply_to=event.message_id)
            print("yeah")
        elif event.to_me and event.text and event.user_id != Valeria and (cmdl[2] not in event.text):
            print(0)
            if event.text.lower() == cmdl[0]:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                     random_id=get_random_id(),
                                     message=cmdl)
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     random_id=get_random_id(),
                                     message=cmdl)
                print("cmdl[0]")
            elif event.text.lower() == cmdl[1]:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                     random_id=get_random_id(),
                                     message="Ok, zoomer")
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     random_id=get_random_id(),
                                     message="Ok, zoomer")
                print("cmdl[1]")
            elif cmdl[3] == event.text.lower() and (hid != event.user_id):
                hid = 0
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                     random_id=get_random_id(),
                                     message="Ok",
                                     reply_to=event.message_id)
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     random_id=get_random_id(),
                                     message="Ok",
                                     reply_to=event.message_id)
            elif (adnicks[0] or adnicks[1]) in event.text.lower():
                vk.messages.send(user_id=admin,
                                 random_id=get_random_id(),
                                 forward_messages=event.message_id)
                print('Ferum')
            elif event.text.lower() == cmdl[4]:
                if event.from_user:
                    vk.messages.sendSticker(user_id=event.user_id,
                                            random_id=get_random_id(),
                                            sticker_id=163,
                                            reply_to=event.message_id)
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     random_id=get_random_id(),
                                     sticker_id=163,
                                     reply_to=event.message_id)
            elif event.text.lower() == cmdl[5]:
                meme = VkUpload(vk).photo_messages(photos=f'E:\VkBotD\memes\meme ({random.randint(1,count)}).jpg')
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                     random_id=get_random_id(),
                                     attachment=f'photo{meme[0]["owner_id"]}_{meme[0]["id"]}')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     random_id=get_random_id(),
                                     attachment=f'photo{meme[0]["owner_id"]}_{meme[0]["id"]}')
            elif event.text.lower() == 'send last meme':
                meme = VkUpload(vk).photo_messages(photos=f'E:\VkBotD\memes\meme ({count}).jpg')
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                     random_id=get_random_id(),
                                     attachment=f'photo{meme[0]["owner_id"]}_{meme[0]["id"]}')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     random_id=get_random_id(),
                                     attachment=f'photo{meme[0]["owner_id"]}_{meme[0]["id"]}')
            elif event.user_id == admin:
                if event.text.lower() == adcmdl[0]:
                    if event.from_user:
                        vk.messages.send(user_id=event.user_id,
                                         random_id=get_random_id(),
                                         message='stopped')
                    elif event.from_chat:
                        vk.messages.send(chat_id=event.chat_id,
                                         random_id=get_random_id(),
                                         message='stopped')
                    print("adcmdl[0]")
                    break
                elif adcmdl[1] in event.text.lower():
                    f = open('HPhrases.txt', mode='a', encoding='utf-8')
                    hphrase = event.text[len(adcmdl[1])+1:]
                    f.write('\n'+hphrase)
                    f.close()
                    if event.from_user:
                        vk.messages.send(user_id=event.user_id,
                                         random_id=get_random_id(),
                                         message=f"'{hphrase}' added")
                    elif event.from_chat:
                        vk.messages.send(chat_id=event.chat_id,
                                         random_id=get_random_id(),
                                         message=f"'{hphrase}' added")
                elif adcmdl[2] == event.text.lower():
                    for i in x['attachments']:
                        Image_DownLoad(i, count)
                        count += 1
                    if event.from_user:
                        vk.messages.send(user_id=event.user_id,
                                         random_id=get_random_id(),
                                         message="added")
                    elif event.from_chat:
                        vk.messages.send(chat_id=event.chat_id,
                                         random_id=get_random_id(),
                                         message="added")
                elif adcmdl[3] == event.text.lower():
                    if x['fwd_messages'] != {}:
                        datatxt = open('data.txt', 'w')
                        for i in x['fwd_messages']:
                            print(i['from_id'])
                            mutel.append(i['from_id']*-1)
                        mutel = list(set(mutel))
                        lines = token + '\n' + '\n'.join(map(str, mutel)) + '\n'
                        datatxt.writelines(lines)
                        datatxt.close()
                    else:
                        datatxt = open('data.txt', 'w')
                        mutel.append(event.chat_id)
                        mutel = list(set(mutel))
                        lines = token + '\n' + '\n'.join(map(str, mutel)) + '\n'
                        datatxt.writelines(lines)
                        datatxt.close()
                    if event.from_user:
                        vk.messages.send(user_id=event.user_id,
                                         random_id=get_random_id(),
                                         message="added")
                    elif event.from_chat:
                        vk.messages.send(chat_id=event.chat_id,
                                         random_id=get_random_id(),
                                         message="added")
                elif adcmdl[4] == event.text.lower():
                    if x['fwd_messages'] != {}:
                        lines = token + '\n'
                        datatxt = open('data.txt', 'w')
                        for i in x['fwd_messages']:
                            try:
                                mutel.remove(i['from_id']*-1)
                            except ValueError:
                                if event.from_user:
                                    vk.messages.send(user_id=event.user_id,
                                                     random_id=get_random_id(),
                                                     message=f"@id{i['from_id']} is not in the mute list")
                                elif event.from_chat:
                                    vk.messages.send(chat_id=event.chat_id,
                                                     random_id=get_random_id(),
                                                     message=f"@id{i['from_id']} is not in the mute list")
                            else:
                                if event.from_user:
                                    vk.messages.send(user_id=event.user_id,
                                                     random_id=get_random_id(),
                                                     message="deleted")
                                elif event.from_chat:
                                    vk.messages.send(chat_id=event.chat_id,
                                                     random_id=get_random_id(),
                                                     message="deleted")
                        mutelstr = map(str, mutel)
                        if len(mutel) > 0:
                            lines += '\n'.join(mutelstr) + '\n'
                        datatxt.writelines(lines)
                        datatxt.close()
                    else:
                        try:
                            mutel.remove(event.chat_id)
                        except ValueError:
                            if event.from_user:
                                vk.messages.send(user_id=event.user_id,
                                                 random_id=get_random_id(),
                                                 message=f"chat{event.chat_id} is not in the mute list")
                            elif event.from_chat:
                                vk.messages.send(chat_id=event.chat_id,
                                                 random_id=get_random_id(),
                                                 message=f"chat{event.chat_id} is not in the mute list")
                        else:
                            datatxt = open('data.txt', 'w')
                            mutelstr = map(str, mutel)
                            if len(mutel) > 0:
                                lines = token + '\n' + '\n'.join(mutelstr) + '\n'
                            else:
                                lines = token + '\n'
                            datatxt.writelines(lines)
                            datatxt.close()
                            if event.from_user:
                                vk.messages.send(user_id=event.user_id,
                                                 random_id=get_random_id(),
                                                 message="deleted")
                            elif event.from_chat:
                                vk.messages.send(chat_id=event.chat_id,
                                                 random_id=get_random_id(),
                                                 message="deleted")
                elif adcmdl[5] == event.text.lower():
                    r = requests.get('https://m.vk.com/audio496547736_456239026_218cda37cb6e27eb39')
                    out = open(f'E:\VkBotD\yeah.txt', "wb")
                    out.write(r.content)
                    out.close()
                elif event.text[0] == "~":
                    try:
                        a = eval(event.text[1:])
                    except:
                        a = sys.exc_info()[0]

                    try:
                        vk.messages.send(user_id=event.user_id,
                                         random_id=get_random_id(),
                                         message=a)
                    except AttributeError:
                        vk.messages.send(chat_id=event.chat_id,
                                         random_id=get_random_id(),
                                         message=a)
                    except:
                        try:
                            vk.messages.send(user_id=event.user_id,
                                             random_id=get_random_id(),
                                             message='Done')
                        except AttributeError:
                            vk.messages.send(chat_id=event.chat_id,
                                             random_id=get_random_id(),
                                             message='Done')
            elif event.message_id % 100 == 0:
                f = open('DPhrases.txt', mode='r', encoding='utf-8')
                phrases = f.readlines()
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                     random_id=get_random_id(),
                                     message=phrases[random.randint(0, len(phrases) - 1)])
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     random_id=get_random_id(),
                                     message=phrases[random.randint(0, len(phrases) - 1)])
                f.close()
            elif event.from_user:
                vk.messages.sendSticker(user_id=event.user_id,
                                        random_id=get_random_id(),
                                        sticker_id=163)
        print(event.text, event.message_id)
