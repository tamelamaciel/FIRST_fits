#! /usr/local/bin/python

#===============================================================================
# To repeatedly fill in the NVSS postage stamp survey webpage at
#
#       http://third.ucllnl.org/cgi-bin/firstcutout
#
#
# Parameters required:
#
#   equinox        (set to "J2000")
#   image size     (set to "4.5" arcmin)
#   image type     (set to "FITS file")
#   max intensity  (set to "10" mJy)
#
# Prompts for a text file containing lines of:
#
# source hh mm ss.ss dd mm ss.s
#
# or 
# source hh:mm:ss.ss +dd:mm:ss.s
#
# (the source's name is used for the name of the outfile file (+.fits))
#-------------------------------------------------------------------------------
# Tamela Maciel 30 June 2014
#===============================================================================
import string
import urllib

# FIRST web form address

address='http://third.ucllnl.org/cgi-bin/firstcutout'
method='POST'

# fixed parameters

Equinox='J2000'
ImageSize='4.5' #in arcmin. this is the default value from the webpage
ImageType='FITS Image'
MaxInt='10' #in mJy. this is the default value from the webpage




SourceFile='test_data.txt'

print '------------------------------------------------------'
print 'Extracting .fits files from FIRST cutout                    '
print '------------------------------------------------------'
print 'Using parameters:'
print '  equinox.....: ',Equinox
print '  image size (arcmin).....: ',ImageSize
print '  image type........: ',ImageType
print '  max intensity (mJy).......: ',MaxInt
'-----------------------------'
print '  source file : '+SourceFile
print '------------------------------------------------------'

file  = open(SourceFile, 'r')
notfound=[]
print 'File opened...'
print ''

while 1:

  line=file.readline()
  if '#' in line:
    continue
  if not line: break

  items=string.split(line)

  ObjName=items[0]
  RAlist=items[1].split(':')
  RA=RAlist[0]+' '+RAlist[1]+' '+RAlist[2]
  Declist=items[2].split(':')
  Dec=Declist[0]+' '+Declist[1]+' '+Declist[2]

  print 'ObjName is : ',ObjName
  print 'RA is......: ',RA
  print 'Dec is.....: ',Dec

  outfile=ObjName+'.fits'

  parameters = urllib.urlencode({'Equinox': Equinox, 'RA': RA, 'Dec': Dec, 'ImageSize': ImageSize, 'ImageType': ImageType, 'MaxInt': MaxInt})
  

  if method == 'POST':
    form = urllib.urlopen(address, parameters)
  elif method == 'GET':
    form = urllib.urlopen(address+'?%s' % parameters)
  else:
    print 'invalid method!'

  returned = form.read()

  if 'Field Not Found' in returned:
    notfound.append([ObjName,RA,Dec])
  f=open(outfile,'w')
  f.write(returned)
  f.close()

  print 'Source ',ObjName,' processed, output in '+ObjName+'.fits'

print ''
print '------------------------------------------------------'
print 'Done!'
print '------------------------------------------------------'
