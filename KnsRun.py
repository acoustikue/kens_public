# [Project KNS]KU Notice Scraper
# 0.1.2va, 19.08.24. First tested, last update 19.08.24.
# written by acoustikue(SukJoon Oh)
#                                 __  _ __            
#    ____ __________  __  _______/ /_(_) /____  _____ 
#   / __ `/ ___/ __ \/ / / / ___/ __/ / //_/ / / / _ \
#  / /_/ / /__/ /_/ / /_/ (__  ) /_/ / ,< / /_/ /  __/
#  \__,_/\___/\____/\__,_/____/\__/_/_/|_|\__,_/\___/ 
#                                                     
# Visual Studio 2017 Professional Blank Python Project
# kns.py


from KnsModule import *
from KensTelegram import *

import copy

# main
if __name__ == '__main__':

    # I like these kinds.
    print(project_banner)

    # Initiated telegram bot
    kens_bot = KensTelegramInit()
    kens_bot_chat_id_list = KensTelegramChatIdList2(kens_bot) # chat id

    # Starting service
    ku_html_text = []
    ku_html_text.append(copy.deepcopy(KnsGetHtmlText(ku_request_urls[0]))) # Haksa
    ku_html_text.append(copy.deepcopy(KnsGetHtmlText(ku_request_urls[1]))) # Janghak


    new_info_dict_haksa = KnsParseNoticeHaksa(ku_html_text[0])
    new_info_dict_janghak = KnsParseNoticeJanghak(ku_html_text[1])

    # converted data
    new_info_haksa = KnsConvertDictToArrary(new_info_dict_haksa)
    new_info_janghak = KnsConvertDictToArrary(new_info_dict_janghak)


    # Previous information
    prev_info_haksa = KnsReadInfo(ku_exported_filename_haksa)
    updated_info_haksa = KnsCompare(prev_info_haksa, new_info_haksa)

    prev_info_janghak = KnsReadInfo(ku_exported_filename_janghak)
    updated_info_janghak = KnsCompare(prev_info_janghak, new_info_janghak)



    #print('[console] Printing parsed Haksa board information...')
    #for info in new_info_haksa:
    #    print('\t ' + str(info))
    
    #print('[console] Printing parsed Janghak board information...')
    #for info in new_info_janghak:
    #    print('\t ' + str(info))

    # if not updated, then write it!!
    
    if len(updated_info_haksa) is not 0: 
        KnsWriteInfo(new_info_dict_haksa, ku_exported_filename_haksa)

        # Sending message
        KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, KnsTelegramMakeMessageHaksa(updated_info_haksa))

    if len(updated_info_janghak) is not 0: 
        KnsWriteInfo(new_info_dict_janghak, ku_exported_filename_janghak)
    
        # Sending message
        KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, KnsTelegramMakeMessageJanghak(updated_info_janghak))
    

    quit()