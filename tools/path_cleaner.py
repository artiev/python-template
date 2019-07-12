import os
import click

from tools.path_explorer import search_path_for_files_with_extensions
from tools.path_explorer import search_path_for_directories_with_partial_match


@click.group()
def cli() -> None: pass


@cli.command()
@click.argument( 'path' )
def clear_cache_files( path: str ) -> None:
    cache_extensions = ('pyc', 'pyo', 'pyd')

    file_path_list = search_path_for_files_with_extensions(
        path = path,
        extensions = cache_extensions
    )

    for filepath in file_path_list:

        status = 'FAILED'
        additional = ''

        try:
            os.unlink( filepath )
            status = 'OK'
        except Exception as err:  # pylint: disable=wide-except
            additional = '--> ' + str( err )

        template = 'Deleting  `{path}`: {status} {additional}'
        click.echo(
            template.format(
                path = filepath,
                status = status,
                additional = additional
            )
        )


@cli.command()
@click.argument( 'path' )
def clear_cache_folders_if_empty( path: str ) -> None:
    folder_path_list = search_path_for_directories_with_partial_match(
        path,
        partial = '__pycache__'
    )

    for folderpath in folder_path_list:

        status = 'FAILED'
        additional = ''

        try:
            os.rmdir( folderpath )
            status = 'OK'
        except Exception as err:  # pylint: disable=wide-except
            additional = '--> ' + str( err )

        template = 'Deleting  `{path}`: {status} {additional}'
        click.echo(
            template.format(
                path = folderpath,
                status = status,
                additional = additional
            )
        )


@cli.command()
@click.argument( 'path' )
@click.pass_context
def clear_all_cache( ctx, path: str ) -> None:
    ctx.forward( clear_cache_files )
    ctx.forward( clear_cache_folders_if_empty )


if __name__ == '__main__':
    cli()
