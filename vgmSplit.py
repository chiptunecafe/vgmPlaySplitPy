import vgmSystemChannels
import os,configparser,sys,subprocess,shutil
import pdb


VGM_PLAY_PATH = "VGMPlay.exe"
CONFIG_PATH = "VGMPlay.ini"
CHANNEL_COUNT_OVERRIDE = 0
system = "X1-010" #had this implemented differently but too lazy to make it nice

def generateBaseMask(channelCount):#Base mask for generating config mask
    if channelCount == 0:
        return 0
    if channelCount == 1:
        return 1
    x = 1
    for i in range(channelCount - 1):
        x = x << 1
        x = x | 1
    return x

def generateMasks(size,x):#Masks for confing
    #x = 0b1111111111111111
    op = x
    mask = 1
    masks = []
    for i in range(size):
        op = x ^ mask
        mask = mask << 1
        masks.append(op)
        #print("{0:b}".format(op))
    return masks

def prepPathsToStrings(paths):#encases arg strings with " for compatibility
    for i in range(len(paths)):
        paths[i] = format('"{}"'.format(paths[i]))

def prepPathToString(path):#encases arg strings with " for compatibility
    return  '"{}"'.format(path)

def displayMasks(masks):
    for mask in masks:
        print("{0:b} ".format(mask))

def loadAllVGMs(basePath = None):
    currentDirectory = os.listdir(basePath)
    vgmFilePaths = []
    for file in currentDirectory:
        if file.endswith(".vgm") or file.endswith(".vgz"):
            vgmFilePaths.append(file)#add base path
    return vgmFilePaths

def loadBaseConfig(path):
    config = configparser.ConfigParser()
    config.optionxform = str 
    config.read(path)
    return config

def writeMuteMask(mask,config,system,path):
    config[system]["MuteMask"] = str(mask)
    f = open(path,"w")
    config.write(f)
    f.close()

def renderAll(path = None):#temp clammped system val
        #channelCountOverRide is for removing last x channels
    #channel mute init
    channelCount = 0
    if system in vgmSystemChannels.systemsChannelCounts:
        channelCount = vgmSystemChannels.systemsChannelCounts[system]
    else:
        sys.exit("System {} not found".format(system))
    if CHANNEL_COUNT_OVERRIDE != 0:
        channelCount = CHANNEL_COUNT_OVERRIDE
    baseMask = generateBaseMask(channelCount)
    masks = generateMasks(channelCount,baseMask)
    config = loadBaseConfig(CONFIG_PATH)
    config["General"]["LogSound"] = "1"
    
    #vgmPaths
    vgmPaths = loadAllVGMs(path)
    #prepPathsToStrings(vgmPaths)
    
    for vgmPath in vgmPaths:
        currentSongName = vgmPath[:-4]#change this to scan the vgm later
        if not os.path.isdir(currentSongName):
            os.mkdir(currentSongName)
        i = 0
        for mask in masks:
            writeMuteMask(mask,config,system,CONFIG_PATH)
            subprocess.call("{} {}".format(VGM_PLAY_PATH,prepPathToString(vgmPath)))
            workingPath = os.getcwd()
            oldPath = "{}\\{}.wav".format(workingPath,currentSongName)
            newPath = "{}\\{}\\{}{}.wav".format(workingPath,currentSongName,currentSongName,i)
            shutil.move(oldPath,newPath)
            i += 1

def main():
    pass
    renderAll()

main()
