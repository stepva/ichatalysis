# iChatalysis

iChatalysis is a simple, stand-alone version of [chatalysis](https://github.com/stepva/chatalysis), my other project, which lets you analyse Apple Messages/iMessages in a nice and clean way. All you need is a Mac, iCloud account on which you save your Messages and Contacts, and iChatalysis does the rest, directly using the data you have on your Mac in a safe way.

## Set-up

1. As mentioned above, iChatalysis only works on Mac, where you need to have your Messages saved (most likely via iCloud). If you use iCloud and have all your Messages and Contacs synced there, you also need to go to the Messages app on your Mac, in the dropdown menu in the top left corner select Messages -> Preferences -> iMessage –> check Enable Messages on iCloud. After that all your Messages will get synced from iCloud to your Mac, if they have not been before.
2. You also need to give your Terminal access to your hidden folders (the Messages), so that iChatalysis can access them. Go to System Preference (settings) -> Security and Privacy –> Privacy -> Full Disk Access. Now allow changes by clicking the lock in the bottom right and find Terminal in the list of apps on the right. If it is not there, you can add it and find it with the plus sign. Check the box by Terminal to give it access.
3. [Download iChatalysis in a zip folder](https://github.com/stepva/ichatalysis/archive/master.zip) and extract it wherever you want to.
4. Download and install [Python 3](https://www.python.org/downloads/) (remember to add it to PATH when installing it) if you do not have it.
5. In your Terminal, navigate to the iChatalysis folder, for example:

```
    cd Desktop/ichatalysis-master
```

6. Install required packages:

```
    pip3 install -r requirements.txt
```

7. Now you can finally run iChatalysis!

```
    python3 ichatalysis
```

or, for example,

```
    python3 Desktop/ichatalysis-master/ichatalysis
```

