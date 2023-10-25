import requests
import json
import time
import base64
from LeagueClientInfo import getKey, getPort

def Main():

    while(CheckPhase() != "InProgress"):     #If you are not in a game, keep polling
        
        match CheckPhase():

            case "Lobby":
                
                time.sleep(1)

            case "Matchmaking":
              
                time.sleep(0.5)

            case "ChampSelect":
                time.sleep(2)

            case "ReadyCheck":
                
                AcceptQueue()
                time.sleep(1)

def CheckPhase():

    Port = getPort() #Get the port
    Key = getKey() #Get the unencoded key

    url = "https://127.0.0.1:" + Port + "/lol-gameflow/v1/session" #Set the url using port
    
    apiKeyBeforeEncode = "riot:" + Key 

    #Encode apiKey
    b = base64.b64encode(bytes(apiKeyBeforeEncode,'utf-8'))
    apiKey = b.decode('utf-8')

    apiKey = "Basic " + apiKey

    payload = {}
    headers = {
  'Authorization': apiKey
    }

    #Sends a "GET" request asking for the session data
    response = requests.request("GET", url, headers=headers, data=payload, verify=False) 

    #Convert the response to a json
    jsonResponse = response.json()

    #Convert the json into a json-formatted string
    jsonResponseString = json.dumps(jsonResponse)

    #Parse the json file
    parseJsonResponse = json.loads(jsonResponseString)

    #Return the current phase
    return(parseJsonResponse["phase"])


def AcceptQueue():

    Port = getPort()
    Key = getKey()

    url = "https://127.0.0.1:" + Port + "/lol-matchmaking/v1/ready-check/accept"
 
    apiKeyBeforeEncode = "riot:" + Key

    b = base64.b64encode(bytes(apiKeyBeforeEncode,'utf-8'))
    apiKey = b.decode('utf-8')

    apiKey = "Basic " + apiKey

    headers = {
    'Authorization': apiKey
    }
    
    
    payload = {}
    
    
    requests.request("POST", url, headers=headers, data=payload, verify=False)


if __name__=="__main__":
    Main()
