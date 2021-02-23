import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"


def main():
    vk_session = vk_api.VkApi(
        token='ec296fa79437a9580df4749cb3c9e10b34ac677b5b9941bdddaafe2f1b53136e78a212e4a9327d925711a')

    longpoll = VkBotLongPoll(vk_session, '202478177')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            if event.obj.message['text'].startswith('!рандом'):
                if event.from_user:
                    vk.messages.send(user_id=event.obj['user_id'],
                                     message=f"{random.randint(0, 100)}",
                                     random_id=random.randint(0, 2 ** 64))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"{random.randint(0, 100)}",
                                     random_id=random.randint(0, 2 ** 64))

            elif event.obj.message['text'].startswith('!орёл и решка') or event.obj.message['text'].startswith('!орел и решка'):
                answer = random.randint(1, 2)
                if answer == 1:
                    answer = 'орёл'
                else:
                    answer = "решка"
                if event.from_user:
                    vk.messages.send(user_id=event.obj['user_id'],
                                     message=f"{answer}",
                                     random_id=random.randint(0, 2 ** 64))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"{answer}",
                                     random_id=random.randint(0, 2 ** 64))

            elif event.obj.message['text'].startswith('!колбасу халяль куриную мне за 90 рублей'):
                if event.from_user:
                    vk.messages.send(user_id=event.obj['user_id'],
                                     message=f"🌭",
                                     random_id=random.randint(0, 2 ** 64))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"🌭",
                                     random_id=random.randint(0, 2 ** 64))

            elif event.obj.message['text'].startswith('!погода'):
                text = event.obj.message['text'][7:].split()

                querystring = {"lon": f"{text[0]}", "lat": f"{text[1]}", "units": "metric", "lang": "ru"}

                headers = {
                    'x-rapidapi-key': "2d20230fbcmsh61ffa2964aaa8a8p1f15ddjsne21c28b55a93",
                    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
                }

                response = requests.request("GET", url, headers=headers, params=querystring)

                if event.from_user:
                    vk.messages.send(user_id=event.obj['user_id'],
                                     message=f"{response.text}",
                                     random_id=random.randint(0, 2 ** 64))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"{response.text}",
                                     random_id=random.randint(0, 2 ** 64))
# https://rapidapi.com/weatherbit/api/weather/endpoints


if __name__ == '__main__':
    main()