# Galaxy plugin for Battle.net

This plugin allows you to install and launch your Blizzard games via the GOG Galaxy 2.0 launcher.

## Installation
Use build-in `Search` engine from GOG Galaxy 2.0 Settings

*Note: The actual code in build-in Search is a reviewed fork https://github.com/FriendsOfGalaxy/galaxy-integration-blizzard prepared by FriendsOfGalaxy*

### From source (tested on windows 10 and macos 10.14 with python 3.7)
- copy / clone this repo
- run:
```bash
cd galaxy_blizzard_plugin
pip install -r requirements/dev.txt
inv install
```

## Note on playtime

Currently we only support displaying the total playtime of your quickplay matches in Overwatch. Playtime might take some time to update after you quit the game.

**Important:** Make sure your Overwatch profile is set to public in order to show your playtime.
To do that, start up Overwatch and navigate to the Options. From there click the "Social" tab and toggle the option "Career Profile Visibility" to "Public".

## Note on Classic Blizzard Games not detected as installed or launching

If you have classic Blizzard games which are not properly detected as installed or don't launch when clicking 'play'
please provide the name and values of the games key under

```
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\
```

Windows registry path (by opening `Run`-> `regedit`)

If on MAC please provide the games bundle_id which can be found by calling

```
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep {game_name}
```

## Uninstallation (remove all data)
Click `Disconnect` button in GOG Galaxy Settings. If you see `Connect` instead of `Disconnect` (this may happen on plugin crash or accessing from different machine) you need to connect it again and then disconnect.

### "Soft" disconnect (advanced)
If you want to keep imported data (owned games, play time), but do not need to sync more and play with local games, you can "turn off" local plugin:
- close Galaxy
- remove plugin local database (on Windows usually at `C:\ProgramData\GOG.com\Galaxy\storage\plugins`).

## Help us with game detection

Unfortunately, games' details must currently be hardcoded for detection, and are kept in `definitions.py`. Currently multiple versions of the same game is not supported as ownership is matched 1:1 on UID

### Adding undetected games

Blizzard games must be added to the map of title IDs with their UID, game name, and product family

#### Example and tips for finding the necessary data

| Product family (for launching) | UID (for installation) | Title ID (for ownership) | Game name |
| :---: | :-----: | :----: | :----: |
| Pro | prometheus | 5272175 | Overwatch |


#### Game name

The game name should match the name in Battle.net exactly, including special characters


##### Product family

Product family may be found in configs (`C:\Users\<user>\AppData\Roaming\Battle.net`) as e.g.

    {
        "User": {
            "Client": {
                "PlayScreen": {
                    "GameFamily": {
                        "WoW": {                <-- Family
                            "CustomTabOrder": "1"
                        },
                        "D3": {
                            "CustomTabOrder": "2"
                        },
                ...

##### UID

UID may be present in `Battle.net.config` in configs directory if the game was installed, as e.g.

    {
        "Games": {
            "osi_beta": {
                "ServerUid": "osi_beta",        <-- UID
                "LastActioned": "1632131669",
                "Resumable": "true"
            }
    }
    
This may also be helpful in determining UIDs: 

https://wowdev.wiki/TACT#Products (Agent Product is our UID here)

As visible in these tables, multiple versions of a game correspond to different UIDs, **which is currently not supported in plugin architecture for multiple versions in the same region.**

##### Title ID

Title ID can be checked for your games by checking the https://account.battle.net/api/games-and-subs endpoint in a browser while logged in to your Battle.net account

##### Further notes

Battle.net client logs, which can be found in e.g. `%LOCALAPPDATA%\Battle.net\Logs` may be helpful in providing this information. You _may_ be able to find some information in logs for unowned games.


## Development

Install required packages for building and testing:

```bash
pip install -r requirements/dev.txt
```

You may want to install the pacakges in a virtual environment:

```bash
pip install virtualenv
cd galaxy_blizzard_plugin
virtualenv .venv
.venv\Scripts\activate.bat
pip install -r requirements/dev.txt
```

Run tests:
```bash
inv test
```

Build package
```bash
inv build [--output=<output_folder>] [--ziparchive=<zip_package_name.zip>]
```

#### Shortcuts:

Build to local plugins folder
```bash
inv install
```

Build zip package with name indicating current version:
```bash
inv pack
```
