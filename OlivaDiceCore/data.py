# -*- encoding: utf-8 -*-
'''
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   data.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import os
import platform
import sys
import uuid

OlivaDiceCore_ver = '3.0.8'

exce_path = os.getcwd()

bot_info_basic = 'OlivaDice By lunzhiPenxil Ver.' + str(OlivaDiceCore_ver)

bot_info_basic_short = 'OlivaDice Ver.' + str(OlivaDiceCore_ver)

bot_info = bot_info_basic + ' [Python ' + str(platform.python_version()) + ' For NoneBot2]'

bot_version_short = 'OlivaDice ' + str(OlivaDiceCore_ver)

bot_version_short_header = 'OlivaDice/' + str(OlivaDiceCore_ver)

bot_summary = bot_info_basic + '\n'
bot_summary += 'Python ' + str(sys.version) + '\n'
bot_summary += str(platform.machine()) + '\n'
bot_summary += str(platform.processor()) + '\n'
bot_summary += str(os.name) + ':' + str(platform.platform())

bot_content = {
    'masterKey': str(uuid.uuid4())
}

dataDirRoot = './data/OlivaDice'
