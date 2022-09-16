import getch
from geometry_msgs.msg import Twist


from src.options_dict import option_dict

async def job(pub, instance):
    option = getOption()
    msg = Twist()
    option_dict[option][1](msg, instance)
    pub.publish(msg)

def getOption():
    entry = getch.getch()
    print(f"Selected Move: {option_dict[entry][0]}")
    return entry