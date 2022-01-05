# vgmPlaySplitPy
Python script for splitting .vgm/.vgz renders in vgmPlay. 

Script currently needs to manually told what vgm to render

Written for VGMPlay 0.51.0 **channel masking might not work if you use an earlier version*** depending on the system you are using.

# Issues
- Does not work properly for multiChip .vgms (YM2151+PCM etc.)
- auto vgm/vgz detetction removed afer re-write

# usage
- Download [vgmPlay](https://github.com/vgmrips/vgmplay) and all files into a directory.
- run vgmSplit.py in same directory.

## options
- Ensure that `VGM_PLAY_PATH` matches the vgmplay executable
- Ensure that `CONFIG_PATH` matches the vgmplay ini
- Change `G_SYSTEMG_SYSTEM` to match the system your are targeting in VGMPlay.ini. Currentl supported systems can be found in `systemChannels.py`
- Change `G_VGM_PATH` to the path your .vgm is locaeed
