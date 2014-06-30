FIRST_fits
==========

Queries the FIRST survey image cutouts webpage for an uploaded list of RA DEC positions and returns the FIRST fits files

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
#
#
# Test data file: test_data.txt
#  contains a list of five RA DEC positions with source names 'a' - 'e'
