# -*- encoding: utf-8 -*-
"""
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   main.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
"""

from typing import Optional, Tuple

from nonebot import get_bots, get_driver
from nonebot.adapters.cqhttp import Bot
from nonebot.adapters.cqhttp.event import (
    Event,
    FriendRequestEvent,
    GroupMessageEvent,
    GroupRequestEvent,
    MetaEvent,
    PokeNotifyEvent,
    PrivateMessageEvent,
)
from nonebot.plugin import on

import OlivaDiceCore.msgReply
import OlivaDiceCore.ordinaryInviteManager
import OlivaDiceCore.pulse
from OlivaDiceCore.middleware import PluginEvent, Proc


async def pre_process(
    bot: Optional[Bot] = None, event: Optional[Event] = None
) -> Tuple[PluginEvent, Proc]:
    plugin_event = PluginEvent(bot, event)
    proc = Proc()

    return plugin_event, proc


@get_driver().on_bot_connect
async def init(bot: Bot):
    plugin_event, proc = await pre_process()
    OlivaDiceCore.msgReply.unity_init(plugin_event, proc)


@on("message").handle()
async def private_message(bot: Bot, event: PrivateMessageEvent):
    plugin_event, proc = await pre_process(bot, event)
    OlivaDiceCore.msgReply.unity_reply(plugin_event, proc)


@on("message").handle()
async def group_message(bot: Bot, event: GroupMessageEvent):
    plugin_event, proc = await pre_process(bot, event)
    OlivaDiceCore.msgReply.unity_reply(plugin_event, proc)


@on("notice").handle()
async def poke(bot: Bot, event: PokeNotifyEvent):
    plugin_event, proc = await pre_process(bot, event)
    OlivaDiceCore.msgReply.poke_reply(plugin_event, proc)


@on("request").handle()
async def friend_add_request(bot: Bot, event: FriendRequestEvent):
    plugin_event, proc = await pre_process(bot, event)
    OlivaDiceCore.ordinaryInviteManager.unity_friend_add_request(plugin_event, proc)


@on("request").handle()
async def group_invite_reques(bot: Bot, event: GroupRequestEvent):
    plugin_event, proc = await pre_process(bot, event)
    OlivaDiceCore.ordinaryInviteManager.unity_group_invite_request(plugin_event, proc)


@on("meta").handle()
async def heartbeat(bot: Bot, event: MetaEvent):
    plugin_event, proc = await pre_process(bot, event)
    OlivaDiceCore.pulse.unity_heartbeat(plugin_event, proc)


@get_driver().on_shutdown
async def save():
    plugin_event, proc = await pre_process()
    OlivaDiceCore.msgReply.unity_save(plugin_event, proc)
