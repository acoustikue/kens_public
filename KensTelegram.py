# [Project KENS]KU EE Notice Scraper
# 0.1.1va, 19.08.21. First tested, last update 19.08.23.
# written by acoustikue(SukJoon Oh)
#                                 __  _ __            
#    ____ __________  __  _______/ /_(_) /____  _____ 
#   / __ `/ ___/ __ \/ / / / ___/ __/ / //_/ / / / _ \
#  / /_/ / /__/ /_/ / /_/ (__  ) /_/ / ,< / /_/ /  __/
#  \__,_/\___/\____/\__,_/____/\__/_/_/|_|\__,_/\___/ 
#                                                     
# Visual Studio 2017 Professional Blank Python Project
# KensTelegram.py


# Done! Congratulations on your new bot. 
# You will find it at t.me/KENS_bot. 
# You can now add a description, about section and profile picture for your bot, see /help for a list of commands. 
# By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. 
# Just make sure the bot is fully operational before you do this.

# Use this token to access the HTTP API:
# Keep your token secure and store it safely, it can be used by anyone to control your bot.

# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

# acoustikue, important!!
# First install API
# pip install python-telegram-bot


import telegram

from KensModule import *
import copy


#
# Test module
# Parameter: -
# Returns: Bot object
# Author: acoustikue
def KensTelegramInit():

    print('[console] KENS_bot telegram initiated.')
    bot = telegram.Bot(token='')

    # chat_id = bot.getUpdates()[-1].message.chat.id

    return bot

#
# Parameter: Bot
# Returns: chat id
# Author: acoustikue
# --Previous Version
def KensTelegramChatIdList(kens_bot):

    id_list = []
    # firstname_list = []

    user_list = kens_bot.getUpdates()

    for user in user_list:

        if str(user.message.chat.id) in user_list: 
            # search if id is in the list
            pass

        else:
            # search if id is not in the list
            id_list.append(str(user.message.chat.id))

    # print(id_list)
        #pass

    return id_list





#
# Parameter: Bot
# Returns: -
# Author: acoustikue
def KensTelegramReadAndCheckUser():

    id_list = []

    with open(ku_ee_telegram_user_filename, "r") as user_file:

        # read saved user list
        saved_info = user_file.read().splitlines()
        
    print('[console] Saved user list: ')

    for list in saved_info:

        id_list.append(str(list))
        print('\t ' + str(list))

    return id_list




#
# Parameter: Bot
# Returns: -
# Author: acoustikue
def KensTelegramWriteUser(kens_bot):

    id_list = KensTelegramReadAndCheckUser()
    # firstname_list = []

    user_list = kens_bot.getUpdates()

    with open(ku_ee_telegram_user_filename, "a") as user_file:
        for user in user_list:

            chat_id = str(user.message.chat.id)

            if str(chat_id) in id_list: 
                # search if id is in the list
                print('[console] ID(' + str(chat_id) + ') is in the list.')
                

            else:

                print('[console] New ID: ' + str(chat_id))
                # search if id is not in the list
                id_list.append(str(chat_id))
                # exports id_list
                user_file.write(str(chat_id) + '\n')

        # avoids multiple duplicates
        # id_list = list(set(id_list))
    return id_list



#
# Parameter: Bot
# Returns: chat id
# Author: acoustikue
# --Previous Version
def KensTelegramChatIdList2(kens_bot):

    return KensTelegramWriteUser(kens_bot)



# Parameter: -
# Returns: -
# Author: acoustikue
def KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, message):

    for chat_id in kens_bot_chat_id_list:

        print('[console] Sending message to chat id: ' + str(chat_id))
        kens_bot.sendMessage(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.HTML)




# Parameter: -
# Returns: -
# Author: acoustikue
def KensTelegramMakeMessage(updated_list):

    pre = '<b>건국대학교 전기전자공학부 공지 알림봇입니다.</b>\n'
    pre += '<a href="http://ee.konkuk.ac.kr/noticeList.do?siteId=EE&boardSeq=424&menuSeq=2837">홈페이지 이동하기</a>\n\n'

    message = '' + pre

    # This function makes message to send
    if len(updated_list) is 0:
        message += '업데이트가 없습니다.'

    else:

        message += '업데이트 사항입니다.\n'

        index = 1

        for info in updated_list:

            token = info.split('\t')
            
            if token[0] == '[공지]':
                message += (str(index) + ' : <b>' + str(token[0]) + '</b> <i>' + str(token[-1]) + '</i>\n')
            
            else:
                message += (str(index) + ' : ' + str(token[-1]) + '\n')

            index += 1
            

    return message



# From here, this is additional function for kns module.
# Just import this file to use function below

# Parameter: -
# Returns: -
# Author: acoustikue
def KnsTelegramMakeMessageHaksa(updated_list):

    pre = '<b>[KNS] 건국대학교 전기전자공학부 공지 알림봇입니다.</b>\n'
    pre += '<a href="http://konkuk.ac.kr">건국대학교 홈페이지 이동하기</a>\n\n'

    message = '' + pre

    # This function makes message to send
    if len(updated_list) is 0:
        message += '[학사] 업데이트가 없습니다.'

    else:

        message += '<b>학사</b> 업데이트 사항입니다.\n'

        index = 1

        for info in updated_list:

            token = info.split('\t')
            
            if token[0] == 'None':
                message += ('<b>[공지]</b> <i>' + str(token[-1]) + '</i>\n')
            
            else:
                message += (str(index) + ' : ' + str(token[-1]) + '\n')

            index += 1
            

    return message


# Parameter: -
# Returns: -
# Author: acoustikue
def KnsTelegramMakeMessageJanghak(updated_list):

    pre = '<b>[KNS] 건국대학교 전기전자공학부 공지 알림봇입니다.</b>\n'
    pre += '<a href="http://konkuk.ac.kr">건국대학교 홈페이지 이동하기</a>\n\n'

    message = '' + pre

    # This function makes message to send
    if len(updated_list) is 0:
        message += '<b>장학</b> 업데이트가 없습니다.'

    else:

        message += '<b>장학</b> 업데이트 사항입니다.\n'

        index = 1

        for info in updated_list:

            token = info.split('\t')
            
            if token[0] == 'None':
                message += ('<b>[공지]</b> <i>' + str(token[-1]) + '</i>\n')
            
            else:
                message += (str(index) + ' : ' + str(token[-1]) + '\n')

            index += 1
            

    return message




# Parameter: -
# Returns: -
# Author: acoustikue
def KnsTelegramMakeMessageGuukjae(updated_list):

    pre = '<b>[KNS] 건국대학교 전기전자공학부 공지 알림봇입니다.</b>\n'
    pre += '<a href="http://konkuk.ac.kr">건국대학교 홈페이지 이동하기</a>\n\n'

    message = '' + pre

    # This function makes message to send
    if len(updated_list) is 0:
        message += '<b>국제</b> 업데이트가 없습니다.'

    else:

        message += '<b>국제</b> 업데이트 사항입니다.\n'

        index = 1

        for info in updated_list:

            token = info.split('\t')
            
            if token[0] == 'None':
                message += ('<b>[공지]</b> <i>' + str(token[-1]) + '</i>\n')
            
            else:
                message += (str(index) + ' : ' + str(token[-1]) + '\n')

            index += 1
            

    return message



# Parameter: -
# Returns: -
# Author: acoustikue
def KnsTelegramMakeMessageHaksaeng(updated_list):

    pre = '<b>[KNS] 건국대학교 전기전자공학부 공지 알림봇입니다.</b>\n'
    pre += '<a href="http://konkuk.ac.kr">건국대학교 홈페이지 이동하기</a>\n\n'

    message = '' + pre

    # This function makes message to send
    if len(updated_list) is 0:
        message += '<b>학생</b> 업데이트가 없습니다.'

    else:

        message += '<b>학생</b> 업데이트 사항입니다.\n'

        index = 1

        for info in updated_list:

            token = info.split('\t')
            
            if token[0] == 'None':
                message += ('<b>[공지]</b> <i>' + str(token[-1]) + '</i>\n')
            
            else:
                message += (str(index) + ' : ' + str(token[-1]) + '\n')

            index += 1
            

    return message




# Parameter: -
# Returns: -
# Author: acoustikue
def KnsTelegramMakeMessageIlban(updated_list):

    pre = '<b>[KNS] 건국대학교 전기전자공학부 공지 알림봇입니다.</b>\n'
    pre += '<a href="http://konkuk.ac.kr">건국대학교 홈페이지 이동하기</a>\n\n'

    message = '' + pre

    # This function makes message to send
    if len(updated_list) is 0:
        message += '<b>일반</b> 업데이트가 없습니다.'

    else:

        message += '<b>일반</b> 업데이트 사항입니다.\n'

        index = 1

        for info in updated_list:

            token = info.split('\t')
            
            if token[0] == 'None':
                message += ('<b>[공지]</b> <i>' + str(token[-1]) + '</i>\n')
            
            else:
                message += (str(index) + ' : ' + str(token[-1]) + '\n')

            index += 1
            

    return message






if __name__ == '__main__':

    print('[console] KensTelegram.py test script.')
    

    kens_bot = KensTelegramInit()
    # kens_bot_chat_id_list = KensTelegramChatIdList(kens_bot) # chat id
    # kens_bot_chat_id_list = KensTelegramReadAndCheckUser() # chat id
    KensTelegramWriteUser(kens_bot)

    






