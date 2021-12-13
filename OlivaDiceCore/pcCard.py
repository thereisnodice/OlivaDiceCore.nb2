# -*- encoding: utf-8 -*-
'''
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   pcCard.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import hashlib
import json
import os

import OlivaDiceCore.data
import OlivaDiceCore.pcCardData

dictPcCardData = {
    'unity' : {}
}

dictPcCardSelection = {
    'unity' : {}
}

dictPcCardTemplate = {
    'unity' : {}
}

dictPcCardTemplateDefault = {
    'unity' : OlivaDiceCore.pcCardData.dictPcCardTemplateDefault.copy()
}

def releaseDir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def dataPcCardTotalCount():
    total_count = 0
    for dictPcCardData_this in dictPcCardData:
        for dictPcCardData_hostkey_this in dictPcCardData[dictPcCardData_this]:
            total_count += 1
    return total_count

def dataPcCardSave(hostKey, pcHash):
    global dictPcCardData
    global dictPcCardSelection
    global dictPcCardTemplate
    dataDirRoot_this = OlivaDiceCore.data.dataDirRoot
    releaseDir(dataDirRoot_this)
    if hostKey in dictPcCardData:
        if pcHash in dictPcCardData[hostKey]:
            releaseDir(dataDirRoot_this + '/' + hostKey)
            releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard')
            releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard/data')
            pcCardDataPath = dataDirRoot_this + '/' + hostKey + '/pcCard/data/' + pcHash
            with open(pcCardDataPath, 'w', encoding = 'utf-8') as pcCardDataPath_f:
                pcCardDataPath_f.write(json.dumps(dictPcCardData[hostKey][pcHash], ensure_ascii = False, indent = 4))
    if hostKey in dictPcCardSelection:
        if pcHash in dictPcCardSelection[hostKey]:
            releaseDir(dataDirRoot_this + '/' + hostKey)
            releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard')
            releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard/selection')
            pcCardSelectionPath = dataDirRoot_this + '/' + hostKey + '/pcCard/selection/' + pcHash
            with open(pcCardSelectionPath, 'w', encoding = 'utf-8') as pcCardSelectionPath_f:
                pcCardSelectionPath_f.write(json.dumps(dictPcCardSelection[hostKey][pcHash], ensure_ascii = False, indent = 4))
    if hostKey in dictPcCardTemplate:
        if pcHash in dictPcCardTemplate[hostKey]:
            releaseDir(dataDirRoot_this + '/' + hostKey)
            releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard')
            releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard/template')
            pcCardTemplatePath = dataDirRoot_this + '/' + hostKey + '/pcCard/template/' + pcHash
            with open(pcCardTemplatePath, 'w', encoding = 'utf-8') as dictPcCardTemplate_f:
                dictPcCardTemplate_f.write(json.dumps(dictPcCardTemplate[hostKey][pcHash], ensure_ascii = False, indent = 4))

def dataPcCardLoad(hostKey, pcHash):
    global dictPcCardData
    global dictPcCardSelection
    global dictPcCardTemplate
    dataDirRoot_this = OlivaDiceCore.data.dataDirRoot
    releaseDir(dataDirRoot_this)
    releaseDir(dataDirRoot_this + '/' + hostKey)
    releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard')
    releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard/data')
    releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard/selection')
    releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard/template')
    pcCardDataPath = dataDirRoot_this + '/' + hostKey + '/pcCard/data/' + pcHash
    pcCardSelectionPath = dataDirRoot_this + '/' + hostKey + '/pcCard/selection/' + pcHash
    pcCardTemplatePath = dataDirRoot_this + '/' + hostKey + '/pcCard/template/' + pcHash
    if hostKey not in dictPcCardData:
        dictPcCardData[hostKey] = {}
    if pcHash not in dictPcCardData[hostKey]:
        dictPcCardData[hostKey][pcHash] = {}
    if hostKey not in dictPcCardSelection:
        dictPcCardSelection[hostKey] = {}
    if pcHash not in dictPcCardSelection[hostKey]:
        dictPcCardSelection[hostKey][pcHash] = {}
    if hostKey not in dictPcCardTemplate:
        dictPcCardTemplate[hostKey] = {}
    if pcHash not in dictPcCardTemplate[hostKey]:
        dictPcCardTemplate[hostKey][pcHash] = {}
    if os.path.exists(pcCardDataPath):
        with open(pcCardDataPath, 'r', encoding = 'utf-8') as pcCardDataPath_f:
            dictPcCardData[hostKey][pcHash] = json.loads(pcCardDataPath_f.read())
    if os.path.exists(pcCardSelectionPath):
        with open(pcCardSelectionPath, 'r', encoding = 'utf-8') as pcCardSelectionPath_f:
            dictPcCardSelection[hostKey][pcHash] = json.loads(pcCardSelectionPath_f.read())
    if os.path.exists(pcCardTemplatePath):
        with open(pcCardTemplatePath, 'r', encoding = 'utf-8') as pcCardTemplatePath_f:
            dictPcCardTemplate[hostKey][pcHash] = json.loads(pcCardTemplatePath_f.read())

def dataPcCardLoadAll():
    dataDirRoot_this = OlivaDiceCore.data.dataDirRoot
    releaseDir(dataDirRoot_this)
    pcCardDataHostList = os.listdir(dataDirRoot_this)
    for pcCardDataHostList_this in pcCardDataHostList:
        hostKey = pcCardDataHostList_this
        releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard')
        releaseDir(dataDirRoot_this + '/' + hostKey + '/pcCard/data')
        pcCardDataPCHashList = os.listdir(dataDirRoot_this + '/' + hostKey + '/pcCard/data')
        for pcCardDataPCHashList_this in pcCardDataPCHashList:
            pcHash = pcCardDataPCHashList_this
            dataPcCardLoad(hostKey, pcHash)

def pcCardRebase(pcHash, pcCardName):
    selection_key = 'selection'
    pcCardNameOld = None
    dict_pcCardNameOld = {}
    dict_pcCardTemplateOld = {}
    if pcHash not in dictPcCardSelection['unity']:
        dictPcCardSelection['unity'][pcHash] = {}
    if selection_key in dictPcCardSelection['unity'][pcHash]:
        pcCardNameOld = dictPcCardSelection['unity'][pcHash][selection_key]
    dictPcCardSelection['unity'][pcHash][selection_key] = pcCardName
    if pcCardNameOld != None:
        if pcHash in dictPcCardData['unity']:
            if pcCardNameOld in dictPcCardData['unity'][pcHash]:
                dict_pcCardNameOld = dictPcCardData['unity'][pcHash][pcCardNameOld].copy()
                dictPcCardData['unity'][pcHash].pop(pcCardNameOld)
        else:
            dictPcCardData['unity'][pcHash] = {}
    else:
        dictPcCardData['unity'][pcHash] = {}
    dictPcCardData['unity'][pcHash][pcCardName] = dict_pcCardNameOld
    if pcCardNameOld != None:
        if pcHash in dictPcCardTemplate['unity']:
            if pcCardNameOld in dictPcCardTemplate['unity'][pcHash]:
                dict_pcCardTemplateOld = dictPcCardTemplate['unity'][pcHash][pcCardNameOld].copy()
                dictPcCardTemplate['unity'][pcHash].pop(pcCardNameOld)
        else:
            dictPcCardTemplate['unity'][pcHash] = {}
    else:
        dictPcCardTemplate['unity'][pcHash] = {}
    dictPcCardTemplate['unity'][pcHash][pcCardName] = dict_pcCardTemplateOld
    dataPcCardSave('unity', pcHash)
    return True

def pcCardDataSetBySkillNameReplace(pcHash, skillName, skillValue, pcCardName = 'default'):
    selection_key = 'selection'
    tmp_pc_card_name_key = pcCardName
    tmp_pc_card_name_key_new = pcCardName
    if pcHash not in dictPcCardSelection['unity']:
        dictPcCardSelection['unity'][pcHash] = {}
    if selection_key in dictPcCardSelection['unity'][pcHash]:
        tmp_pc_card_name_key = dictPcCardSelection['unity'][pcHash][selection_key]
    else:
        dictPcCardSelection['unity'][pcHash][selection_key] = tmp_pc_card_name_key
    if pcHash in dictPcCardData['unity']:
        pass
    else:
        dictPcCardData['unity'][pcHash] = {}
    if tmp_pc_card_name_key not in dictPcCardData['unity'][pcHash]:
        dictPcCardData['unity'][pcHash][tmp_pc_card_name_key] = {}
    dictPcCardData['unity'][pcHash][tmp_pc_card_name_key][str(skillName)] = skillValue
    if tmp_pc_card_name_key != tmp_pc_card_name_key_new:
        dictPcCardData['unity'][pcHash][tmp_pc_card_name_key_new] = dictPcCardData['unity'][pcHash][tmp_pc_card_name_key]
        dictPcCardData['unity'][pcHash].pop(tmp_pc_card_name_key)
        dictPcCardSelection['unity'][pcHash][selection_key] = tmp_pc_card_name_key_new
    dataPcCardSave('unity', pcHash)

def pcCardDataSetBySkillName(pcHash, skillName, skillValue, pcCardName = 'default'):
    selection_key = 'selection'
    tmp_pc_card_name_key = pcCardName
    if pcHash not in dictPcCardSelection['unity']:
        dictPcCardSelection['unity'][pcHash] = {}
    dictPcCardSelection['unity'][pcHash][selection_key] = tmp_pc_card_name_key
    if pcHash in dictPcCardData['unity']:
        pass
    else:
        dictPcCardData['unity'][pcHash] = {}
    if tmp_pc_card_name_key not in dictPcCardData['unity'][pcHash]:
        dictPcCardData['unity'][pcHash][tmp_pc_card_name_key] = {}
    dictPcCardData['unity'][pcHash][tmp_pc_card_name_key][str(skillName)] = skillValue
    dataPcCardSave('unity', pcHash)

def pcCardDataGetBySkillName(pcHash, skillName):
    selection_key = 'selection'
    tmp_skill_value = 0
    tmp_pc_card_name_key = 'default'
    if pcHash not in dictPcCardSelection['unity']:
        return tmp_skill_value
    if selection_key not in dictPcCardSelection['unity'][pcHash]:
        return tmp_skill_value
    else:
        tmp_pc_card_name_key = dictPcCardSelection['unity'][pcHash][selection_key]
    if pcHash not in dictPcCardData['unity']:
        return tmp_skill_value
    if tmp_pc_card_name_key not in dictPcCardData['unity'][pcHash]:
        return tmp_skill_value
    if str(skillName) in dictPcCardData['unity'][pcHash][tmp_pc_card_name_key]:
        tmp_skill_value = dictPcCardData['unity'][pcHash][tmp_pc_card_name_key][str(skillName)]
    return tmp_skill_value

def pcCardDataGetSelectionKey(pcHash):
    selection_key = 'selection'
    tmp_pc_card_name_key = None
    if pcHash not in dictPcCardSelection['unity']:
        return tmp_pc_card_name_key
    if selection_key not in dictPcCardSelection['unity'][pcHash]:
        return tmp_pc_card_name_key
    else:
        tmp_pc_card_name_key = dictPcCardSelection['unity'][pcHash][selection_key]
    return tmp_pc_card_name_key

def pcCardDataSetSelectionKey(pcHash, pcCardName):
    selection_key = 'selection'
    tmp_pc_card_name_key = pcCardName
    tmp_card_dict = {}
    if pcHash in dictPcCardData['unity']:
        tmp_card_dict = dictPcCardData['unity'][pcHash]
    if tmp_pc_card_name_key in tmp_card_dict:
        if pcHash not in dictPcCardSelection['unity']:
            dictPcCardSelection['unity'][pcHash] = {}
        dictPcCardSelection['unity'][pcHash][selection_key] = tmp_pc_card_name_key
        dataPcCardSave('unity', pcHash)
        return True
    else:
        return False

def pcCardDataDelSelectionKey(pcHash, pcCardName):
    selection_key = 'selection'
    tmp_pc_card_name_key = pcCardName
    tmp_card_dict = {}
    tmp_card_dict_2 = {}
    if pcHash in dictPcCardData['unity']:
        tmp_card_dict = dictPcCardData['unity'][pcHash]
    else:
        dictPcCardData['unity'][pcHash] = {}
    if pcHash in dictPcCardTemplate['unity']:
        tmp_card_dict_2 = dictPcCardTemplate['unity'][pcHash]
    else:
        dictPcCardTemplate['unity'][pcHash] = {}
    if tmp_pc_card_name_key in tmp_card_dict:
        dictPcCardData['unity'][pcHash].pop(tmp_pc_card_name_key)
        if tmp_pc_card_name_key in tmp_card_dict_2:
            dictPcCardTemplate['unity'][pcHash].pop(tmp_pc_card_name_key)
        if pcHash not in dictPcCardSelection['unity']:
            dictPcCardSelection['unity'][pcHash] = {}
            return False
        if selection_key in dictPcCardSelection['unity'][pcHash]:
            if tmp_pc_card_name_key == dictPcCardSelection['unity'][pcHash][selection_key]:
                dictPcCardSelection['unity'][pcHash].pop(selection_key)
                if len(dictPcCardData['unity'][pcHash].keys()) > 0:
                    tmp_card_dict_keys = list(dictPcCardData['unity'][pcHash].keys())
                    dictPcCardSelection['unity'][pcHash][selection_key] = tmp_card_dict_keys[0]
        dataPcCardSave('unity', pcHash)
        return True
    else:
        return False

def pcCardDataGetTemplateByKey(templateName):
    global dictPcCardTemplateDefault
    tmp_template = None
    if templateName in dictPcCardTemplateDefault['unity']:
        tmp_template = dictPcCardTemplateDefault['unity'][templateName]
    return tmp_template

def pcCardDataGetTemplateKey(pcHash, pcCardName):
    global dictPcCardTemplate
    selection_key = 'template'
    tmp_pc_template_name_key = None
    if pcHash not in dictPcCardTemplate['unity']:
        return tmp_pc_template_name_key
    if pcCardName not in dictPcCardTemplate['unity'][pcHash]:
        return tmp_pc_template_name_key
    if selection_key not in dictPcCardTemplate['unity'][pcHash][pcCardName]:
        return tmp_pc_template_name_key
    else:
        tmp_pc_template_name_key = dictPcCardTemplate['unity'][pcHash][pcCardName][selection_key]
    return tmp_pc_template_name_key

def pcCardDataGetTemplateRuleKey(pcHash, pcCardName):
    global dictPcCardTemplate
    selection_key = 'checkRules'
    tmp_pc_template_name_key = None
    if pcHash not in dictPcCardTemplate['unity']:
        return tmp_pc_template_name_key
    if pcCardName not in dictPcCardTemplate['unity'][pcHash]:
        return tmp_pc_template_name_key
    if selection_key not in dictPcCardTemplate['unity'][pcHash][pcCardName]:
        return tmp_pc_template_name_key
    else:
        tmp_pc_template_name_key = dictPcCardTemplate['unity'][pcHash][pcCardName][selection_key]
    return tmp_pc_template_name_key

def pcCardDataSetTemplateKey(pcHash, pcCardName, templateName = 'default', ruleName = 'default'):
    selection_key = 'template'
    selection_key_2 = 'checkRules'
    tmp_pc_card_name_key = pcCardName
    if templateName not in dictPcCardTemplateDefault['unity']:
        return False
    if selection_key_2 not in dictPcCardTemplateDefault['unity'][templateName]:
        return False
    if ruleName not in dictPcCardTemplateDefault['unity'][templateName][selection_key_2]:
        return False
    tmp_card_dict = {}
    if pcHash in dictPcCardData['unity']:
        tmp_card_dict = dictPcCardData['unity'][pcHash]
    if tmp_pc_card_name_key in tmp_card_dict:
        if pcHash not in dictPcCardTemplate['unity']:
            dictPcCardTemplate['unity'][pcHash] = {}
        if tmp_pc_card_name_key not in dictPcCardTemplate['unity'][pcHash]:
            dictPcCardTemplate['unity'][pcHash][tmp_pc_card_name_key] = {}
        dictPcCardTemplate['unity'][pcHash][tmp_pc_card_name_key][selection_key] = templateName
        dictPcCardTemplate['unity'][pcHash][tmp_pc_card_name_key][selection_key_2] = ruleName
        dataPcCardSave('unity', pcHash)
        return True
    else:
        return False

def pcCardDataGetUserAll(pcHash):
    selection_key = 'selection'
    tmp_card_dict = {}
    if pcHash in dictPcCardData['unity']:
        tmp_card_dict = dictPcCardData['unity'][pcHash]
    return tmp_card_dict

def pcCardDataGetByPcName(pcHash):
    selection_key = 'selection'
    tmp_skill_list = {}
    tmp_pc_card_name_key = 'default'
    if pcHash not in dictPcCardSelection['unity']:
        return tmp_skill_list
    if selection_key not in dictPcCardSelection['unity'][pcHash]:
        return tmp_skill_list
    else:
        tmp_pc_card_name_key = dictPcCardSelection['unity'][pcHash][selection_key]
    if pcHash in dictPcCardData['unity']:
        if tmp_pc_card_name_key in dictPcCardData['unity'][pcHash]:
            tmp_skill_list = dictPcCardData['unity'][pcHash][tmp_pc_card_name_key]
    return tmp_skill_list

def checkPcName(data):
    res = True
    if len(data) > 50:
        res = False
    if '\n' in data:
        res = False
    return res

def getPcHash(pcId, platform):
    hash_tmp = hashlib.new('md5')
    hash_tmp.update(str(pcId).encode(encoding='UTF-8'))
    hash_tmp.update(str(platform).encode(encoding='UTF-8'))
    return hash_tmp.hexdigest()
