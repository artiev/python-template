"""
The path explorer module is designed to help locate and filter and folders
files within the directory structure. It is not restricted to the local project,
so expose/use with caution.
"""

import os


def search_path_for_directories_and_files(
        path: str, omit_python_cache: bool = True ) -> (list, list):
    """
    Creates two lists containing all found directories, and all files starting
    from a given path.
    """

    list_of_files = list()
    list_of_directories = list()

    list_of_paths_to_skip = list()

    walkthrough = os.walk( path, topdown = True, followlinks = True )
    for parent_path, _, files in walkthrough:

        is_folder_skippable = False

        for path_to_skip in list_of_paths_to_skip:
            if parent_path.startswith( path_to_skip ):
                is_folder_skippable = True

        if omit_python_cache and '__pycache__' in parent_path:
            is_folder_skippable = True

        if not is_folder_skippable:
            if os.path.basename( parent_path ).startswith( '.' ):
                list_of_paths_to_skip.append( parent_path )
            else:
                list_of_directories.append( parent_path )
                list_of_files.extend(
                    [parent_path + '/' + file for file in files] )

    return list_of_directories, list_of_files


def search_path_for_directories_with_partial_match(
        path: str, partial: str ) -> list:
    """
    Gets results from the path explorer, and does a simple string comparison
    on the complete absolute path for a partial match to the provided string.
    """

    # pylint: disable=unused-variable
    dirs, files = search_path_for_directories_and_files(
        path,
        omit_python_cache = False
    )
    dirs[:] = [dir for dir in dirs if partial in dir]

    return dirs


def search_path_for_files_with_extensions(
        path: str, extensions: set ) -> list:
    """
    Gets results for the path explorer, and filters out only the files with an
    extension matching any of the list provided.
    """

    # pylint: disable=unused-variable
    dirs, files = search_path_for_directories_and_files(
        path,
        omit_python_cache = False
    )
    files[:] = [file for file in files if file.split( '.' ).pop() in extensions]

    return files
