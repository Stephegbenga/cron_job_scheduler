import os

bot_arrays = ['customer_support', 'indiatesting', 'indiayoga', 'wascheduler_py']

def execute_command(command):
    try:
        os.system(command)
    except:
        print("Something went wrong")


def stop_all_bots():
    for bot in bot_arrays:
        command = f"pm2 restart {bot}"
        execute_command(command)


def start_all_bots():
    for bot in bot_arrays:
        command = f"pm2 restart {bot}"
        execute_command(command)