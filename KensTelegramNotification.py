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
# KensTelegramNotification.py

from KensTelegram import *


server_test_pre_message = '''<b>[공지사항]</b>
건국대학교 전기전자공학부 알림 봇 서버 점검으로 인한 서비스 중단 안내드립니다.

서비스 점검: <b>금일 메세지 발송 후 약 2시간</b>

서비스 이용에 불편을 드려 죄송합니다. 
빠른 시간 내에 서비스가 다시 제공될 수 있도록 노력하겠습니다. 

<i>관리자 올림.</i>
'''

server_test_post_message = '''<b>[공지사항]</b>
건국대학교 전기전자공학부 알림 봇 서버 점검 완료로 인한 서비스 재개 안내드립니다.

현 시간 부로 서비스 제공이 <b>재개</b>되었습니다.

<i>관리자 올림.</i>
'''

server_test_log_message_1 = '''<b>[공지사항]</b>
건국대학교 전기전자공학부 알림 봇 서비스 업데이트 로그 안내드립니다.

2019.08.21. <b>Version: 0.1.0va</b>
- Project KENS initiated, author(SukJoon Oh)

2019.08.24. <b>Version: 0.1.1va</b>
- Telegram ID saving function added. No more receiving only recent ID's, preventing skipping sending messages for random ID's.
- Administrator notification service module added.
- Fixed giving alert every hour, even there's no updated information in the notice board.


'''

server_test_log_message_2 = '''<b>[공지사항]</b>
건국대학교 전기전자공학부 알림 봇 서비스 업데이트 로그 안내드립니다.

2019.08.25. <b>Version: 0.1.3vb</b>
- KNS on KENS project successfully tested. Version upgraded to BETA.
- Hello KNS! New service has been launched. This project is named KNS(Konkuk Univ Notice board Scraper). It is mainly focused on scraping main homepage notice board, where as KENS is only for the EE homepage.
- 0.1.3vb is beta version, so it only sends notification of Haksa and Janghak section, but other tabs will be supported in the later version.
- Directory scanning process added, for convenience in launching server.
'''


server_test_log_message_3 = '''<b>[공지사항]</b>
건국대학교 전기전자공학부 알림 봇 서비스 업데이트 로그 안내드립니다.

2019.08.25. <b>Version: 0.1.6vb</b>
- KNS on KENS project updated! Now more tabs are supported.
- Guukjae, haksaeng, ilban tab support was added. Other remaining tabs need a slight different algorithm, so please wait for later update.
- Note that this service is still BETA, so there might be unexpected actions, for instance KNS catches even a slight modifications of a string in a single title. This will be fixed in the later update.
'''

    

if __name__ == '__main__':

    kens_bot = KensTelegramInit()
    kens_bot_chat_id_list = KensTelegramChatIdList2(kens_bot) # chat id

    # sends infos
    # KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, server_test_pre_message)
    KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, server_test_post_message)
    # KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, server_test_log_message_1)
    KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, server_test_log_message_2)

    # Only to Admin
    # ['706386870'] Administrator Chat ID
    #KensTelegramSendMessage(kens_bot, ['706386870'], server_test_pre_message)
    #KensTelegramSendMessage(kens_bot, ['706386870'], server_test_post_message)
    #KensTelegramSendMessage(kens_bot, ['706386870'], server_test_log_message_1)
    # KensTelegramSendMessage(kens_bot, ['706386870'], server_test_log_message_2)