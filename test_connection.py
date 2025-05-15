import pytest
import asyncio
from mini import move
from mini.apis.api_setup import StartRunProgram
import mini.mini_sdk as MiniSdk
from mini.apis.api_expression import PlayExpression
import mini.mini_sdk as MiniSdk
from mini.apis.api_setup import StartRunProgram
from mini.apis import *
from mini.apis.api_sound import *
from mini.apis.base_api import *
from mini.apis.api_action import *
from mini.apis.api_behavior import *




#test di funzioni asincrone
@pytest.mark.asyncio 
async def test_robot_connection():
    device = None
    try:
        # Configura il tipo di robot
        MiniSdk.set_robot_type(MiniSdk.RobotType.EDU)

        # Connessione al robot
        device = await MiniSdk.get_device_by_name("00011", 10) 
        await MiniSdk.connect(device)

       
        await StartRunProgram().execute()
        await asyncio.sleep(6)

        # Controlla se la connessione è attiva
        assert device is not None

    except Exception as e:
        pytest.fail(f"Errore durante la connessione: {e}")

    