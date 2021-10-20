def openGarageDoor():
    """Run an example script to quickly test."""
    import asyncio
    import logging

    from aiohttp import ClientSession

    from pymyq import login
    from pymyq.account import MyQAccount
    from pymyq.errors import MyQError, RequestError
    from pymyq.garagedoor import STATE_CLOSED, STATE_OPEN

    from consoleColors import bcolors as c

    _LOGGER = logging.getLogger()

    EMAIL = "cbaker@bamolaw.com"
    PASSWORD = "Ceb4175!"
    ISSUE_COMMANDS = True
    # LOGLEVEL = logging.DEBUG
    LOGLEVEL = logging.WARNING

    async def print_garagedoors(account: MyQAccount):  # noqa: C901
        """Print garage door information and open/close if requested

        Args:
            account (MyQAccount): Account for which to retrieve garage doors
        """
        print(f"  GarageDoors: {len(account.covers)}")
        print("  ---------------")
        if len(account.covers) != 0:
            for idx, device in enumerate(account.covers.values()):

                if ISSUE_COMMANDS:
                    try:
                        open_task = None
                        opened = closed = False
                        if device.open_allowed:
                            if device.state == STATE_OPEN:
                                print(f"Garage door {device.name} is already open")
                            else:
                                print(f"Opening garage door {device.name}")
                                try:
                                    open_task = await device.open(wait_for_state=False)
                                except MyQError as err:
                                    _LOGGER.error(
                                        "Error when trying to open %s: %s",
                                        device.name,
                                        str(err),
                                    )
                                print(f"Garage door {device.name} is {device.state}")

                        else:
                            print(f"Opening of garage door {device.name} is not allowed.")

                        # We're not waiting for opening to be completed before we do call to close.
                        # The API will wait automatically for the open to complete before then
                        # processing the command to close.
                    except RequestError as err:
                        _LOGGER.error(err)
            print("  ------------------------------")

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
                    await print_garagedoors(account=account)
                    print(c.FAIL + "[myq api] " + c.WARNING + f"Successfully Opened Braden's Garage Doors.")

            except MyQError as err:
                _LOGGER.error("There was an error: %s", err)

    asyncio.get_event_loop().run_until_complete(main())


# -------------------
# -------------------#-------------------
# -------------------#-------------------#-------------------
# -------------------#-------------------#-------------------
# -------------------#-------------------
# -------------------

amnt = 0
def openGarageDoorTest():
    """Run an example script to quickly test."""
    import asyncio
    import logging

    from aiohttp import ClientSession

    from pymyq import login
    from pymyq.account import MyQAccount
    from pymyq.errors import MyQError, RequestError
    from pymyq.garagedoor import STATE_CLOSED, STATE_OPEN

    from consoleColors import bcolors as c

    _LOGGER = logging.getLogger()

    EMAIL = "cbaker@bamolaw.com"
    PASSWORD = "Ceb4175!"
    ISSUE_COMMANDS = True
    # LOGLEVEL = logging.DEBUG
    LOGLEVEL = logging.WARNING

    async def print_garagedoors(account: MyQAccount):  # noqa: C901
        """Print garage door information and open/close if requested

        Args:
            account (MyQAccount): Account for which to retrieve garage doors
        """
        print(f"  GarageDoors: {len(account.covers)}")
        print("  ---------------")
        if len(account.covers) != 0:
            for idx, device in enumerate(account.covers.values()):

                if ISSUE_COMMANDS:
                    try:
                        open_task = None
                        opened = closed = False
                        if device.open_allowed:
                            if device.state == STATE_OPEN:
                                print(f"Garage door {device.name} is already open")
                            else:
                                print(f"Opening garage door {device.name}")
                                try:
                                    open_task = await device.open(wait_for_state=False)
                                except MyQError as err:
                                    _LOGGER.error(
                                        "Error when trying to open %s: %s",
                                        device.name,
                                        str(err),
                                    )
                                print(f"Garage door {device.name} is {device.state}")

                        else:
                            print(f"Opening of garage door {device.name} is not allowed.")

                        # We're not waiting for opening to be completed before we do call to close.
                        # The API will wait automatically for the open to complete before then
                        # processing the command to close.
                    except RequestError as err:
                        _LOGGER.error(err)
            print("  ------------------------------")

    async def main() -> None:
        """Create the aiohttp session and run the example."""
        logging.basicConfig(level=LOGLEVEL)

        async with ClientSession() as websession:
            try:
                # Create an API object:
                # print(f"{EMAIL} {PASSWORD}")
                api = await login(EMAIL, PASSWORD, websession)

                for account in api.accounts.values():
                    global amnt
                    # print(f"Account ID: {account.id}")
                    # print(f"Account Name: {account.name}")

                    # Get all devices listed with this account – note that you can use
                    # api.covers to only examine covers or api.lamps for only lamps.
                    amnt += 1
                    print(c.FAIL + "[myq api] " + c.WARNING + f"Successfully Opened Braden's Garage Doors. (test)")

            except MyQError as err:
                _LOGGER.error("There was an error: %s", err)

    asyncio.get_event_loop().run_until_complete(main())
