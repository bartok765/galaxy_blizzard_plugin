# Galaxy plugin for Battle.net

This plugin allows you to install and launch your Blizzard games via the GOG Galaxy 2.0 launcher.

## Installation
1. Download [latest](https://github.com/FriendsOfGalaxy/galaxy-integration-blizzard/releases) release of the plugin for your platform.
2. Create plugin folder (if it does not exists yet):
	- Windows: `%LOCALAPPDATA%\GOG.com\Galaxy\plugins\installed\battlenet`
	- MacOS: `${HOME}/Library/Application Support/GOG.com/Galaxy/plugins/installed/blizzard`
3. Unpack plugin to the plugin folder created in step 2.
4. Re-connect(or re-start) your GOG Galaxy Client

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


## Development
Install required packages for building and testing:
```bash
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

If you have classic blizzard games which are not properly detected as installed or don't launch when clicking 'play'
please provide the name and values of the games key under

```Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\```

registry path.

If on MAC please provide the games bundle_id which can be found by calling

```/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep {game_name}```
