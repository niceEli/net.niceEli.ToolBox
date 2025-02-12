import os
import requests
import webbrowser
import shutil
from time import sleep
from zipfile import ZipFile
import os.path
import platform
from sys import exit


def stringTF(start,end,s):
    return s[s.find(start)+len(start):s.rfind(end)]
    

def cls():
    os.system('cls' 
    if os.name=='nt'
    else 'clear')

################
###   Load   ###
################

W  = '\033[0m'  # white
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[36m' # blue
P  = '\033[35m' # purple
E  = '\033[30;1m' #gray
Y  = '\033[0;33m' #yellow

def colorize(string):
    string = string.replace("$W",W)
    string = string.replace("$R",R)
    string = string.replace("$G",G)
    string = string.replace("$O",O)
    string = string.replace("$B",B)
    string = string.replace("$P",P)
    string = string.replace("$E",E)
    string = string.replace("$Y",Y)
    string = string.replace(r"\n","\n")
    return string

    
####### PROGRAM VERSION #######
cnt_program = 1.7
#indev 1.6 -> Hotfix (1.7)

ver_program = G+"v"+str(cnt_program)+W

ver_info = "$OLEB-net.lem.ToolBox v1.7 (Hotfix) changelog:\n$W-$G Make Default Branch 1.19.2 Untill Full Rewrite (2.0) releases."
####### PROGRAM VERSION #######

repo = "Legacy-Edition-Minigames"

cfg_branch = "1.19.2"
current_hash = R+"unknown"
check_for_updates = -1
online_count_program = 0

fabric = 0
dependencies = 0
optimize = 0
upnp = 0
viafabric = 0
minimotd = 0
styledplayerlist = 0
server_scripts = 0
ram = 0
motd_sync = -1
eula = 0

lebDebugDisableDownloadContent = 0
lebDebugKeepCache = 0
lebDebugSkipPhase2 = 0
lebTBStatus = 0

def readConfig():
    global cfg_branch
    global current_hash
    global motd_sync
    global check_for_updates
    isUpdating = 0
    try:      
        if os.path.isfile('LEB-ToolBox_old.exe') or os.path.isfile('LEB-ToolBox_old') or os.path.isfile('LEB-ToolBox_DELETE_ME.exe') or os.path.isfile('LEB-ToolBox_DELETE_ME'):
            isUpdating = 1
        if os.path.isfile('LEB-net.lem.ToolBox.cfg'):
            raw = open("LEB-net.lem.ToolBox.cfg", "r")
            f = raw.read()
            file_split = f.split("#/#")
            cfg_branch = file_split[0]
            motd_sync = int(file_split[1])
            current_hash = file_split[2]
            check_for_updates = int(file_split[3])
        else:
            print(O+"***************************************************************************"+W)
            print(G+r"""    __    __________              ______            ______            
   / /   / ____/ __ )            /_  __/___  ____  / / __ )____  _  __
  / /   / __/ / __  |  ______     / / / __ \/ __ \/ / __  / __ \| |/_/
 / /___/ /___/ /_/ /  /_____/    / / / /_/ / /_/ / / /_/ / /_/ />  <  
/_____/_____/_____/             /_/  \____/\____/_/_____/\____/_/|_|  
                                                                      """+ver_program+W)
            print(O+"***************************************************************************"+W)
            print("")
            print("Welcome to LEB-net.lem.ToolBox!")
            print("")
            print("LEB-net.lem.ToolBox is a tool designed to make it easy for users to install, update and customize their own LEB instance.")
            print("To navigate through the program, wait until a blue <Input:> message appears. Then, use the numbers displayed on screen to select your choice and press ENTER.")
            print("")
            print("If you encounter any problem, try performing a clean reinstall or contact us on our Discord.")
            print(B+"LEB"+W+"-"+G+"net.lem.ToolBox "+W+"created by Pi"+R+"por"+O+"Games"+W)
            print(E+"Legacy Edition"+O+" Battle"+W+" created by "+R+"DBTDerpbox "+E+"+"+B+" contributors"+W)
            print("Consider donating at"+O+" Patreon"+W+"! "+O+"patreon.com/DBTDerpbox"+W)
            print("")
            print("Have fun!")
            print("")
            action = input(B+"Press ENTER to continue . . ."+W)
            raw = open("LEB-net.lem.ToolBox.cfg", "w")
            raw.write("1.19.2#/#1#/#unknown#/#1#/#0")
            raw.close()
    except:
        if isUpdating == 0:
            print(R+"An error has ocurred while trying to load the configuration file.")
            print(W+"If you have updated the program recently, it might mean that the program requires a configuration upgrade.")
            print("The program will try to convert the old configuration version to the new format required.")
            print("")
            print(P+"Do you want to continue?")
            action = input(B+"Input [Y/N] (defualt=Yes): "+W)
        else:
            action = "y"
        if action.lower() == "y":
            try:
                print("")
                print("Trying to convert old configuration...")
                raw = open("LEB-net.lem.ToolBox.cfg", "r")
                f = raw.read()
                file_split = f.split("#/#")
                cfg_branch = file_split[0]
                motd_sync = int(file_split[1])
                current_hash = file_split[2]
                check_for_updates = int(file_split[3])
            except:
                pass
            finally:
                if cfg_branch == "":
                    cfg_branch = "1.19.2"
                if motd_sync == -1:
                    motd_sync = 1
                if current_hash == "":
                    current_hash = R+"unknown"
                if check_for_updates == -1:
                    check_for_updates = 1
                raw.close()
                raw = open("LEB-net.lem.ToolBox.cfg", "w")
                print(str(motd_sync))
                raw.write(cfg_branch+"#/#"+str(motd_sync)+"#/#"+current_hash+"#/#"+str(check_for_updates)+"#/#0")
                raw.close()
                print("Conversion finished.")
                readConfig()
        elif action.lower() == "n":
            print("")
        else:
            raw = open("LEB-net.lem.ToolBox.cfg", "w")
            raw.write("main#/#1#/#unknown#/#1#/#0")
            raw.close()
    finally:
        raw.close()
if os.name=='nt':
    os.system('title LEB-net.lem.ToolBox v'+str(cnt_program))

################
###   GUIs   ###
################

def mainMenu():
    readConfig()
    cls()
    print("=============================================================================")
    print(G+r"""    __    __________              ______            ______            
   / /   / ____/ __ )            /_  __/___  ____  / / __ )____  _  __
  / /   / __/ / __  |  ______     / / / __ \/ __ \/ / __  / __ \| |/_/
 / /___/ /___/ /_/ /  /_____/    / / / /_/ / /_/ / / /_/ / /_/ />  <  
/_____/_____/_____/             /_/  \____/\____/_/_____/\____/_/|_|  
                                                                      """+ver_program+W)
    if lebTBStatus == 0:
        print("")
    elif lebTBStatus == 1:
        print(E+"(i) The program is fully updated."+W)
    elif lebTBStatus == -1:
        print(O+"(!) There are new updates available."+W)
    elif lebTBStatus == -2:
        print(Y+"(!) There are new updates, but none are available for your system yet."+W)
    elif lebTBStatus == -3:
        print(R+"[!!!] You are running a developer/pre-release version of this program! "+W)
    print("=============================================================================")
    print("")
    print(P+"Choose an action below:"+W)
    print("")
    print(Y+"--- Legacy Edition Battle ---"+W)
    try:
        f = open("fabric-server-launch.jar")
        print("0. Start LEB Server")
        print("1. Update LEB " + E +"(current commit installed: " +G+current_hash+E+")"+W)
        f.close()
    except IOError:
        print("1. Install LEB")
    print("")
    print(Y+"--- Customize aspects ---"+W)
    print("2. Settings")
    print("3. Change branch (current selected branch: ", B+cfg_branch+W, ")")
    print("")
    print(Y+"--- Documentation ---"+W)
    print("4. Open GitHub project page")
    print("5. See the Changelog")
    print("")
    print("")
    print("6. Exit")
    print("")
    action = input(B+"Input: "+W)
    if action == "0":
        try:
            f = open("fabric-server-launch.jar")
            f.close()
            cls()
            print(G+"****************************")
            print("*** LEB Server Launching ***")
            print("****************************"+W)
            print("")
            if platform.system() == "Linux":
                os.system("./Run-Linux.sh")
            elif platform.system() == "Darwin":
                os.system("./Run-MacOS.sh")
            elif platform.system() == "Windows":
                os.system("Run-Windows.cmd")
            print("")
            print(R+"***************************")
            print("*** LEB Server Stopping ***")
            print("***************************"+W)
            print("")
            action = input(B+"Press ENTER to return to the main menu . . ."+W)
            mainMenu()
        except IOError:
            mainMenu()  
    elif action == "1":
        try:
            f = open("fabric-server-launch.jar")
            f.close()
            updateMenu()
        except IOError:
            installMenu()  
    elif action == "2":
        settingsMenu()
    elif action == "3":
        changeBranch()
    elif action == "4":
        webbrowser.open('https://github.com/Legacy-Edition-Minigames/Minigames')
        mainMenu()
    elif action == "5":
        changeLog()
    elif action == "6":
        exit()
    elif action == "debug nodownload": #forces not to download or extract the lebupdatecache/leb.zip file. THIS OPTION WILL MAKE LEB-TOOLBOX UNSTABLE (MIGHT CRASH).
        global lebDebugSkipPhase2
        lebDebugSkipPhase2 = 1
        action = input(B+"forced skip download and install of phase 2"+W)
        mainMenu()
    elif action == "debug forcecache": #forces to use local lebupdatecache/leb.zip file instead of downloading it from github.
        global lebDebugDisableDownloadContent
        lebDebugDisableDownloadContent = 1
        action = input(B+"forced use local lebupdatecache/leb.zip when on install phase 2 instead of downloading"+W)
        mainMenu()
    elif action == "debug keepcache": #forces to use keep lebupdatecache/leb.zip file instead of removing it right after extracting the files.
        global lebDebugKeepCache
        lebDebugKeepCache = 1
        action = input(B+"forced keep lebupdatecache/leb.zip folder after installing"+W)
        mainMenu()
    elif action == "debug reinstall": #opens reinstall GUI
        reinstall()
    elif action == "debug install": #opens install GUI
        installMenu()
    elif action == "debug setmotd": #executes the set MOTD function. toggles on and off this feature
        setMOTD()
    elif action == "debug repo": #changes the repo for update checking to the my own. usefull for experimental features that require changes on the main github.
        global repo
        repo = "PiporGames"
        action = input(B+"changed repo fetching to PiporGames"+W)
        mainMenu()
    elif action == "debug cfu": #executes the CFU routine function. kinda experimental for now.
        var111 = checkForUpdates()
        print(str(var111))
        input("")
        mainMenu()
    else:
        mainMenu()

def installMenu():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print("=======================================================")
    print("")
    print(G+"Welcome to the LEB setup wizard!"+W)
    print("Thank you for downloading LEB. This wizard will help you setup your own LEB server instance.")
    print("The setup will ask you some questions before proceeding to setup everything.")
    print("")
    print("Consider donating if you want to support this project.")
    print("We hope you have fun!")
    print("")
    print(P+"Press " + B+ "ENTER " + P+ "to continue  . . ." + W)
    print("")
    action = input("")
    installMenu_2()
    
def installMenu_2():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Install type (1/1)"+W)
    print("=======================================================")
    print("")
    print(G+"Install type:"+W)
    print("1. Full Install"+W+":"+E+" This option will install every dependency and enhancement needed for LEB to work as intended."+W)
    print("2. Minimal Install"+W+":"+E+" This option will install only necesary dependencies for LEB to work, without any enhancements."+W)
    print("3. Custom Install"+W+":"+E+" You will be asked what components to install individually."+W)
    print("")
    print(P+"Choose a install type from above:"+W)
    print("")
    action = input(B+"Input: "+W)

    global fabric
    global dependencies
    global optimize
    global upnp
    global viafabric
    global server_scripts
    global minimotd
    global styledplayerlist
    global motd_sync
    global EULA
    eula = 0
    # set 0 / nothing = user choice
    # set 1 = install
    # set 2 = do not install
    if action == "1":
        fabric = 1
        dependencies = 1
        optimize = 1
        upnp = 1
        viafabric = 1
        minimotd = 1
        styledplayerlist = 1
        server_scripts = 1
        motd_sync = 1
        installMenu_3()
    elif action == "2":
        fabric = 1
        dependencies = 1
        optimize = 2
        upnp = 2
        viafabric = 2
        minimotd = 2
        styledplayerlist = 2
        server_scripts = 2
        motd_sync = 2
        installMenu_3()
    elif action == "3":
        fabric = 0
        dependencies = 0
        optimize = 0
        upnp = 0
        viafabric = 0
        minimotd = 0
        styledplayerlist = 0
        server_scripts = 0
        motd_sync = 0
        installMenu_3()
    else:
        installMenu_2()

        
def installMenu_3():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Components (1/2)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to install "+G+"Fabric"+B+"?"+W)
    print("Fabric is the core server component of the server and it " +R+"MUST"+W+" be installed, not just to make LEB work, but to actually be able to run the server itself.")
    print("Besides upgrading the Fabric version because of extraordinary circumstances, you should always install this component.")
    print("")
    print(R+"WARNING: LEB WON'T WORK IF THIS COMPONENT IS NOT INSTALLED!")
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global fabric   
    if fabric == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
        if action.lower() == "y":
            fabric = 1
            installMenu_4()
        elif action.lower() == "n":
            fabric = 2
            installMenu_4()
        else:
            installMenu_3()
    else:
        installMenu_4()


def installMenu_4():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Components (2/2)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to install "+G+"Dependencies (multiple components)"+B+"?"+W)
    print("LEB ships with a preset of required dependencies for it to work as intended. This dependencies " +R+"MUST"+W+" be installed to make LEB work as intended.")
    print(B+"The list of dependencies contains:")
    print(G+"- Fabric API")
    print("- ServerUtils")
    print("- SnowballKB")
    print("- Starlight")
    print("- Editable Player NBT Hack")
    print("- No Chat Reports"+W)
    print("Besides upgrading the dependencies version because of extraordinary circumstances, you should always install this component.")
    print("")
    print(R+"WARNING: LEB WON'T WORK IF THIS COMPONENT IS NOT INSTALLED!")
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global dependencies
    if dependencies == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W) 
        if action.lower() == "y":
            dependencies = 1
            installMenu_4_B()
        elif action.lower() == "n":
            dependencies = 2
            installMenu_4_B()
        else:
            installMenu_4()
    else:
        installMenu_4_B()

def installMenu_4_B():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Enhancements (1/9)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to install "+G+"Optimization mods"+B+"?"+W)
    print("LEB Lobby loading delay and memory usage can be reduced with the help of some lightweight modifications to the server-side code.")
    print("Using this will optimize the server to use less of your system's resources without any drawbacks.")
    print(B+"The list of optimization mods contains:")
    print(G+"- FerriteCore")
    print("- Lithium")
    print("- Carpet")
    print("- Krypton")
    print("- ServerCore")
    print("- Very Many Players")
    print("")
    print(E+"This is an optional enhancement."+W)
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global optimize
    if optimize == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
        if action.lower() == "y":
            optimize = 1
            installMenu_5()
        elif action.lower() == "n":
            optimize = 2
            installMenu_5()
        else:
            installMenu_4_B()
    else:
        installMenu_5()

def installMenu_5():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Enhancements (2/9)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to use "+G+"UPnP"+B+"?"+W)
    print("Universal PlugAndPlay (UPnP) is a custom port forwarding protocol used to automatically open your router's port to the outside Internet.")
    print("This is a neat feature to have if you have problems with Port Forwarding or you don't know much about it, and your friends want to connect to your computer"+E+" (asuming you are not playing in a LAN)"+W+".")
    print("This enhancement doesn't work with all types and models of routers out there, check if yours have UPnP before installing!.")
    print("")
    print(E+"This is an optional enhancement."+W)
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global upnp
    if upnp == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
        if action.lower() == "y":
            upnp = 1
            installMenu_6()
        elif action.lower() == "n":
            upnp = 2
            installMenu_6()
        else:
            installMenu_5()
    else:
        installMenu_6()

        
def installMenu_6():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Enhancements (3/9)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to use "+G+"ViaFabric & ViaBackwards"+B+"?"+W)
    print("ViaFabric & ViaBackwards are mods that provides cross-version compatibility, allowing client versions between 1.16 to 1.19 to join the server.")
    print("This is a neat feature to have if your players use mods, resourcepacks, or modified clients that are designed specifically for versions 1.16, 1.17 or 1.19.")
    print("")
    print(E+"This is an optional enhancement."+W)
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global viafabric
    if viafabric == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W) 
        if action.lower() == "y":
            viafabric = 1
            installMenu_6_2()
        elif action.lower() == "n":
            viafabric = 2
            installMenu_6_2()
        else:
            installMenu_6()
    else:
        installMenu_6_2()

def installMenu_6_2():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Enhancements (4/9)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to use "+G+"MiniMOTD"+B+"?"+W)
    print("MiniMOTD is a mod that provides fancy looking server status messages (MOTDs), featuring cool looking gradients, among other things.")
    print("This is a neat feature to have if you want to have cool looking server stats.")
    print("")
    print(E+"This is an optional enhancement."+W)
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global minimotd
    if minimotd == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W) 
        if action.lower() == "y":
            minimotd = 1
            installMenu_6_3()
        elif action.lower() == "n":
            minimotd = 2
            installMenu_6_3()
        else:
            installMenu_6_2()
    else:
        installMenu_6_3()

def installMenu_6_3():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Enhancements (5/9)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to use "+G+"StyledPlayerList"+B+"?"+W)
    print("StyledPlayerList is a mod that provides a fancy looking tablist, featuring cool looking gradients, and some useful stats.")
    print("This is a neat feature to have if you want to make your tablist look a bit less empty.")
    print("")
    print(E+"This is an optional enhancement."+W)
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global styledplayerlist
    if styledplayerlist == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W) 
        if action.lower() == "y":
            styledplayerlist = 1
            installMenu_7()
        elif action.lower() == "n":
            styledplayerlist = 2
            installMenu_7()
        else:
            installMenu_6_3()
    else:
        installMenu_7()


def installMenu_7():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Enhancements (6/9)"+W)
    print("=======================================================")
    print("")
    print(B+"How much "+G+"RAM"+B+" do you want to allocate to LEB?"+W)
    print("Modified servers, such as LEB, require extra memory than default Minecraft servers.")
    print("You can set whatever amount of RAM (in GB) you want to use.")
    print("")
    print(E+"It's recommended to use"+G+" at least 3GB of RAM"+E+" to ensure LEB will work as intended."+W)
    print("")
    print(P+"How much RAM do you want to allocate (in GB)?:"+W)
    print("")
    global ram
    while True:
        try:
            ram = int(input(B+"Input " + G + "[in GB]" + B + ": "+W))
            break;
        except ValueError:
            installMenu_7()
    installMenu_8()

def installMenu_8():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Enhancements (8/9)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to use "+G+"MOTD Sync"+B+"?"+W)
    print("With MOTD Sync enabled, the server's MOTD Message will be synced with the latest official LEB commit's MOTD.")
    print("This is helpfull if you want to quickly determinate if you are running an old version of LEB.")
    print("")
    print(E+"This is an optional enhancement. You can change this setting at the LEB-Toolbox Settings Page."+W)
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global motd_sync
    global cfg_branch
    if motd_sync == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
        if action.lower() == "y":
            try:
                f = open("LEB-net.lem.ToolBox.cfg", "w")
                f.write(cfg_branch+"#/#1")
            finally:
                f.close()
            motd_sync = 1
            installMenu_9()
        elif action.lower() == "n":
            motd_sync = 2
            installMenu_9()
        else:
            installMenu_8()
    else:
        installMenu_9()

def installMenu_9():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Enhancements (9/9)"+W)
    print("=======================================================")
    print("")
    print(B+"Do you want to use "+G+"Server GUI"+B+"?"+W)
    print("With Server GUI enabled, upon server start, a detailed window will apear containg a memory graph, player list and command console.")
    print("This is a nice way of managing your LEB server, but it consumes some (not that much) resources and might not show error logs properly.")
    print("Disabling this component will output instead a black terminal window with lots of debugging logs.")
    print("")
    print(E+"This is an optional enhancement."+W)
    print("")
    print(P+"Do you want to install this component?:"+W)
    print("")
    global server_scripts
    if server_scripts == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)  
        if action.lower() == "y":
            server_scripts = 1
            installMenu_10()
        elif action.lower() == "n":
            server_scripts = 2
            installMenu_10()
        else:
           installMenu_9()
    else:
        installMenu_10()


def installMenu_10():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"EULA Agreement"+W)
    print("=======================================================")
    print("")
    print(B+"Do you accept the "+G+"Minecraft's EULA"+B+"?"+W)
    print("For your server to run you must accept Minecraft's EULA.")
    print("The Minecraft's EULA contains information and rules about what you can do and can't do while using the game.")
    print("Agreement of the Minecraft's EULA is "+R+"strictly needed"+W+", otherwise your server would be illegal to operate and thus, won't open.")
    print("")
    print(R+"WARNING: LEB WON'T WORK IF MINECRAFT'S EULA IS NOT AGREED!")
    print("")
    print(P+"Do you want to accept the "+G+"Minecraft's EULA"+B+"?"+W)
    print("")
    global eula
    if eula == 0:
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)  
        if action.lower() == "y":
            eula = 1
            installMenu_11()
        elif action.lower() == "n":
            eula = 2
            installMenu_11()
        else:
           installMenu_10()
    else:
        installMenu_11()

        
def installMenu_11():
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Ready to Install"+W)
    print("=======================================================")
    print("")
    print(G+"Ready to install LEB!"+W)
    print("You are now ready to install LEB.")
    print("This program will now connect to the internet to download the required files.")
    print("")
    print(P+"Press " + B+ "ENTER " + P+ "to start downloading . . ." + W)
    print("")
    action = input("")
    installMenu_12()

def installMenu_12():
    global fabric
    global dependencies
    global optimize
    global upnp
    global viafabric
    global minimotd
    global styledplayerlist
    global server_scripts
    global motd_sync
    global ram
    cls()
    print("=======================================================")
    print(G+"Install LEB"+W)
    print(G+"Installing..."+W)
    print("=======================================================")
    print("")
    print(G+"Installing LEB!"+W)
    print("")
    prepare()
    #fabric
    if fabric == 1:
        print("Downloading Fabric...", end='')
        sleep(0.05)
        try:
            fabricurl = requests.get('https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.1/fabric-installer-0.11.1.jar', allow_redirects=True)
            open("fabricinstaller.jar", "wb").write(fabricurl.content)
            print(G+"DONE"+W)
            print("Installing Fabric...", end='')
            sleep(0.05)
            os.system('java -jar fabricinstaller.jar server -mcversion 1.19.2 -downloadMinecraft')     
            print(G+"DONE"+W)     
            print("Removing Fabric installer files...", end='')
            os.remove("fabricinstaller.jar")  
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
    else:
        print(R+"Skipping Fabric install... FABRIC IS A REQUIRED COMPONENT, BE SURE TO INSTALL IT MANUALLY AFTERWARDS"+W)
        sleep(0.05)
    #dependencies
    if dependencies == 1:
        print("Downloading Dependencies "+B+"["+W)
        sleep(0.05)
        try:
            os.mkdir('mods')
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading FabricAPI...", end='')
            sleep(0.05)
            fabricapiurl = requests.get('https://cdn.modrinth.com/data/P7dR8mSH/versions/mrB7EiW4/fabric-api-0.70.0%2B1.19.2.jar', allow_redirects=True)
            open('mods/fabric-api-0.70.0+1.19.2.jar', 'wb').write(fabricapiurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading ServerUtils...", end='')
            sleep(0.05)
            serverutilsurl = requests.get('https://github.com/kyrptonaught/Server-Utils/releases/download/1.0.5/ServerUtils-1.0.5-1.19.jar', allow_redirects=True)
            open('mods/ServerUtils-1.0.5-1.19.jar', 'wb').write(serverutilsurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading SnowballKB...", end='')
            sleep(0.05)
            snowballkburl = requests.get('https://mediafilez.forgecdn.net/files/3885/676/snowballkb-1.2-1.19.jar', allow_redirects=True)
            open('mods/snowballkb-1.2-1.19.jar', 'wb').write(snowballkburl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading Starlight...", end='')
            sleep(0.05)
            starlighturl = requests.get('https://cdn.modrinth.com/data/H8CaAYZC/versions/1.1.1%2B1.19/starlight-1.1.1%2Bfabric.ae22326.jar', allow_redirects=True)
            open('mods/starlight-1.1.1+fabric.ae22326.jar', 'wb').write(starlighturl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading Editable Player NBT Hack...", end='')
            sleep(0.05)
            editnbtplayerurl = requests.get('https://cdn.modrinth.com/data/gY2Q7o7X/versions/EDCQqJQg/editableplayernbthack-1.1.0-1.19.2.jar', allow_redirects=True)
            open('mods/editableplayernbthack-1.1.0-1.19.2.jar', 'wb').write(editnbtplayerurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading No Chat Reports...", end='')
            sleep(0.05)
            vmpurl = requests.get('https://cdn.modrinth.com/data/qQyHxfxd/versions/YuX53PIA/NoChatReports-FABRIC-1.19.2-v1.13.12.jar', allow_redirects=True)
            open('mods/NoChatReports-FABRIC-1.19.2-v1.13.12.jar', 'wb').write(vmpurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        print(B+"] "+W+"Dependencies "+G+"DONE"+W)
    else:
        print(R+"Skipping Dependencies... DEPENDENCIES ARE REQUIRED COMPONENTS, BE SURE TO INSTALL THEM MANUALLY AFTERWARDS"+W)
        sleep(0.05)
    #optimize
    if optimize == 1:
        print("Downloading Optimizations "+B+"["+W)
        sleep(0.05)
        try:
            os.mkdir('mods')
        except OSError as error:
            print("", end='')
            pass
        try:
            print("Downloading FerriteCore...", end='')
            sleep(0.05)
            ferritecoreurl = requests.get('https://cdn.modrinth.com/data/uXXizFIs/versions/kwjHqfz7/ferritecore-5.0.3-fabric.jar', allow_redirects=True)
            open('mods/ferritecore-5.0.3-fabric.jar', 'wb').write(ferritecoreurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading Lithium...", end='')
            sleep(0.05)
            lithiumurl = requests.get('https://cdn.modrinth.com/data/gvQqBUqZ/versions/7scJ9RTg/lithium-fabric-mc1.19.2-0.10.4.jar', allow_redirects=True)
            open('mods/lithium-fabric-mc1.19.2-0.10.4.jar', 'wb').write(lithiumurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading Carpet...", end='')
            sleep(0.05)
            carpeturl = requests.get('https://mediafilez.forgecdn.net/files/4033/215/fabric-carpet-1.19.2-1.4.84%2Bv221018.jar', allow_redirects=True)
            open('mods/fabric-carpet-1.19.2-1.4.84+v221018.jar', 'wb').write(carpeturl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading Krypton...", end='')
            sleep(0.05)
            kryptonurl = requests.get('https://cdn.modrinth.com/data/fQEb0iXm/versions/0.2.1/krypton-0.2.1.jar', allow_redirects=True)
            open('mods/krypton-0.2.1.jar', 'wb').write(kryptonurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading ServerCore...", end='')
            sleep(0.05)
            servercoreurl = requests.get('https://cdn.modrinth.com/data/4WWQxlQP/versions/kzD8EGTS/servercore-1.3.3-1.19.2.jar', allow_redirects=True)
            open('mods/servercore-1.3.3-1.19.2.jar', 'wb').write(servercoreurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        try:
            print("Downloading Very Many Players...", end='')
            sleep(0.05)
            vmpurl = requests.get('https://cdn.modrinth.com/data/wnEe9KBa/versions/2tNVStHO/vmp-fabric-mc1.19.2-0.2.0%2Bbeta.7.23-all.jar', allow_redirects=True)
            open('mods/vmp-fabric-mc1.19.2-0.2.0+beta.7.23-all.jar', 'wb').write(vmpurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        print(B+"] "+W+"Optimizations "+G+"DONE"+W)
    else:
        print(E+"Skipping Optimizations..."+W)
        sleep(0.05)
    #upnp
    if upnp == 1:
        print("Downloading dedicatedUPnP...", end='')
        sleep(0.05)
        try:
            dedicatedmcupnpurl = requests.get('https://mediafilez.forgecdn.net/files/3835/172/dedicatedmcupnp-1.2.1.jar', allow_redirects=True)
            open('mods/dedicatedmcupnp-1.2.1.jar', 'wb').write(dedicatedmcupnpurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
    else:
        print(E+"Skipping UPnP..."+W)
        sleep(0.05)
    #viafabric
    if viafabric == 1:
        print("Downloading ViaFabric...", end='')
        sleep(0.05)
        try:
            viafabricurl = requests.get('https://cdn.modrinth.com/data/YlKdE5VK/versions/Su0V35Vs/viafabric-0.4.9%2B22-main.jar', allow_redirects=True)
            open('mods/viafabric-0.4.9+22-main.jar', 'wb').write(viafabricurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
        print("Downloading ViaBackwards...", end='')
        sleep(0.05)
        try:
            viabackwardsurl = requests.get('https://github.com/ViaVersion/ViaBackwards/releases/download/4.5.1/ViaBackwards-4.5.1.jar', allow_redirects=True)
            open('mods/ViaBackwards-4.5.1.jar', 'wb').write(viabackwardsurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
    else:
        print(E+"Skipping ViaFabric..."+W)
        sleep(0.05)
        print(E+"Skipping ViaBackwards..."+W)
        sleep(0.05)
    #minimotd
    if minimotd == 1:
        print("Downloading MiniMOTD...", end='')
        sleep(0.05)
        try:
            minimotdurl = requests.get('https://cdn.modrinth.com/data/16vhQOQN/versions/c745jM85/minimotd-fabric-mc1.19.2-2.0.9.jar', allow_redirects=True)
            open('mods/minimotd-fabric-mc1.19.2-2.0.9.jar', 'wb').write(minimotdurl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
    else:
        print(E+"Skipping MiniMOTD..."+W)
        sleep(0.05)
    #styledplayerlist
    if styledplayerlist == 1:
        print("Downloading StyledPlayerList...", end='')
        sleep(0.05)
        try:
            styledplayerlisturl = requests.get('https://cdn.modrinth.com/data/DQIfKUHf/versions/2.2.2%2B1.19.1/styledplayerlist-2.2.2%2B1.19.1.jar', allow_redirects=True)
            open('mods/styledplayerlist-2.2.2+1.19.1.jar', 'wb').write(styledplayerlisturl.content)
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
    else:
        print(E+"Skipping StyledPlayerList..."+W)
        sleep(0.05)
    #scripts
    ram = (str(ram))
    print("Creating server scripts "+B+"["+W)
    sleep(0.05)
    print(B+"RAM...: " + G + ram + B + " GB"+W)
    print(B+"Server GUI...: " + G, end='')
    if server_scripts == 1:
        print("Yes")
    else:
        print("No")
    print(B+"MOTD Sync...: " + G, end='')
    if motd_sync == 1:
        print("Yes")
    else:
        print("No")
    try:
        if server_scripts == 1:
            scriptgui = ""
        else:
            scriptgui = "nogui"
        #Windows
        winscript = open("Run-Windows.cmd","w")
        #MacOS
        macscript = open("Run-MacOS.sh","w")
        #Linux
        linuxscript = open("Run-Linux.sh","w")
                           
        winscript.write("@ECHO OFF\njava -Xmx"+ram+"G -Xms"+ram+"G -jar fabric-server-launch.jar "+scriptgui+"\nPAUSE")
        macscript.write("exec java -Xmx"+ram+"G -Xms"+ram+"G -jar fabric-server-launch.jar "+scriptgui)
        linuxscript.write("java -Xmx"+ram+"G -Xms"+ram+"G -jar fabric-server-launch.jar "+scriptgui)

        winscript.close()
        macscript.close()
        linuxscript.close()

        #linux chmod
        if platform.system() == "Linux":
            os.system("chmod +x Run-Linux.sh")
        #MacOS chmod
        if platform.system() == "Darwin":
            os.system("chmod +x Run-MacOS.sh")
    except OSError as error:
        print(R+"FAIL (" + str(error) + ")"+W)
    print(B+"] "+W+"Creating server scripts "+G+"DONE"+W)
    #EULA
    if eula == 1:
        print("Agreeing Minecraft EULA...", end='')
        sleep(0.05)
        try:
            eulafile = open("eula.txt","w")
            eulafile.write("eula=TRUE")
            eulafile.close()
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ")"+W)
    else:
        print(R+"Skipping Minecraft's EULA agreement... MINECRAFT'S EULA AGREEMENT IS REQUIERED, BE SURE TO SET EULA=TRUE AT eula.txt OR IT WON'T RUN"+W)
        sleep(0.05)
    print("")
    print("")
    print(G+"*** Core-Server Setup successful! ***"+W)
    print("")
    print(E+"Preparing to install LEB-Resources in 5 seconds . . ."+W)
    sleep(5)
    prepare()
    if lebDebugSkipPhase2 == 0:
        downloadInstall()
        setMOTD()
        clean()
    print("")
    print(G+"***************************")
    print("*** Install successful! ***")
    print("***************************"+W)
    print("")
    action = input(B+"Press ENTER to continue . . ."+W)
    installMenu_13()


def installMenu_13():
    cls()
    print("=======================================================")
    print(G+"LEB Install Completed"+W)
    print(G+"Finish setup"+W)
    print("=======================================================")
    print("")
    print(G+"LEB has been installed successfully!"+W)
    print("You are now ready to run your own LEB server.")
    print("To run your server, select the option <<0. Start LEB Server>> at the LEB-net.lem.ToolBox main menu, or execute the file called <<Run ...>> and your OS of preference.")
    print("You can change your LEB net.lem.ToolBox and server settings at the Settings page.")
    print("")
    print(B+"LEB"+W+"-"+G+"net.lem.ToolBox "+W+"created by Pi"+R+"por"+O+"Games"+W)
    print(E+"Legacy Edition"+O+" Battle"+W+" created by "+R+"DBTDerpbox "+E+"+"+B+" contributors"+W)
    print("Consider donating at"+O+" Patreon"+W+"! "+O+"patreon.com/DBTDerpbox"+W)
    print("")
    action = input(B+"Press ENTER to return to the main menu . . ."+W)
    mainMenu()

    
def updateMenu():
    cls()
    print("=======================================================")
    print(G+"Update LEB"+W)
    print("=======================================================")
    print("")
    print(P+"Choose an action below:"+W)
    print("")
    print("1. Update to the latest commit available " + E +"(current commit installed: " +G+current_hash+E+")"+W)
    print("2. Perform a Clean update to the latest commit available")
    print("3. Reinstall LEB")
    print("")
    print("4. Change branch (current selected branch: ", B+cfg_branch+W, ")")
    print("")
    print("5. Exit")
    print("")
    action = input(B+"Input: "+W)
    
    if action == "1":
        updater()
    elif action == "2":
        cleanUpdater()
    elif action == "3":
        reinstallMenu()
    elif action == "4":
        changeBranch()
    elif action == "5":
        mainMenu()
    else:
        updateMenu()


def updater():
    cls()
    print("=======================================================")
    print(G+"Update LEB > Update to the latest commit available"+W)
    print("=======================================================")
    print("")
    print("This will update you current server to the latest version (commit) uploaded to the GitHub repository.")
    print("")
    print(P+"Are you sure you want to update to the last commit?"+W)
    print("")
    action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
    if action.lower() == "y":
        print(E+"User authorised operation, executing..."+W)
         #continue execution
    elif action.lower() == "n":
        mainMenu()
    else:
        updater()
    print("")
    prepare()
    backup()
    if lebDebugSkipPhase2 == 0:
        downloadInstall()
        setMOTD()
        restore()
        clean()
    print()
    print(G+"*** Update successful! ***"+W)
    print("")
    action2 = input(B+"Press ENTER to continue . . ."+W)
    mainMenu()

def cleanUpdater():
    cls()
    print("=======================================================")
    print(G+"Update LEB > Perform a Clean update to the latest commit available"+W)
    print("=======================================================")
    print("")
    print(R+"WARNING!: Performing a Clean Update will erase all player save data (ex: advancements).")
    print("It's recommended to backup playerdata to avoid loosing player-specific-settings, custom presets, advancements,...")
    print("If you are troubleshooting problems on a mirrored server, feel free to continue." +W)
    print("")
    print(P+"Are you sure you want to ERASE everything and install again?"+W)
    print("")
    action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
    if action.lower() == "y":
        print(E+"User authorised operation, executing..."+W)
         #continue execution
    elif action.lower() == "n":
        mainMenu()
    else:
        cleanUpdater()
    print("")
    prepare()
    if lebDebugSkipPhase2 == 0:
        downloadInstall()
        setMOTD()
        clean()
    print()
    print(G+"*** Clean Update successful! ***"+W)
    print("")
    action2 = input(B+"Press ENTER to continue . . ."+W)
    mainMenu()

def reinstallMenu():
    cls()
    print("=======================================================")
    print(G+"Update LEB > Reinstall LEB"+W)
    print("=======================================================")
    print("")
    print(R+"WARNING!: Reinstalling LEB will erase ALL DATA, including server files, player data and LEB resources.")
    print("It's recommended to backup the folder LEB-net.lem.ToolBox is installed to to avoid losing player-specific-settings, custom presets, advancements,...")
    print("If you are troubleshooting problems on a mirrored server, feel free to continue." +W)
    print("")
    print(P+"Are you sure you want to TRULY ERASE EVERYTHING NO JOKES and install again?"+W)
    print("")
    action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
    if action.lower() == "y":
        print("Performing deletion of "+R+"ALL DATA"+W+" in "+E+"10 seconds."+R+" Close the program NOW if you don't want to do this!! (CTRL+C on Linux)")
        sleep(10)
        print(E+"User authorised operation, executing..."+W)
         #continue execution
    elif action.lower() == "n":
        mainMenu()
    else:
        cleanUpdater()
    print("")
    reinstall()
    installMenu()
    #I think this part of the code won't be executing anytime soon, but who cares.
    print()
    print(G+"*** Reinstall successful! ***"+W)
    print("")
    action2 = input(B+"Press ENTER to continue . . ."+W)
    mainMenu()
    
def changeBranch():
    cls()
    print("=======================================================")
    print(B+"Change Branch"+W)
    print("=======================================================")
    print("")
    print("You can choose whatever branch you feel like using by selecting one of the displayed branches below.")
    print("The default (most stable and updated) branch is "+G+"MAIN"+W+".")
    print("Using branches other than "+G+"MAIN"+W+" might break the server (which could include player savedata!). "+E+R+"Test with caution!"+E)
    print("")
    print("To select a branch, type the corresponding number or type the name of the branch in the text box (be sure it's correctly spelled or LEB-net.lem.ToolBox will break!).")
    print("")
    print(G+"Default branches:"+W)
    print("1. 1.19.2 (Default)")
    print("2. main")
    print("")
    print(P+"Avaible branches:"+W)
    print("3. testing")
    print("4. experimental-dev")
    print("5. experimental-server")
    print("")
    print("6. Exit")
    print("")
    action = input(B+"Input: "+W)

    global cfg_branch

    if action == "6":
         mainMenu()
    if action == "1":
        cfg_branch = "1.19.2"
    elif action == "2":
        cfg_branch = "main"
    elif action == "3":
        cfg_branch = "testing"
    elif action == "4":
        cfg_branch = "experimental-dev"
    elif action == "5":
        cfg_branch = "experimental-server"
    else:
        cfg_branch = action
    print(W+"Branch has been updated to "+P+cfg_branch+W+".")
    sleep(2.5)
    writeConfig(cfg_branch,motd_sync,current_hash,check_for_updates)
    mainMenu()


def settingsMenu():
    readConfig()
    response_motd = ""
    response_cfu = ""
    if motd_sync == 1:
        response_motd = G+"TRUE"+W
    else:
        response_motd = R+"FALSE"+W
    if check_for_updates == 1:
        response_cfu = G+"TRUE"+W
    else:
        response_cfu = R+"FALSE"+W
    cls()
    print("=======================================================")
    print(G+"Settings"+W)
    print("=======================================================")
    print("")
    print("Welcome to the Settings page: Change your net.lem.ToolBox/Server settings here.")
    print(E+"Program version: "+ver_program+W)
    print("")
    print(G+"LEB-net.lem.ToolBox Settings:"+W)
    print("")
    print("1. Change branch (current selected branch: ", B+cfg_branch+W, ")")
    print(E+"   Allows you to change the build branch the server is running on."+W)
    print("2. Update LEB-net.lem.ToolBox (current version: "+ver_program+W+")")
    print(E+"   Update LEB-net.lem.ToolBox to the latest stable version available at GitHub."+W)
    print("3. Check for LEB-net.lem.ToolBox updates at startup ("+response_cfu+")"+W)
    print(E+"   This will check if there are any updates available for LEB-net.lem.ToolBox when you start the application."+W)
    print("")
    print(B+"Server Settings:"+W)
    print("")
    print("4. Use MOTD Sync ("+response_motd+")"+W)
    print(E+"   Automatically syncs the MOTD of the server with the commit version currently installed."+W)
    print("")
    print("")
    print("5. Exit")
    print("")
    print(P+"Choose an action below:"+W)
    print("")
    action = input(B+"Input: "+W)
    if motd_sync == 1:
        response_motd = 1
    else:
        response_motd = 0
        
    if check_for_updates == 1:
        response_cfu = 1
    else:
        response_cfu = 0
        
    if action == "1":
        changeBranch()
    elif action == "2":
        updateLEBTB()
    elif action == "3":
        print("")
        if response_cfu == 1:
            writeConfig(cfg_branch,motd_sync,current_hash,"0")
            print("CFU at startup has been "+R+"disabled"+W+" successfully.")
        else:
            writeConfig(cfg_branch,motd_sync,current_hash,"1")
            print("CFU at startup has been "+G+"enabled"+W+" successfully.")   
        print("")
        sleep(2)
        settingsMenu()
    elif action == "4":
        print("")
        if response_motd == 1:
            writeConfig(cfg_branch,"0",current_hash,check_for_updates)
            print("MOTD Sync has been "+R+"disabled"+W+" successfully.")
        else:
            writeConfig(cfg_branch,"1",current_hash,check_for_updates)
            print("MOTD Sync has been "+G+"enabled"+W+" successfully.")
            print(W+"To apply the changes, you must <Update to the last commit> from the Update page."+W)
        print("")
        sleep(3)
        settingsMenu()
        print("")
        readConfig()
        print("")
        sleep(2)
        settingsMenu()
    elif action == "5":
        mainMenu()
    else:
        settingsMenu()


def updateLEBTB():
    cls()
    print("=======================================================")
    print(G+"Update LEB-net.lem.ToolBox"+W)
    print("=======================================================")
    print("")
    print("You can update your LEB-net.lem.ToolBox program to the latest stable version available at GitHub.")
    print("The current LEB-net.lem.ToolBox program version is "+ver_program+W)
    print("Newer LEB-net.lem.ToolBox updates might ship with new features, bugfixes, and other improvements!")
    print("")
    print(E+"Searching for updates . . ."+W)
    print("")
    result = checkForUpdates()
    result2 = checkForChangeLog()
    cls()
    print("=======================================================")
    print(G+"Update LEB-net.lem.ToolBox"+W)
    print("=======================================================")
    print("")
    print("You can update your LEB-net.lem.ToolBox program to the latest stable version available at GitHub.")
    print("The current LEB-net.lem.ToolBox program version is "+ver_program+W)
    print("Newer LEB-net.lem.ToolBox updates might ship with new features, bugfixes, and other improvements!")
    print("")
    if result == 0:
        print(E+"There aren't any new updates. Your program is fully updated.")
        print("")
        action = input(B+"Press ENTER to return . . ."+W)
        settingsMenu()
    elif result == -1:
        print(R+"An unknown error has occurred while fetching the required information.")
        print("")
        action = input(R+"Press ENTER to return . . ."+W)
        settingsMenu()
    elif result == 2:
        print(R+"A new version has been detected, but no compatible builds are available at the time for your operating system.")
        print(W+"Wait until a build is compiled for your version or (for advanced users) build your own using the source code available at GitHub.")
        print(O+"Be warned that running the program from the source code, without compiling, could make some features unavailable.")
        print("")
        action = input(R+"Press ENTER to return . . ."+W)
        settingsMenu()
    elif result == 1:
        print(G+"New update v"+str(online_count_program)+" available!")
        print("")
        print(B+"CHANGELOG:"+W)
        print(result2)
        print("")
        print(P+"Do you want to update now?"+W)
        print("")
        action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
        if action.lower() == "y":
            ### LEB-net.lem.ToolBox update
            print(E+"Preparing to update LEB-net.lem.ToolBox..."+W)
            print("Downloading LEB-net.lem.ToolBox...", end="")
            pgrmfile = ""
            try:
                if platform.system() == "Linux":
                    prgrmfile = requests.get('https://raw.githubusercontent.com/'+repo+'/net.lem.ToolBox/main/LEB-net.lem.ToolBox-v'+str(online_count_program), allow_redirects=True)
                    open("LEB-net.lem.ToolBox-new", "wb").write(prgrmfile.content)
                elif platform.system() == "Darwin":
                    prgrmfile = requests.get('https://raw.githubusercontent.com/'+repo+'/net.lem.ToolBox/main/LEB-net.lem.ToolBox-v'+str(online_count_program), allow_redirects=True)
                    open("LEB-net.lem.ToolBox-new-MacOS", "wb").write(prgrmfile.content)
                elif platform.system() == "Windows":
                    prgrmfile = requests.get('https://raw.githubusercontent.com/'+repo+'/net.lem.ToolBox/main/LEB-net.lem.ToolBox-v'+str(online_count_program)+'.exe', allow_redirects=True)
                    open("LEB-net.lem.ToolBox-new.exe", "wb").write(prgrmfile.content)
                print(G+"DONE"+W)
            except Exception as error:
                print(R+"FAIL ("+str(error)+")"+W)
            print(P+"Do you want to keep the old version (in case the newer version breaks)?"+W)
            print("")
            action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
            try:
                if action.lower() == "y":
                    print("Keeping old version...", end="")
                    if platform.system() == "Linux":
                        os.rename("LEB-net.lem.ToolBox", "LEB-ToolBox_old")
                    elif platform.system() == "Darwin":
                        os.rename("LEB-net.lem.ToolBox-MacOS", "LEB-ToolBox_old-MacOS")
                    elif platform.system() == "Windows":
                        os.rename("LEB-net.lem.ToolBox.exe", "LEB-ToolBox_old.exe")
                else:
                    print("Marking DELETE_ME to old version...", end="")
                    if platform.system() == "Linux":
                        os.rename("LEB-net.lem.ToolBox", "LEB-ToolBox_DELETE_ME")
                    elif platform.system() == "Darwin":
                        os.rename("LEB-net.lem.ToolBox-MacOS", "LEB-ToolBox_DELETE_ME-MacOS")
                    elif platform.system() == "Windows":
                        os.rename("LEB-net.lem.ToolBox.exe", "LEB-ToolBox_DELETE_ME.exe")
                    print(G+"DONE"+W)
            except Exception as error:
                print(R+"FAIL ("+str(error)+")"+W)
            try:
                print("Renaming new update file...", end="")
                if platform.system() == "Linux":
                    os.rename("LEB-net.lem.ToolBox-new", "LEB-net.lem.ToolBox")
                    os.system("chmod +x LEB-net.lem.ToolBox")
                elif platform.system() == "Darwin":
                    os.rename("LEB-net.lem.ToolBox-new-MacOS", "LEB-net.lem.ToolBox-MacOS")
                elif platform.system() == "Windows":
                    os.rename("LEB-net.lem.ToolBox-new.exe", "LEB-net.lem.ToolBox.exe")
            except Exception as error:
                print(R+"FAIL ("+str(error)+")"+W)
            print("")
            print(O+"***" +W+"LEB-net.lem.ToolBox will restart in 5 . . ."+O+" ***"+W)
            print("")
            sleep(5)
            print(E+"Restarting..."+W)
            if platform.system() == "Linux":
                os.system("./LEB-net.lem.ToolBox")
            elif platform.system() == "Darwin":
                os.system("./LEB-net.lem.ToolBox-MacOS")
            elif platform.system() == "Windows":
                os.startfile("LEB-net.lem.ToolBox.exe")
            exit()
        elif action.lower() == "n":
            settingsMenu()
        else:
            updateLEBTB()


def changeLog():
    cls()
    print("=======================================================")
    print(B+"CHANGELOG"+W)
    print("=======================================================")
    print("")
    print("You are now reading the LEB-net.lem.ToolBox "+ver_program+" "+B+"changelog"+W+".")
    print("")
    print(B+"CHANGELOG:"+W)
    print(colorize(ver_info))
    print("")
    print("")
    action = input(B+"Press ENTER to return . . ."+W)
    mainMenu()



    
####################
###   Functions  ###
####################
def writeConfig(var_branch,var_motd_sync,var_hash,var_cfu):
    try:
        f = open("LEB-net.lem.ToolBox.cfg", "w")
        f.write(var_branch+"#/#"+str(var_motd_sync)+"#/#"+var_hash+"#/#"+str(var_cfu))
    finally:
        f.close()

def prepare():
    if lebDebugKeepCache == 0:
        print("Preparing files...", end='')
        sleep(0.05)
        try:
            shutil.rmtree("leb_update_cache")
            os.mkdir("leb_update_cache")
        except OSError as error:
            os.mkdir("leb_update_cache")
            print("", end='')
        finally:
            print(G+"DONE"+W)

def backup():
    print("Backing up...", end='')
    sleep(0.05)      
    try:
        shutil.copytree('world/advancements', 'leb_update_cache/world/advancements')
        shutil.copytree('world/stats', 'leb_update_cache/world/stats')
    except OSError as error:
        print(error, end='')
        pass
    finally:
        print(G+"DONE"+W)


def downloadInstall():
    if lebDebugSkipPhase2 == 0:
        if lebDebugDisableDownloadContent == 0:
            print(E+"Note: Due to GitHub limitations, download ETA is not available."+W)
            print("Downloading LEB build" + E+ " (this can take up to 6 minutes)" + W)
            print("Now downloading...", end='')
            leb_zip = requests.get('https://github.com/Legacy-Edition-Minigames/Minigames/archive/refs/heads/' + cfg_branch+ '.zip', allow_redirects=True, stream=True)
            with open( 'leb_update_cache/leb.zip', "wb" ) as f:
                for chunk in leb_zip.iter_content( chunk_size = 1024 ):
                    if chunk:
                        f.write( chunk )
            print(G+"DONE"+W)
        print("Removing old files "+B+"["+W)
        sleep(0.05)
        files = [".gitignore","INSTALLATION.md","INSTALLATION-MINEHUT.md","LICENSE","README.md","SCREENSHOTS.md","CUSTOMPACK.md"]
        directories = ["world","images","config",".github"]
        try:
            #crear arrays uno de archivos y otro de carpetas y hacer loop
            for file in files:
                if os.path.isfile(file):
                    print ("Removing " + str(file) + " ...", end='')
                    os.remove(file)
                    print(G+"DONE"+W)
            for directory in directories:
                if os.path.isdir(directory):
                    print ("Removing " + str(directory) + " ...", end='')
                    shutil.rmtree(directory)
                    print(G+"DONE"+W)
        except Exception as error:
            print (R+"FAIL ("+str(error)+"), stopping code..."+W, end='')
            pass
        print(B+"] "+W+"Removing old files "+G+"DONE"+W)
        print("Extracting files...", end='')
        sleep(0.05)
        with ZipFile('leb_update_cache/leb.zip', 'r') as zipObj:
            zipObj.extractall()
        print(G+"DONE"+W)
        print("Moving files...", end='')
        sleep(0.05)
        try:
            for filename in os.listdir('Minigames-' + cfg_branch):
                shutil.move('Minigames-' + cfg_branch + "/" + filename, filename)
            shutil.rmtree('Minigames-' + cfg_branch)
        except Exception as error:
            str(error)
        print(G+"DONE"+W)
    

def restore():
    print("Restoring backup...", end='')
    sleep(0.05)
    try:
        shutil.rmtree('world/advancements')
        shutil.rmtree('world/stats')
    except OSError as error:
        print("", end='')
    
    try:
        shutil.copytree('leb_update_cache/world/advancements', 'world/advancements')
        shutil.copytree('leb_update_cache/world/stats', 'world/stats')
    except OSError as error:
        print("", end='')
        pass
    finally:
        print(G+"DONE"+W)
        
    
def clean():
    if lebDebugKeepCache == 0:
        try:
            shutil.rmtree("leb_update_cache")
        except OSError as error:
            print(R+error, end='')
            pass
        finally:
            print(G+"DONE"+W)


def setMOTD():
    if motd_sync == 1:
        try:
            print("Syncing MOTD...", end='')
            #get hash
            leb_zip = ZipFile('leb_update_cache/leb.zip')
            git_hash = "git-" + cfg_branch + "-" + leb_zip.comment.decode("utf-8")[:6]

            #read contents
            with open("server.properties", "r") as motd_file:
                lines = motd_file.readlines()
            with open("server.properties", "w") as motd_file:
                for line in lines:
                    if "motd=" not in line:
                        motd_file.write(line)
                motd_file.write("\nmotd=\u00A79Legacy Edition Battle Public Server \u00A7r\u00A7r\\n" + git_hash)
            motd_file.close()

            minimotd_file = open("config/MiniMOTD/main.conf", "r")
            content = minimotd_file.read()
            old_motd = stringTF("<gradient:#d8d8d8:#2bc7ac><italic>","</gradient>",content)
            new_motd = content.replace(old_motd, git_hash)
            minimotd_file.close()
            
            minimotd_file = open("config/MiniMOTD/main.conf", "w")
            minimotd_file.write(new_motd)
            minimotd_file.close()
            print(G+"DONE"+W)
        except OSError as error:
            print(R+"FAIL (" + str(error) + ") >>> Did leb_update_cache/leb.zip erase itself, or does this branch not contain a miniMOTD/server.properties config file?"+W)
            pass
        finally:
            writeConfig(cfg_branch,motd_sync,leb_zip.comment.decode("utf-8")[:6],check_for_updates)

def reinstall():
    print("Removing "+R+"ALL FILES"+B+" ["+W)
    sleep(0.05)
    files = [".gitignore","INSTALLATION.md","INSTALLATION-MINEHUT.md","LICENSE","README.md","SCREENSHOTS.md","CUSTOMPACK.md","installer.py","banned-ips.json","banned-players.json","eula.txt","fabric-server-launch.jar","fabric-server-launcher.properties","ops.json","Run-Linux.sh","Run-MacOS.sh","Run-Windows.cmd","server.jar","server.properties","usercache.json","whitelist.json"]
    directories = ["world","images","config",".github",".fabric","libraries","logs","mods"]
    try:
        for file in files:
            if os.path.isfile(file):
                print ("Removing " + str(file) + " ...", end='')
                os.remove(file)
                print(G+"DONE"+W)
        for directory in directories:
            if os.path.isdir(directory):
                print ("Removing " + str(directory) + " ...", end='')
                shutil.rmtree(directory)
                print(G+"DONE"+W)
    except Exception as error:
        print (R+"FAIL ("+str(error)+"), stopping code..."+W, end='')
        pass
    print(B+"] "+W+"Removing "+R+"ALL FILES "+G+"DONE"+W)
    sleep(2)

def checkForUpdates():
    global lebTBStatus
    ver1 = 0
    try:
        req = requests.get('https://raw.githubusercontent.com/'+repo+'/net.lem.ToolBox/main/LEB-net.lem.ToolBox.py', allow_redirects=True)
        data = (req.content).decode("utf-8")
        info = data.split("\n")
        for line in info:
            if "cnt_program = " in line:
                value = line.split("cnt_program = ")[1]
                value = value.replace("\r","")
                ver1 = float(value)
                break
    except Exception as error:
        print('checkForUpdates>>'+str(error))
        input()
        return -1
    if ver1 > cnt_program:
        extension = ''
        if platform.system() == "Linux":
            extension = ''
        elif platform.system() == "Darwin":
            extension = '-MacOS'
        elif platform.system() == "Windows":
            extension = '.exe'
        try:
            global online_count_program
            req = requests.get('https://raw.githubusercontent.com/'+repo+'/net.lem.ToolBox/main/LEB-net.lem.ToolBox-v'+str(ver1)+str(extension), allow_redirects=True)
            data = req.content
            if data == b'404: Not Found':
                lebTBStatus = -2
                return 2
            else:            
                online_count_program = ver1
                lebTBStatus = -1
                return 1
        except Exception as error:
                online_count_program = ver1
                return -1
    elif ver1 == cnt_program:
        lebTBStatus = 1
        return 0
    elif ver1 < cnt_program:
        lebTBStatus = -3
        return 0
    else:
        return 0
    
def checkForChangeLog():
    try:
        req = requests.get('https://raw.githubusercontent.com/'+repo+'/net.lem.ToolBox/main/LEB-net.lem.ToolBox.py', allow_redirects=True)
        data = (req.content).decode("utf-8")
        info = data.split("\n")
        for line in info:
            if "ver_info = " in line:
                value = line.split("ver_info = ")[1]
                value = value.replace("\r","")
                changelog = value
                return colorize(str(changelog))
            
    except Exception as error:
        return R+"Error when retrieving changelog ("+str(error)+")."

def rmOldVer():
    if os.path.isfile('LEB-ToolBox_DELETE_ME.exe'):
        try:
            os.remove("LEB-ToolBox_DELETE_ME.exe")
        except Exception as error:
            print(R+str(error)+W)
            print("")
            sleep(3)
            pass
    if os.path.isfile('LEB-ToolBox_DELETE_ME'):
        try:
            os.remove("LEB-ToolBox_DELETE_ME")
        except Exception as error:
            print(R+str(error)+W)
            print("")
            sleep(3)
            pass


### pre-initialization check for updates (cfu) routine ###
def CFU():
    rmOldVer()
    readConfig()
    cls()
    if check_for_updates == 1:
        result = checkForUpdates()
        result2 = checkForChangeLog()
        if result == 1:
            print(O+"*******************************************************"+W)
            print(G+"New LEB-net.lem.ToolBox v"+str(online_count_program)+" update has been found!"+W)
            print(O+"*******************************************************"+W)
            print("")
            print(B+"CHANGELOG:"+W)
            print(result2)
            print("")
            print(P+"Do you want to go to the LEB-net.lem.ToolBox update Menu?"+W)
            print("")
            action = input(B+"Input " + G + "[Y/N]" + B + ": "+W)
            if action.lower() == "y":
                updateLEBTB()




###.#.#.### The one line of code that makes all of this work ###.#.#.###

if __name__ == '__main__':
    readConfig()
    CFU()
    mainMenu()
else:
    print(R+'LEB-net.lem.ToolBox is not designed to be loaded as external code, a library or an addon. This thread will now be terminated.')
    exit



##############################################################################
###  LEB-net.lem.ToolBox, created by PiporGames, with love, for the LEM Community  ###
##############################################################################
