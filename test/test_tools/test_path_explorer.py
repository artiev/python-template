from os.path import dirname

import pytest

from tools import path_explorer

PATH_TO_HERE = dirname( __file__ )
PATH_TO_TEST = dirname( PATH_TO_HERE )
PATH_TO_TOOLS = dirname( PATH_TO_TEST ) + '/tools'


class TestProjectExplorerLibrary():

    def test_explorer_on_test_directory( self ):
        dirs, files = path_explorer.search_path_for_directories_and_files(
            path = PATH_TO_HERE,
            omit_python_cache = True
        )

        assert (__file__ in files)

        cache_folders_recorded = [dir for dir in dirs if '__pycache__' in dir]

        assert (len( cache_folders_recorded ) == 0)

    def test_explorer_on_test_directory_including_cache( self ):
        dirs, files = path_explorer.search_path_for_directories_and_files(
            path = PATH_TO_HERE,
            omit_python_cache = False
        )

        cache_folders_recorded = [dir for dir in dirs if '__pycache__' in dir]

        assert (__file__ in files)
        assert (len( cache_folders_recorded ) > 0)

    def test_current_file_found( self ):
        files = path_explorer.search_path_for_files_with_extensions(
            path = PATH_TO_HERE,
            extensions = ('py')
        )

        assert (__file__ in files)

    @pytest.mark.parametrize( 'extensions, path, count',
                              [
                                  (('py', 'xml'), PATH_TO_TOOLS, 3),
                                  (('py'), PATH_TO_HERE, 1),
                                  (('xml'), PATH_TO_TOOLS, 1),
                                  ((), PATH_TO_HERE, 0),
                                  (('com'), PATH_TO_HERE, 0)
                              ]
                              )
    def test_filtering_files_by_extension( self,
                                           extensions: set,
                                           path: str,
                                           count: int ):
        files = path_explorer.search_path_for_files_with_extensions(
            path = path,
            extensions = extensions
        )

        assert (len( files ) >= count)

    def test_filtering_directories_by_partial_match( self ):
        dirs = path_explorer.search_path_for_directories_with_partial_match(
            path = dirname( PATH_TO_TEST ),
            partial = 'test'
        )

        assert (len( dirs ) >= 1)
        assert (dirname( __file__ ) in dirs)

        dirs = path_explorer.search_path_for_directories_with_partial_match(
            path = dirname( PATH_TO_HERE ),
            partial = 'match me if you can'
        )

        assert (len( dirs ) == 0)
