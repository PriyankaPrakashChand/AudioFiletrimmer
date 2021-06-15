# #import libraries
# # to install pydub library simple go to the terminal and type-> pip intall pydub
import argparse
import os
import sys
from pydub import AudioSegment  
import datetime

# # Create the command line argument parser
parser = argparse.ArgumentParser(prog='audeditor',description='Edit the Audio File')

def validate_input(input):
    try:
         datetime.datetime.strptime(input, '%H:%M:%S')
         return input
    except ValueError:
        raise ValueError("Incorrect data format, should be hh-mm-ss")


parser.add_argument('-s', '--start', metavar='start time', type=validate_input, nargs='+',
                    help='an integer for start hour', required=True,dest= 'start')
parser.add_argument('-e', '--end', metavar='end time', type=validate_input, nargs='+',
                    help='an integer for end hour',required=True, dest= 'end')
parser.add_argument('-p','--path',
                       metavar='path',
                       type=str,
                       help='full path to song',required=True)

# Execute the parse_args() method
args = parser.parse_args()
print (args)
start = args.start[0].split(':')
end= args.end[0].split(':')
audio_file_name= args.path
# Audio Trim
startHour=int(start[0])
startMin = int(start[1])
startSec=int(start[2])
endHour=int(end[0])
endMin = int(end[1])
endSec = int(end[2])


# convert Time to miliseconds
startTime = startHour*3600000+startMin*60000+startSec*1000
endTime = endHour*3600000+endMin*60000+endSec*1000

print(startTime)
print(endTime)

if endTime < startTime:
    raise Exception("end time should be more than start time")

print(audio_file_name)


#also works with wav files
song = AudioSegment.from_mp3(audio_file_name)
if (song.duration_seconds *1000)<endTime:
    raise Exception("end time should be less than song duration")



extract = song[startTime:endTime] # when both start and end edges need to be trimmed
# extract = song[startTime:] # when only start edge needs to be trimmed
# extract = song[:endTime] # when only end edge needs to be trimmed
print("extraction complete")

# Saving
audio_file_extension=audio_file_name[-3:]



extract.export(audio_file_name[:-4]+ '-extract.'+audio_file_extension, format=audio_file_extension)
print("Conversion completed")
