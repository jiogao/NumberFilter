from enum import Enum

class NFLogType(Enum):
    info = 0
    error = 1

# logList = []
events = []

def info(*args):
    log(NFLogType.info, *args)

def error(*args):
    log(NFLogType.error, *args)

def log(logType, *args):
    label = '[{0}]'.format(logType)
    print(label, *args)
    # logStr = label
    # for item in args:
    #     logStr += " "
    #     logStr += item
    # logList.append(logStr)

    for item in events:
        item(logType, *args)
    
def registLogEvent(event):
    events.append(event)

# info("aaa")
# info("aaa2")
# info("aaa3")
# print(logList)