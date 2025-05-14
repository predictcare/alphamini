# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 12:39:32 2025

@author: aphel
"""
import pytest
import asyncio
import nest_asyncio
from mini.apis.api_setup import StartRunProgram
from mini.apis.api_expression import PlayExpression
from mini.apis.api_sence import ObjectRecognise, RecogniseObjectResponse, ObjectRecogniseType
from mini.apis.api_sound import *
import mini.mini_sdk as MiniSdk
from mini.apis.base_api import *
from mini.apis.api_action import *
from mini.apis.api_behavior import *
from mini.apis.api_observe import ObserveHeadRacket, HeadRacketType
from mini.dns.dns_browser import WiFiDevice
from mini.pb2.codemao_observeheadracket_pb2 import ObserveHeadRacketResponse

async def main():
#1 - connessione  al robot
    try:
        # Configura il tipo di robot
        MiniSdk.set_robot_type(MiniSdk.RobotType.EDU)
        
        # Connessione al robot
        device = await MiniSdk.get_device_by_name("00011", 10)  # Usa il seriale corretto
        await MiniSdk.connect(device)
        
        # Entra in 'programming mode'
        await StartRunProgram().execute()
        await asyncio.sleep(5)
  
        

    except Exception as e:
        print(f"Si è verificato un errore: {e}")
    finally:
        # Disconnessione
        if device:
            await MiniSdk.quit_program()
            await MiniSdk.release()
            print("Disconnesso dal robot.")





# Esegui il programma
nest_asyncio.apply()
asyncio.run(main())
