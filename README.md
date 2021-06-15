# AudioFiletrimmer
- This code allows us to trim the edges of an audio file (.wav or .mp3) using python without downloading complex software on your device.
- The code includes a user-friendly command line interface for configuring the start and end time and for converting an mp3 file to a wav file and vice versa. 
## Dependancies
* Ensure that ffmpeg is properly installed and added to path.
  * Refer to : https://www.wikihow.com/Install-FFmpeg-on-Windows
* Install packages: 
  * **pip install pydub**
  *  **pip install argparse**

## Command Line Interface Arguments:
* -s/--start: The start time. hh:mm:ss Eg: 00:00:23
* -e/--end: The end time.hh:mm:ss Eg: 00:00:23
* -p/--path: Path to the full song. Eg: C:\Users\Priyanka\Desktop\songs\\<name_of_song>.mp3
    **All arguments are required**
## Sample CLI usage:
Ensure that the following command is executed in the terminal from the location where the python script Trim_edges.py is stored:
**python Trim_Edges.py 
-p C:\Users\Priyanka\Desktop\songs\\<name_of_song>.mp3 
-s 00:00:20 
-e 00:04:50**

## Edge cases taken care of:
* start time should be less than end time.
* end time should be less than song duration.
* audio file path should be correct.
* audio file extention should be either *.mp3* or *.wav* only. 

## What I learned:
* How to use the argparse library to create a simple command line interface with custom validation functions for the input arguments.
* How to raise exceptions in python.
* How to use the audioSegment subpackage from pydub package to create an audio filter based on time. 
