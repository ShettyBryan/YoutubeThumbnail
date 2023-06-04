import click
import PIL
from PIL import Image


@click.command(options_metavar='-i <image-path> -o <output-directory> -f <filename>')
@click.option(
    '-i', '--image-path', 'srcImageFile',
    required=True,
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    help='Path to the source image file'
    )
@click.option(
    '-o', '--output-directory', 'destinationDirectory',
    required=True,
    type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True),
    help='Path to the output directory'
    )
@click.option(
    '-f', '--filename', 'filename',
    required=True,
    help='Filename of the thumbnail image'
    )
def main(srcImageFile, destinationDirectory, filename):
    """
    Creates a Ready-For-Youtube Thumbnail image from the source image file and
    saves it to the output directory as a PNG file.
    """
    WIDTH_PIXELS = 1280
    HEIGHT_PIXELS = 720
    SIZE = (WIDTH_PIXELS, HEIGHT_PIXELS)

    try:
        with Image.open(srcImageFile) as image:
            image.thumbnail(SIZE, resample=3)
            image.save(f"{destinationDirectory}/{filename}.png", "PNG")
    except FileNotFoundError:
        click.secho("Error: If the file cannot be found.", fg='red')
    except PIL.UnidentifiedImageError:
        click.secho("Error: Image cannot be opened or identified.", fg='red')
    except ValueError:
        click.secho("Error: the mode is not 'r', or a StringIO instance is used for fp", fg='red')
    except TypeError:
        click.secho("Error: Formats is not None, a list or a tuple ", fg='red')


if __name__ == '__main__':
    main()
