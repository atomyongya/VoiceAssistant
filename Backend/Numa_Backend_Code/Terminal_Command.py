import os

def terminal_Command(command_Type):
    
    if command_Type.strip() == "update":
        os.system("sudo apt update")
        
    elif command_Type.strip() == "upgrade":
        os.system("sudo apt upgrade")
        
    elif command_Type.strip() == "autoremove":
        os.system("sudo apt autoremove")
    
    elif command_Type.strip() == "shutdown now":
        os.system("shutdown now")
        
    elif command_Type.strip() == "reboot":
        os.system("reboot")
        
    elif command_Type.strip() == "kill chrome":
        os.system("pkill chrome")
    
    elif command_Type.strip() == "kill all":
        os.system("killall5")
        
    elif command_Type.strip() == "exit":
        os.system("exit")
        
    else:
        print("No such command exist")
        exit()
    
    
