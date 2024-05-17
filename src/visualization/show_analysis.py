# -*- coding: utf-8 -*-
from pathlib import Path

import click
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath):
    """ Runs data analysis scripts to turn features data from (saved in ../processed)
    into meaningful data ready to be shown.
    """
    pass


if __name__ == '__main__':
    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
