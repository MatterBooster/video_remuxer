# FFMPEG Video Remuxer
Uses FFMPEG to remux files with your whished audio and video codecs.

With this you can switch the extension of your video files and you can also use different cideo codecs currently build in are: h.264, HEVC (h.265) and AV1. 

### Attention: The build-in video player of windows does not support HEVC and wants you to buy an 0.99€/$ extension. But you can use the command:
```powershell
ffplay path\to\your\file
```
To play it with FFMPEG or you can also download other video player like VLC (https://www.videolan.org/vlc/)

# Installation prerequisites:
- ffmpeg (https://www.python.org/downloads/)
- python (https://ffmpeg.org/download.html)

### For installing ffmpeg: (https://github.com/ScoopInstaller/Scoop)
Open your PowerShell and put in 
```powershell
iwr -useb get.scoop.sh | iex
```
This will instill Scoop (https://scoop.sh/), which is a command-line installer for Windows.

Then you have to type:
```powershell
scoop install ffmpeg
```
in your PowerShell or Commandpromp (cmd). This will then install FFMPEG.
