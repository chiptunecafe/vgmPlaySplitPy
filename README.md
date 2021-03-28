# vgmPlaySplitPy
Python script for splitting .vgm/.vgz renders in vgmPlay. VERY ROUGH EARLY VERSION.

Script auto detects and .vgz/.vgm files and auto renders channel separated .wav files into separate folders

**WINDOWS ONLY**
for linux you need to change the path from \ to /

# Issues
Does not work properly for multimask .vgms (YM2608,YM2603,YM2151+PCM etc.)

# usage
- Download [vgmPlay](https://github.com/vgmrips/vgmplay) and all files into a directory.
- run vgmSplit.py in same directory.

## options
- Ensure that `VGM_PLAY_PATH` matches the vgmplay executable
- Ensure that `CONFIG_PATH` matches the vgmplay executable
- Change `system` to match the system your are targeting in VGMPlay.ini or vgmSystemChannels.py
- `CHANNEL_COUNT_OVERRIDE` will force only the first `CHANNEL_COUNT_OVERRIDE` number of channels are renderd.
