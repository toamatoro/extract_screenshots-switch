import os 
import shutil

#input should be encoded
def extract(directory, dest):

	os.chdir(directory)

	count = 0

	size = len(os.listdir(directory))

	for obj in os.listdir(directory):

		name = os.fsdecode(obj);

		if ( ('.jpg' in name) or ('.mp4' in name) ):
			shutil.copy(name, dest)
		else:
			extract(os.getcwd() + '/' + name, dest)

		count = count + 1

		if (count == size):
			os.chdir('..')
			return



#########################################################################


#get name of flash drive
#could assume only volume
dest = os.getcwd() + '/nin_photos'

os.chdir('/Volumes')

directory = os.fsencode( os.getcwd() )


#find micro sd card(assumes no other volumes)
# 	and navigate to nintendo album
for file in os.listdir( directory ):

	filename = os.fsdecode(file)

	if( (filename != 'Macintosh HD') and (filename != 'BOOTCAMP') ):
		os.chdir(filename)
		break

os.chdir( 'Nintendo/Album' )

directory = os.fsencode( os.getcwd() )


extract(directory, dest)


print( 'done' )

