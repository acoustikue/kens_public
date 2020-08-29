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
# KensModule.py

# Vers 1, selenium type
# 08.22. Seems unnecessary. 
# from selenium import webdriver

# Vers 2, bs4 type
import requests
from bs4 import BeautifulSoup
import copy # Deep cpy

# regex, common
# import re # Well?

# import time
import os


project_banner = r'''[Project KENS] KU EE Notice Scraper
0.1.0va, 19.08.21. First tested, last update 19.08.17.
written by acoustikue(SukJoon Oh)
    __                                                             
   / /____  __   ___  ___     ___________________ _____  ___  _____
  / //_/ / / /  / _ \/ _ \   / ___/ ___/ ___/ __ `/ __ \/ _ \/ ___/
 / ,< / /_/ /  /  __/  __/  (__  ) /__/ /  / /_/ / /_/ /  __/ /    
/_/|_|\__,_/   \___/\___/  /____/\___/_/   \__,_/ .___/\___/_/     
                        _           __     __  /_/                 
    ____  _________    (_)__  _____/ /_   / /_____  ____  _____    
   / __ \/ ___/ __ \  / / _ \/ ___/ __/  / //_/ _ \/ __ \/ ___/    
  / /_/ / /  / /_/ / / /  __/ /__/ /_   / ,< /  __/ / / (__  )     
 / .___/_/   \____/_/ /\___/\___/\__/  /_/|_|\___/_/ /_/____/      
/_/              /___/                                             
                                                    
Visual Studio 2017 Professional Blank Python Project
'''


# added for linux system, for cron scheduler command
system_path_windows = os.getcwd() + '\\'
system_path_linux = os.getcwd() + '/'

system_path = system_path_windows

ku_ee_reqeust_url = 'http://ee.konkuk.ac.kr/noticeList.do?siteId=EE&boardSeq=424&menuSeq=2837'
ku_ee_exported_filename = system_path + 'notice.kens'
ku_ee_telegram_user_filename = system_path + 'user_telegram.kens'



# Getting response module
# Parameter: string(url)
# Returns: Response object from reqeust.get()
# Author: acoustikue
def KensGetHtmlText(url):

    print('[console] Sending requests...', end='')
    
    # Getting texts
    ku_ee_res = requests.get(url)
    print('Done, status code: ' + str(ku_ee_res.status_code))

    return ku_ee_res



#
# deprecated
def KensParseNoticeTitle(response):

    # Ready for parsing?
    print('[console] Parsing notice title...', end='')
    ku_soup = BeautifulSoup(response.text, 'html.parser')
    print(' Done. Printing title(list) of the first page.')
   
    link_list = ku_soup.find_all('a', class_='subject_click')
    
    index = 1

    for notice in link_list:
        print('    Index[' + str(index) + ']: ' + str(notice.text.lstrip()))

        index += 1

    return link_list



#
# deprecated
def KensParseNoticeDate(response):

    # Ready for parsing?
    print('[console] Parsing written dates...', end='')
    ku_soup = BeautifulSoup(response.text, 'html.parser')

    print(' Done. Printing date(list) of the first page.')

    date_list = ku_soup.find_all('td')


    index = 1

    for notice in date_list:
        print('    Index[' + str(index) + ']: ' + str(notice.text.lstrip()))

        index += 1

    return date_list



#
# main interface
# Parameter: Response object
# Returns: Dictionary type of parsed data.
# Author: acoustikue
def KensParseNotice(response):

    # Ready for parsing?
    print('[console] Parsing information...', end='')

    ku_soup = BeautifulSoup(response.text, 'html.parser')
    ku_soup = BeautifulSoup(str(ku_soup.find('table', class_='grid')), 'html.parser')

    print(' Done. Printing infos(list) of the first page.')
    

    list = ku_soup.find_all('td')
    #link = ku_soup.find_all('a')

    #print(link)

    # literally works as a structure.
    # Deep copy necessary.
    structure = {
        'NUMBER': '1',
        'TITLE': 'None', 
        'AUTHOR': 'None',
        'DATE': 'None',
        'SEEN': '0'
        }

    notice_info = []

    
    index = 0

    for info in list:

        if(index == 5): index = 0

        if index is 0: structure['NUMBER'] = str(info.text.lstrip()) 
        if index is 1: 
            structure['TITLE'] = str(info.text.lstrip())
            # structure['TITLE'] = str(info.text.lstrip().replace('\n', ''))
            # Memo: if parsed, there will be always '\n' at the end of every title.

        if index is 2: structure['AUTHOR'] = str(info.text.lstrip())
        if index is 3: structure['DATE'] = str(info.text.lstrip())
        if index is 4: 
            structure['SEEN'] = info.text.lstrip()
            notice_info.append(copy.deepcopy(structure))
            
        index += 1

    return notice_info



# Prerequisite for comparing function!
# Parameter: Dictionary type, parsed information.
# Returns: Array type of converted dictionary data.
# Author: acoustikue
def KensConvertDictToArrary(parsed_info):

    print('[console] Converting dictionary to array... ', end='')

    info_array = []

    for info in parsed_info:
        info_array.append(str(info['NUMBER']) + '\t' + str(info['DATE']) + '\t' + str(info['TITLE'].rstrip()))

    print(' Done converting.')

    return info_array



# tested.
# Parameter: Dictionary type of parsed data.
# Returns: -
# Author: acoustikue
def KensWriteInfo(info_dict):

    # saves information as texts
    with open(ku_ee_exported_filename, "w") as save_file:

        print('[console] Writing parsed information...', end='')

        for info in info_dict:
            save_file.write(str(info['NUMBER']) + '\t' + str(info['DATE']) + '\t' + str(info['TITLE']))

        print(' Done exporting.')



# tested.
# Parameter: File address, will be declrared in global scope
# Returns: Array type.
# Author: acoustikue
def KensReadInfo(file_addr):

    with open(file_addr, "r") as saved_file:

        print('[console] Reading previous information...')
        saved_info = saved_file.read().splitlines()

        # Removing '\n'
        for info in saved_info:
            print('\t  ' + info)

        print('[console] Done reading.')
        

    return saved_info        



# Comparing function
# Parameter: Array, Array
# Returns: Array of updated data.
# Author: acoustikue
def KensCompare(prev_notice, new_notice):

    is_in_list_flag = False
    updated_notice = [] # This is where different string will be stored

    # Double for scope will be fine,
    # since there is not much information.
    for new in new_notice:

        is_in_list_flag = False # set this first to False

        for prev in prev_notice:

            # if prev is same with new, 
            if prev == new:

                is_in_list_flag = True 
                # it is in the list, so set the flag to True

                break
        
        if is_in_list_flag is False: # if not found, then the string is updated string.

            print('[console] New notice updated: ' + new)
            updated_notice.append(new)

    return updated_notice
