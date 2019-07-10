"""
The cleanup script looks for python's temporary files
(object, pre-compiled, etc...) and empties the cache.
"""

# pylint:disable=invalid-name, broad-except

import os
import argparse

path = './'
filters = ['__pycache__', '.pyc', '.pyo']

parser = argparse.ArgumentParser( description = 'Clean up the project\'s cache' )
parser.add_argument( '-m', '--mockup', metavar = 'mockup',
                     type = bool,
                     nargs = '?',
                     required = False,
                     default = False,
                     help = 'Does a test run.' )

args = parser.parse_args()

cachefiles = list()
cachedirs = list()

print( 'Scanning project for cache files.' )

for path, dirs, files in os.walk( path ):
    folder = os.path.basename( path )
    if folder in filters:
        cachedirs.append( path )

    for file in files:
        filepath = path + '/' + file
        filepath.replace( '//', '/' )
        for flt in filters:
            if filepath.endswith( flt ):
                cachefiles.append( filepath )

print( 'Found {} files and folders.'.format( len( cachefiles ) + len( cachedirs ) ) )

for item in cachefiles:
    print( 'Removing file {}'.format( item ) )

    if args.mockup is False:
        try:
            os.remove( item )
        except Exception as e:
            print( 'Failed to remove {}'.format( item ) )
            print( 'Halted.' )
            exit( 1 )

for item in cachedirs:
    print( 'Removing folder {}'.format( item ) )

    if args.mockup is False:
        try:
            os.removedirs( item )
        except Exception as e:
            print( 'Failed to remove {}'.format( item ) )
            print( 'Halted.' )
            exit( 1 )

print( 'Success.' )
exit( 0 )
