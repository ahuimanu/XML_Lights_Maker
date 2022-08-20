import sys
import click
from lxml import etree

# lxml guidance: https://www.python101.pythonlibrary.org/chapter31_lxml.html


@click.command()
@click.argument("infile")
@click.argument("outfile")
def main(infile, outfile):
    click.echo(f"checking {infile}")

    with open(infile) as ifile:
        xml = ifile.read()

    # develop root document node
    # https://stackoverflow.com/questions/57833080/how-to-fix-unicode-strings-with-encoding-declaration-are-not-supported
    root = etree.fromstring(bytes(xml, encoding="utf8"))

    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text

            click.echo(f"{elem.tag} => {text}")

    # KML file
    infile = ""

    # P3D XML Placement File
    outfile = ""


if __name__ == "__main__":
    main()
