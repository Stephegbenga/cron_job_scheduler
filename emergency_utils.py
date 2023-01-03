import os

bot_arrays = ['customer_support', 'indiatesting', 'indiayoga', 'wascheduler_py']

def execute_command(command):
    try:
        os.system(command)
    except:
        print("Something went wrong")

