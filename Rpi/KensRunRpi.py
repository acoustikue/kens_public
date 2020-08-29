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
# KensRun.py

from KensModuleRpi import *
from KensTelegramRpi import *




# main
if __name__ == '__main__':

    # I like these kinds.
    print(project_banner)

    # Initiated telegram bot
    kens_bot = KensTelegramInit()
    kens_bot_chat_id_list = KensTelegramChatIdList2(kens_bot) # chat id

    ku_ee_html_text = KensGetHtmlText(ku_ee_reqeust_url)
    

    new_info_dict = KensParseNotice(ku_ee_html_text)
    new_info = KensConvertDictToArrary(new_info_dict)
    # KensWriteInfo(new_info)

    # print(KensConvertDictToArrary(info))

    #for list in info:
    #    print(list)

    prev_info = KensReadInfo(ku_ee_exported_filename)
    
    updated_info = KensCompare(prev_info, new_info)

    if len(updated_info) is not 0:
        KensWriteInfo(new_info_dict)

        # Sending message
        KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, KensTelegramMakeMessage(updated_info))

    else:
        # Sending message
        # KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, KensTelegramMakeMessage(updated_info))
        pass

    quit()



