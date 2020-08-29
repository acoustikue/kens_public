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
# KnsModule.py

# Vers 2, bs4 type
import requests
from bs4 import BeautifulSoup
import copy # Deep cpy

import os


project_banner = r'''[Project KNS] KU EE Notice Scraper
0.1.1va, 19.08.21. First tested, last update 19.08.24.
written by acoustikue(SukJoon Oh)
    __                                                    
   / /____  __   ___________________ _____  ___  _____    
  / //_/ / / /  / ___/ ___/ ___/ __ `/ __ \/ _ \/ ___/     
 / ,< / /_/ /  (__  ) /__/ /  / /_/ / /_/ /  __/ /         
/_/|_|\__,_/  /____/\___/_/   \__,_/ .___/\___/_/          
                        _         /_/_     __              
    ____  _________    (_)__  _____/ /_   / /______  _____ 
   / __ \/ ___/ __ \  / / _ \/ ___/ __/  / //_/ __ \/ ___/ 
  / /_/ / /  / /_/ / / /  __/ /__/ /_   / ,< / / / (__  )  
 / .___/_/   \____/_/ /\___/\___/\__/  /_/|_/_/ /_/____/   
/_/              /___/                                     
 
Visual Studio 2017 Professional Blank Python Project
'''


ku_request_urls = [
    'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=notice&cat=0000300001', # Haksa
    'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=11688412', # Janghak
    'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=11731332', # Changup
    'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=notice&cat=0000300002', # Guukjae
    'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=notice&cat=0000300003', # Haksaeng
    'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=65659&cat=0010300001', # Sanhak
    'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=notice&cat=0000300006' # Iilban
    ]

# added for linux system, for cron scheduler command
system_path_windows = os.getcwd() + '\\kns\\'
system_path_linux = os.getcwd() + '/'

system_path = system_path_linux

ku_exported_filename_haksa = '/home/pi/Desktop/git/project_kens/Rpi/notice_haksa.kns'
ku_exported_filename_janghak = '/home/pi/Desktop/git/project_kens/Rpi/notice_janghak.kns'
ku_exported_filename_changup = '/home/pi/Desktop/git/project_kens/Rpi/notice_changup.kns'
ku_exported_filename_guukjae = '/home/pi/Desktop/git/project_kens/Rpi/notice_guukjae.kns'
ku_exported_filename_haksaeng = '/home/pi/Desktop/git/project_kens/Rpi/notice_haksaeng.kns'
ku_exported_filename_sanhak = '/home/pi/Desktop/git/project_kens/Rpi/notice_sanhak.kns'
ku_exported_filename_ilban = '/home/pi/Desktop/git/project_kens/Rpi/notice_ilban.kns'



# Getting response module
# Parameter: string(url)
# Returns: Single Response object from reqeust.get()
# Author: acoustikue
def KnsGetHtmlText(url):

    print('[console] Sending requests...', end='')

    # Getting texts
    ku_res = requests.get(url)
    print('Done, status code: ' + str(ku_res.status_code))

    return ku_res

#
# main interface
# Parameter: Response object
# Returns: Dictionary type of parsed data.
# Author: acoustikue
def KnsParseNoticeHaksa(response):

    # Ready for parsing?
    print('[console] Parsing information...', end='')

    ku_soup = BeautifulSoup(response.text, 'html.parser')
    ku_soup = BeautifulSoup(str(ku_soup.find('table', class_='list')), 'html.parser')

    print(' Done. Printing infos(list) of the Haksa page.')
    

    list = ku_soup.find_all('td')

    #print(link)

    # literally works as a structure.
    # Deep copy necessary.
    structure = {
        'NUMBER': '1',
        'DIV': 'None', 
        'TITLE': 'None',
        'DATE': 'None',
        'SEEN': '0'
        }

    notice_info = []

    index = 0

    for info in list:

        if(index == 5): index = 0

        if index is 0: 
            if str(info.text.lstrip()) == '':
                structure['NUMBER'] = 'None'

            else: structure['NUMBER'] = str(info.text.lstrip())

        if index is 1: structure['DIV'] = str(info.text.lstrip()).rstrip()
        if index is 2: structure['TITLE'] = str(info.text.lstrip()).rstrip()
            # structure['TITLE'] = str(info.text.lstrip().replace('\n', ''))
            # Memo: if parsed, there will be always '\n' at the end of every title.

        if index is 3: structure['DATE'] = str(info.text.lstrip())
        if index is 4: 
            structure['SEEN'] = info.text.lstrip()
            notice_info.append(copy.deepcopy(structure))
            
        index += 1

    return notice_info




#
# main interface
# Parameter: Response object
# Returns: Dictionary type of parsed data.
# Author: acoustikue
def KnsParseNoticeJanghak(response):

    # Ready for parsing?
    print('[console] Parsing information...', end='')

    ku_soup = BeautifulSoup(response.text, 'html.parser')
    ku_soup = BeautifulSoup(str(ku_soup.find('table', class_='list')), 'html.parser')

    print(' Done. Printing infos(list) of the Janghak page.')
    

    list = ku_soup.find_all('td')

    #print(link)

    # literally works as a structure.
    # Deep copy necessary.
    structure = {
        'NUMBER': '1',
        'DIV': 'N/A', 
        'TITLE': 'None',
        'DATE': 'None',
        'SEEN': '0'
        }

    notice_info = []

    index = 0

    for info in list:

        if(index == 4): index = 0

        if index is 0: 
            if str(info.text.lstrip()) == '':
                structure['NUMBER'] = 'None'

            else: structure['NUMBER'] = str(info.text.lstrip())

        # if index is 1: structure['DIV'] = str(info.text.lstrip()).rstrip()
        if index is 1: structure['TITLE'] = str(info.text.lstrip()).rstrip()
            # structure['TITLE'] = str(info.text.lstrip().replace('\n', ''))
            # Memo: if parsed, there will be always '\n' at the end of every title.

        if index is 2: structure['DATE'] = str(info.text.lstrip())
        if index is 3: 
            structure['SEEN'] = info.text.lstrip()
            notice_info.append(copy.deepcopy(structure))
            
        index += 1

    return notice_info




#
# main interface
# Parameter: Response object
# Returns: Dictionary type of parsed data.
# Author: acoustikue
def KnsParseNoticeGuukjae(response):

    # Ready for parsing?
    print('[console] Parsing information...', end='')

    ku_soup = BeautifulSoup(response.text, 'html.parser')
    ku_soup = BeautifulSoup(str(ku_soup.find('table', class_='list')), 'html.parser')

    print(' Done. Printing infos(list) of the Guukjae page.')
    

    list = ku_soup.find_all('td')

    #print(link)

    # literally works as a structure.
    # Deep copy necessary.
    structure = {
        'NUMBER': '1',
        'DIV': 'N/A', 
        'TITLE': 'None',
        'DATE': 'None',
        'SEEN': '0'
        }

    notice_info = []

    index = 0

    for info in list:

        if(index == 5): index = 0

        if index is 0: 
            if str(info.text.lstrip()) == '':
                structure['NUMBER'] = 'None'

            else: structure['NUMBER'] = str(info.text.lstrip())

        if index is 1: structure['DIV'] = str(info.text.lstrip()).rstrip()
        if index is 2: structure['TITLE'] = str(info.text.lstrip()).rstrip()
            # structure['TITLE'] = str(info.text.lstrip().replace('\n', ''))
            # Memo: if parsed, there will be always '\n' at the end of every title.

        if index is 3: structure['DATE'] = str(info.text.lstrip())
        if index is 4: 
            structure['SEEN'] = info.text.lstrip()
            notice_info.append(copy.deepcopy(structure))
            
        index += 1

    return notice_info




#
# main interface
# Parameter: Response object
# Returns: Dictionary type of parsed data.
# Author: acoustikue
def KnsParseNoticeHaksaeng(response):

    # Ready for parsing?
    print('[console] Parsing information...', end='')

    ku_soup = BeautifulSoup(response.text, 'html.parser')
    ku_soup = BeautifulSoup(str(ku_soup.find('table', class_='list')), 'html.parser')

    print(' Done. Printing infos(list) of the Haksaeng page.')
    

    list = ku_soup.find_all('td')

    #print(link)

    # literally works as a structure.
    # Deep copy necessary.
    structure = {
        'NUMBER': '1',
        'DIV': 'N/A', 
        'TITLE': 'None',
        'DATE': 'None',
        'SEEN': '0'
        }

    notice_info = []

    index = 0

    for info in list:

        if(index == 5): index = 0

        if index is 0: 
            if str(info.text.lstrip()) == '':
                structure['NUMBER'] = 'None'

            else: structure['NUMBER'] = str(info.text.lstrip())

        if index is 1: structure['DIV'] = str(info.text.lstrip()).rstrip()
        if index is 2: structure['TITLE'] = str(info.text.lstrip()).rstrip()
            # structure['TITLE'] = str(info.text.lstrip().replace('\n', ''))
            # Memo: if parsed, there will be always '\n' at the end of every title.

        if index is 3: structure['DATE'] = str(info.text.lstrip())
        if index is 4: 
            structure['SEEN'] = info.text.lstrip()
            notice_info.append(copy.deepcopy(structure))
            
        index += 1

    return notice_info



#
# main interface
# Parameter: Response object
# Returns: Dictionary type of parsed data.
# Author: acoustikue
def KnsParseNoticeIlban(response):

    # Ready for parsing?
    print('[console] Parsing information...', end='')

    ku_soup = BeautifulSoup(response.text, 'html.parser')
    ku_soup = BeautifulSoup(str(ku_soup.find('table', class_='list')), 'html.parser')

    print(' Done. Printing infos(list) of the Ilban page.')
    

    list = ku_soup.find_all('td')

    #print(link)

    # literally works as a structure.
    # Deep copy necessary.
    structure = {
        'NUMBER': '1',
        'DIV': 'N/A', 
        'TITLE': 'None',
        'DATE': 'None',
        'SEEN': '0'
        }

    notice_info = []

    index = 0

    for info in list:

        if(index == 5): index = 0

        if index is 0: 
            if str(info.text.lstrip()) == '':
                structure['NUMBER'] = 'None'

            else: structure['NUMBER'] = str(info.text.lstrip())

        if index is 1: structure['DIV'] = str(info.text.lstrip()).rstrip()
        if index is 2: structure['TITLE'] = str(info.text.lstrip()).rstrip()
            # structure['TITLE'] = str(info.text.lstrip().replace('\n', ''))
            # Memo: if parsed, there will be always '\n' at the end of every title.

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
def KnsConvertDictToArrary(parsed_info):

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
def KnsWriteInfo(info_dict, file_addr):

    # saves information as texts
    with open(file_addr, "w") as save_file:

        print('[console] Writing parsed information...', end='')

        for info in info_dict:
            save_file.write(str(info['NUMBER']) + '\t' + str(info['DATE']) + '\t' + str(info['TITLE'] + '\n'))

        print(' Done exporting.')



# tested.
# Parameter: File address, will be declrared in global scope
# Returns: Array type.
# Author: acoustikue
def KnsReadInfo(file_addr):

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
def KnsCompare(prev_notice, new_notice):

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
