#PRA RODAR, SETAR DOIS TERMINAIS,
#   UM COM O CODIGO: roscore
#   OUTRO COM O CODIGO: rosrun turtlesim turtlesim_node 

import os
import time
from src.job import job

#---------------------------------------------

def load():
    os.system("clear")
    print('Setting up the application...')
    time.sleep(2)
    os.system("clear")

#---------------------------------------------

def main():
    try:
        while True:
            job()
    except Exception as err:
        print(f"Error: Unreadable entry")
        main()


if __name__ == "src.main":
    load()
    main()