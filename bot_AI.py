from iotbot import GroupMsg
from iotbot.decorators import not_botself, only_this_msg_type        
from iotbot.sugar import Text                                        
from iotbot.utils import MsgTypes

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot('qwq',storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///database.sqlite3')

def AIbot(text):
    
    try:
        bot_input = bot.get_response(text)
        print("输出: ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        pass
    return bot_input
@only_this_msg_type(MsgTypes.TextMsg)
def receive_group_msg(ctx:GroupMsg):
    if ctx.Content.startswith('#聊天:'):
        text = ctx.Content[4:]
        ret = AIbot(text)
        if ret:
            Text(ret)
