import psutil
import re

 #Find the processes given a commandline argument (port, key)

def findProcesses(argument):
    matching_processes = []
    for process in psutil.process_iter(['pid', 'cmdline']):
        try:
            cmdline = process.info['cmdline']
            if cmdline and argument in ' '.join(cmdline):
                matching_processes.append({
                    'pid': process.info['pid'],
                    'cmdline': ' '.join(cmdline)
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return str(matching_processes)

#Get the port number for the current instance of the League client

def getPort():

    pattern = r'--app-port="?(\d+)"?' #Regex pattern to capture the port

    output = findProcesses("--app-port")

    match = re.search(pattern, output)

    port = match.group(1)

    return port

#Get the authentication key number for the current instance of the League client

def getKey():

    pattern = r'--remoting-auth-token=([a-zA-Z0-9_-]+)' #Regex pattern to capture the authentication token

    output = findProcesses("--remoting-auth-token")

    match = re.search(pattern, output)
    
    key = match.group(1)

    return key




    
    
