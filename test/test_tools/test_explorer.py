import os
from unittest import TestCase

from tools import explorer

PATH_TO_HERE = os.path.dirname( __file__ )
PATH_TO_TOOLS = os.path.dirname( PATH_TO_HERE ) + '/tools'


class TestProjectExplorerLibrary( TestCase ):
    def setUp( self ):
        pass

    def test_explorer_on_test_directory( self ):
        dirs, files = explorer.search_path_for_directories_and_files(
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
        dirs, files = explorer.search_path_for_directories_and_files(
            path = PATH_TO_HERE,
            omit_python_cache = False
        )

        cache_folders_recorded = [dir for dir in dirs if '__pycache__' in dir]

        self.assertTrue( __file__ in files )
        self.assertGreater( len( cache_folders_recorded ), 0 )

    def test_filtering_files_by_extension( self ):
        files = explorer.search_path_for_files_with_extensions(
            path = PATH_TO_TOOLS,
            extensions = ('py', 'xml')
        )
        self.assertGreaterEqual( len( files ), 3 )

        files = explorer.search_path_for_files_with_extensions(
            path = PATH_TO_HERE,
            extensions = ('py')
        )
        self.assertTrue( __file__ in files )

        files = explorer.search_path_for_files_with_extensions(
            path = PATH_TO_TOOLS,
            extensions = ('xml')
        )
        self.assertEqual( len( files ), 1 )

        files = explorer.search_path_for_files_with_extensions(
            path = PATH_TO_HERE,
            extensions = ()
        )
        self.assertEqual( len( files ), 0 )

        files = explorer.search_path_for_files_with_extensions(
            path = PATH_TO_HERE,
            extensions = ('com')
        )
        self.assertEqual( len( files ), 0 )

    def test_filtering_directories_by_partial_match( self ):
        dirs = explorer.search_path_for_directories_with_partial_match(
            path = os.path.dirname( PATH_TO_HERE ),
            partial = 'test'
        )
        self.assertGreaterEqual( len( dirs ), 1 )
        self.assertTrue( os.path.dirname( __file__ ) in dirs )

        dirs = explorer.search_path_for_directories_with_partial_match(
            path = os.path.dirname( PATH_TO_HERE ),
            partial = 'match me if you can'
        )
        self.assertGreaterEqual( len( dirs ), 0 )

    def tearDown( self ):
        pass
