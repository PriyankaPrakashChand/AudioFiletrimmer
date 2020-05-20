
# to install pydub library simple go to the terminal and type-> pip intall pydub

from pydub import AudioSegment   

files_path = r'#add your file path here- eg: C:\Users\pinkb\Desktop\songs' 
file_name = r'# add the file name here- eg: Top200'


startHour=0 
startMin = 0 
startSec=7
endHour=1 
endMin = 39 
endSec = 55

# convert Time to miliseconds
startTime = startHour*3600000+startMin*60000+startSec*1000
endTime = endHour*3600000+endMin*60000+endSec*1000


# Opening file and extracting segment
song = AudioSegment.from_mp3( files_path+"\\"+file_name+".mp3")



extract = song[startTime:endTime] # when both start and end edges need to be trimmed
# extract = song[startTime:] # when only start edge needs to be trimmed
# extract = song[:endTime] # when only end edge needs to be trimmed
print("extraction complete")

# Saving
extract.export(files_path +"\\"+ file_name+ '-extract.mp3', format="mp3")
print("Conversion completed")
