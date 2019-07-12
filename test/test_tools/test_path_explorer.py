from os.path import dirname
from unittest import TestCase

from tools import path_explorer

PATH_TO_HERE = dirname( __file__ )
PATH_TO_TEST = dirname( PATH_TO_HERE )
PATH_TO_TOOLS = dirname( PATH_TO_TEST ) + '/tools'


class TestProjectExplorerLibrary( TestCase ):
    def setUp( self ):
        pass

    def test_explorer_on_test_directory( self ):
        dirs, files = path_explorer.search_path_for_directories_and_files(
            path = PATH_TO_HERE,
            omit_python_cache = True
        )

        self.assertTrue( __file__ in files )

        cache_folders_recorded = [dir for dir in dirs if '__pycache__' in dir]

        self.assertEqual(
            len( cache_folders_recorded ),
            0,
            msg = 'omit_python_cache yielded cached folders'
        )

    def test_explorer_on_test_directory_including_cache( self ):
        dirs, files = path_explorer.search_path_for_directories_and_files(
            path = PATH_TO_HERE,
            omit_python_cache = False
        )

        cache_folders_recorded = [dir for dir in dirs if '__pycache__' in dir]

        self.assertTrue( __file__ in files )
        self.assertGreater( len( cache_folders_recorded ), 0 )

    def test_filtering_files_by_extension( self ):
        files = path_explorer.search_path_for_files_with_extensions(
            path = PATH_TO_TOOLS,
            extensions = ('py', 'xml')
        )
        self.assertGreaterEqual( len( files ), 3 )

        files = path_explorer.search_path_for_files_with_extensions(
            path = PATH_TO_HERE,
            extensions = ('py')
        )
        self.assertTrue( __file__ in files )

        files = path_explorer.search_path_for_files_with_extensions(
            path = PATH_TO_TOOLS,
            extensions = ('xml')
        )
        self.assertEqual( len( files ), 1 )

        files = path_explorer.search_path_for_files_with_extensions(
            path = PATH_TO_HERE,
            extensions = ()
        )
        self.assertEqual( len( files ), 0 )

        files = path_explorer.search_path_for_files_with_extensions(
            path = PATH_TO_HERE,
            extensions = ('com')
        )
        self.assertEqual( len( files ), 0 )

    def test_filtering_directories_by_partial_match( self ):
        dirs = path_explorer.search_path_for_directories_with_partial_match(
            path = dirname( PATH_TO_TEST ),
            partial = 'test'
        )
        self.assertGreaterEqual( len( dirs ), 1 )
        self.assertTrue( dirname( __file__ ) in dirs )

        dirs = path_explorer.search_path_for_directories_with_partial_match(
            path = dirname( PATH_TO_HERE ),
            partial = 'match me if you can'
        )
        self.assertGreaterEqual( len( dirs ), 0 )

    def tearDown( self ):
        pass
