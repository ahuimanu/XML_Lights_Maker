import sys
import click
from lxml import etree

# lxml guidance: https://www.python101.pythonlibrary.org/chapter31_lxml.html

@click.command()
@click.argument('infile')
@click.argument('outfile')
def main(infile, outfile):
    click.echo(f'checking {infile}')

    with open(infile) as ifile:
        xml = ifile.read()

    # KML file
    infile = ''

    # P3D XML Placement File
    outfile = ''

if __name__ == '__main__':
    main()