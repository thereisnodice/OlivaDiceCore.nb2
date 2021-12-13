# -*- encoding: utf-8 -*-
'''
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   msgCustomManager.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import json
import os

import OlivaDiceCore.data
import OlivaDiceCore.msgCustom


def initMsgCustom(bot_info_dict):
    for bot_info_dict_this in bot_info_dict:
        OlivaDiceCore.msgCustom.dictStrCustomDict[bot_info_dict_this] = {}
        OlivaDiceCore.msgCustom.dictStrCustomDict[bot_info_dict_this] = OlivaDiceCore.msgCustom.dictStrCustom.copy()
    releaseDir(OlivaDiceCore.data.dataDirRoot)
    botHash_list = os.listdir(OlivaDiceCore.data.dataDirRoot)
    for botHash_list_this in botHash_list:
        botHash = botHash_list_this
        releaseDir(OlivaDiceCore.data.dataDirRoot + '/' + botHash)
        releaseDir(OlivaDiceCore.data.dataDirRoot + '/' + botHash + '/console')
        customReplyDir = OlivaDiceCore.data.dataDirRoot + '/' + botHash + '/console'
        customReplyFile = 'customReply.json'
        customReplyPath = customReplyDir + '/' + customReplyFile
        try:
            with open(customReplyPath, 'r', encoding = 'utf-8') as customReplyPath_f:
                OlivaDiceCore.msgCustom.dictStrCustomUpdateDict[botHash] = json.loads(customReplyPath_f.read())
                OlivaDiceCore.msgCustom.dictStrCustomDict[botHash].update(
                    OlivaDiceCore.msgCustom.dictStrCustomUpdateDict[botHash]
                )
        except:
            continue

def saveMsgCustom(bot_info_dict):
    for botHash in bot_info_dict:
        saveMsgCustomByBotHash(botHash)

def saveMsgCustomByBotHash(botHash):
    releaseDir(OlivaDiceCore.data.dataDirRoot + '/' + botHash)
    releaseDir(OlivaDiceCore.data.dataDirRoot + '/' + botHash + '/console')
    customReplyDir = OlivaDiceCore.data.dataDirRoot + '/' + botHash + '/console'
    customReplyFile = 'customReply.json'
    customReplyPath = customReplyDir + '/' + customReplyFile
    if botHash not in OlivaDiceCore.msgCustom.dictStrCustomUpdateDict:
        OlivaDiceCore.msgCustom.dictStrCustomUpdateDict[botHash] = {}
    if type(OlivaDiceCore.msgCustom.dictStrCustomUpdateDict[botHash]) != dict:
        OlivaDiceCore.msgCustom.dictStrCustomUpdateDict[botHash] = {}
    with open(customReplyPath, 'w', encoding = 'utf-8') as customReplyPath_f:
        customReplyPath_f.write(json.dumps(OlivaDiceCore.msgCustom.dictStrCustomUpdateDict[botHash], ensure_ascii = False, indent = 4))

def releaseDir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
