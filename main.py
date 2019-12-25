from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id
import vk_api
import random
import requests
import sys
def Image_DownLoad(data):
    x = 0
    num = ''
    data = data[0]['attachments'][0]['photo']['sizes']
    for u in data:
        if u['width'] > x:
            x = u['width']
            num = u['url']
    return num


cmdl = ['commandlist', 'ok, boomer', '~hate', '~donthate', 'справедливо', '~getmeme']
adcmdl = ['~die', '~addphrase', '~addmeme']
mutel = [1]
adnicks = ['ferum', 'ferrum']
tokentxt = open('token.txt', 'r')
token = tokentxt.readline()
tokentxt.close()
admin = 107442155
hid = 0
Itself = 496547736
Valeria = 559330337
vk_session = vk_api.VkApi(token=token)

counttxt = open('count.txt', mode='r')
count = int(counttxt.readline())
counttxt.close()


vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.USER_TYPING and event.user_id != admin:
        vk.messages.send(user_id=event.user_id,
                         random_id=get_random_id(),
                         message="Чё пишешь, выблядок?")
    elif event.type == VkEventType.MESSAGE_NEW:
        x = (vk.messages.getById(message_ids=event.message_id, preview_length=0)['items'])[0]
    if event.type == VkEventType.MESSAGE_NEW and event.user_id == hid:
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
    elif event.type == VkEventType.MESSAGE_NEW and ('reply_message' in x) and cmdl[2] == event.text:
        if cmdl[2] == event.text.lower() and ((x['reply_message'])['from_id'] != admin != Valeria):
            hid = (x['reply_message'])['from_id']
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
    elif event.type == VkEventType.MESSAGE_NEW and event.attachments and ('reply_message' not in x) and event.user_id != admin and event.to_me:
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
    elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.user_id != Valeria and (cmdl[2] not in event.text) :
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
            if event.from_chat:
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
            meme = VkUpload(vk).photo_messages(photos=f'E:\VkBotD\memes\meme ({random.randint(1,2220)}).jpg')
            if event.from_user:
                vk.messages.send(user_id=event.user_id,
                                 random_id=get_random_id(),
                                 attachment=f'photo{meme[0]["owner_id"]}_{meme[0]["id"]}')
            elif event.from_chat:
                vk.messages.send(chat_id=event.chat_id,
                                 random_id=get_random_id(),
                                 attachment=f'photo{meme[0]["owner_id"]}_{meme[0]["id"]}')
        elif event.text.lower() == adcmdl[0] and event.user_id == admin:
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
        elif adcmdl[1] == event.text.lower() and event.user_id == admin:
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
        elif adcmdl[2] == event.text.lower() and event.user_id == admin:
            url_img = Image_DownLoad(vk.messages.getById(message_ids=event.message_id, preview_length=0)['items'])
            r = requests.get(url_img)
            out = open(f'E:\VkBotD\memes\meme ({count + 1}).jpg', "wb")
            out.write(r.content)
            out.close()
            count += 1
            counttxt = open('count.txt', mode='w')
            counttxt.writelines(str(count))
            counttxt.close()
            if event.from_user:
                vk.messages.send(user_id=event.user_id,
                                 random_id=get_random_id(),
                                 message="The meme is added")
            elif event.from_chat:
                vk.messages.send(chat_id=event.chat_id,
                                 random_id=get_random_id(),
                                 message="The meme is added")
        elif event.text not in adcmdl and event.user_id == admin and event.text[0] == "~":
            try:
                a = eval(event.text[1:])
            except:
                a =  sys.exc_info()[0]
            if event.from_user:
                vk.messages.send(user_id=event.user_id,
                                 random_id=get_random_id(),
                                 message=a)
            elif event.from_chat:
                vk.messages.send(chat_id=event.chat_id,
                                 random_id=get_random_id(),
                                 message=a)
        elif event.from_user and event.user_id != admin:
            vk.messages.sendSticker(user_id=event.user_id,
                                    random_id=get_random_id(),
                                    sticker_id=163)
#457247667
#457247662
#457247661
#457247624