import asyncio
import logging

from aiohttp import ClientSession

from pymyq import login
from pymyq.account import MyQAccount
from pymyq.errors import MyQError, RequestError
from pymyq.garagedoor import STATE_CLOSED, STATE_CLOSING, STATE_OPEN, STATE_OPENING

_LOGGER = logging.getLogger()

EMAIL = "cbaker@bamolaw.com"
PASSWORD = "Ceb4175!"
ISSUE_COMMANDS = True
# LOGLEVEL = logging.DEBUG
LOGLEVEL = logging.WARNING


def print_info(number: int, device):
    """Print the device information

    Args:
        number (int): [description]
        device ([type]): [description]
    """
    print(f"      Device {number + 1}: {device.name}")
    print(f"      Device Online: {device.online}")
    print(f"      Device ID: {device.device_id}")
    print(
        f"      Parent Device ID: {device.parent_device_id}",
    )
    print(f"      Device Family: {device.device_family}")
    print(
        f"      Device Platform: {device.device_platform}",
    )
    print(f"      Device Type: {device.device_type}")
    print(f"      Firmware Version: {device.firmware_version}")
    print(f"      Open Allowed: {device.open_allowed}")
    print(f"      Close Allowed: {device.close_allowed}")
    print(f"      Current State: {device.state}")
    print("      ---------")

closingCounter = 0
closedCounter = 0

openingCounter = 0
openCounter = 0
async def openDoor(account: MyQAccount):
    """Print garage door information and open/close if requested

    Args:
        account (MyQAccount): Account for which to retrieve garage doors
    """
    print(f"  GarageDoors: {len(account.covers)}")
    print("  ---------------")
    while True:
        if len(account.covers) != 0:
            for idx, device in enumerate(account.covers.values()):
                if device.name == "Single Garage Door":
                    pass
                if device.name == "Double Garage Door":
                    if device.state == STATE_CLOSED:
                        global closedCounter
                        if closedCounter <= 0:
                            print('closed')
                            closedCounter += 1
                    if device.state == STATE_CLOSING:
                        global closingCounter
                        if closingCounter <= 0:
                            print('closing')
                            closingCounter += 1
                    if device.state == STATE_OPENING:
                        global openingCounter
                        if openingCounter <= 0:
                            print('opening')
                            openingCounter += 1
                    
                    if device.state == STATE_OPEN:
                        global openCounter
                        if openCounter <= 0:
                            print('open')
                            
                            openCounter += 1


                

async def open(account: MyQAccount):
    print(f"  GarageDoors: {len(account.covers)}")
    print("  ---------------")

async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=LOGLEVEL)
    async with ClientSession() as websession:
        try:
            # Create an API object:
            print(f"{EMAIL} {PASSWORD}")
            api = await login(EMAIL, PASSWORD, websession)

            for account in api.accounts.values():
                print(f"Account ID: {account.id}")
                print(f"Account Name: {account.name}")

                # Get all devices listed with this account – note that you can use
                # api.covers to only examine covers or api.lamps for only lamps.
                await openDoor(account=account)

        except MyQError as err:
            _LOGGER.error("There was an error: %s", err)
    
asyncio.get_event_loop().run_until_complete(main())
