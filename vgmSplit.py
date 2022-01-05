import os,configparser,sys,subprocess,shutil
from systemChannels import systemChannels
from defaultIni import defaultIni

VGM_PLAY_PATH = "VGMPlay.exe"
CONFIG_PATH = "VGMPlay.ini"
G_SYSTEM = "YM2151" 
G_VGM_PATH = "dk468sn.vgm"

def initConfig(systemName):
    config = configparser.ConfigParser()
    config.optionxform = str 
    config["General"] = defaultIni
    config[systemName] = {}
    return config

def formatIHex(val):#vgm play is picky about the hex values
    outval = hex(val)[2:].upper()
    outval = "0x" + outval
    return outval


def prepPathToString(path):#encases arg strings with " for compatibility
    return  '"{}"'.format(path)


def renderChannelType(systemName, vgmPath, channelType, config):
    #setup base mute masks
    config[systemName]["MuteMask" + channelType] = hex(0)#just in case
    for otherChannel in systemChannels[systemName]:
        if otherChannel != channelType:
            config[systemName]["MuteMask" + otherChannel] = hex(0xFF)
    #render channels
    for i in range(systemChannels[systemName][channelType]):
        #update config
        mask = hex(~(1 << i) & 0xFF)
        config[systemName]["MuteMask" + channelType] = mask
        f = open(CONFIG_PATH,"w")
        config.write(f)
        f.close()
        print("MUTE MASK {} {}\n".format(channelType ,config[systemName]["MuteMask" + channelType]))
        #render
        subprocess.call("{} {}".format(VGM_PLAY_PATH,prepPathToString(vgmPath)))
        oldWavPath = "{}.wav".format(vgmPath[:-4])
        newWavPath = "{}_{}_CH{}.wav".format(vgmPath[:-4], channelType, i + 1)
        os.rename(oldWavPath, newWavPath)

def renderAll(systemName, vgmPath):
    config = initConfig(systemName)
    for channelType in systemChannels[systemName]:
        renderChannelType(systemName, vgmPath, channelType, config)
    #render master
    for channelType in systemChannels[systemName]:
        config[systemName]["MuteMask" + channelType] = hex(0)
    f = open(CONFIG_PATH,"w")
    config.write(f)
    f.close()
    subprocess.call("{} {}".format(VGM_PLAY_PATH,prepPathToString(vgmPath)))

def test():
    config = initConfig(G_SYSTEM)
    renderChannelType(G_SYSTEM, G_VGM_PATH, "FM", config)

def main():
    #test()
    renderAll(G_SYSTEM, G_VGM_PATH)


main()