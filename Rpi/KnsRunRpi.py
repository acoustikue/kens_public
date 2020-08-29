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


from KnsModuleRpi import *
from KensTelegramRpi import *

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
    ku_html_text.append(copy.deepcopy('Dummy'))
    ku_html_text.append(copy.deepcopy(KnsGetHtmlText(ku_request_urls[3]))) # Guukjae
    ku_html_text.append(copy.deepcopy(KnsGetHtmlText(ku_request_urls[4]))) # Haksaeng
    ku_html_text.append(copy.deepcopy('Dummy'))
    ku_html_text.append(copy.deepcopy(KnsGetHtmlText(ku_request_urls[6]))) # Ilban


    # Getting information in dict type
    new_info_dict_haksa = KnsParseNoticeHaksa(ku_html_text[0])
    new_info_dict_janghak = KnsParseNoticeJanghak(ku_html_text[1])
    # new_info_dict_changup Needs to be implemented
    new_info_dict_guukjae = KnsParseNoticeGuukjae(ku_html_text[3]) 
    new_info_dict_haksaeng = KnsParseNoticeGuukjae(ku_html_text[4]) 
    # new_info_dict_sanhak Needs to be implemented
    new_info_dict_ilban = KnsParseNoticeIlban(ku_html_text[6]) 



    # converted data
    new_info_haksa = KnsConvertDictToArrary(new_info_dict_haksa)
    new_info_janghak = KnsConvertDictToArrary(new_info_dict_janghak)
    # new_info_changup Needs to be implemented
    new_info_guukjae = KnsConvertDictToArrary(new_info_dict_guukjae)
    new_info_haksaeng = KnsConvertDictToArrary(new_info_dict_haksaeng)
    # new_info_dict_sanhak Needs to be implemented
    new_info_ilban = KnsConvertDictToArrary(new_info_dict_ilban) 


    # 
    # Previous information
    prev_info_haksa = KnsReadInfo(ku_exported_filename_haksa)
    updated_info_haksa = KnsCompare(prev_info_haksa, new_info_haksa)

    prev_info_janghak = KnsReadInfo(ku_exported_filename_janghak)
    updated_info_janghak = KnsCompare(prev_info_janghak, new_info_janghak)

    prev_info_guukjae = KnsReadInfo(ku_exported_filename_guukjae)
    updated_info_guukjae = KnsCompare(prev_info_guukjae, new_info_guukjae)
    
    prev_info_haksaeng = KnsReadInfo(ku_exported_filename_haksaeng)
    updated_info_haksaeng = KnsCompare(prev_info_haksaeng, new_info_haksaeng)

    prev_info_ilban = KnsReadInfo(ku_exported_filename_ilban)
    updated_info_ilban = KnsCompare(prev_info_ilban, new_info_ilban)



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
        KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, KnsTelegramMakeMessageJanghak(updated_info_haksa))

    if len(updated_info_guukjae) is not 0: 
        KnsWriteInfo(new_info_dict_guukjae, ku_exported_filename_guukjae)
        # Sending message
        KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, KnsTelegramMakeMessageGuukjae(updated_info_guukjae))

    if len(updated_info_haksaeng) is not 0: 
        KnsWriteInfo(new_info_dict_haksaeng, ku_exported_filename_haksaeng)
        # Sending message
        KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, KnsTelegramMakeMessageHaksaeng(updated_info_haksaeng))
    
    if len(updated_info_ilban) is not 0:
        KnsWriteInfo(new_info_dict_ilban, ku_exported_filename_ilban)
        # Sending message
        KensTelegramSendMessage(kens_bot, kens_bot_chat_id_list, KnsTelegramMakeMessageIlban(updated_info_ilban))



    quit()