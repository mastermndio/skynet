import click
import platform

@click.group()
def cli():
    """ Welcome to Skynet """

@cli.command()
@click.option('--temp', type=int, help='The temperature you want to convert')
@click.option('--units', help='The units of your temperatur and what you want it converted to')
def convert(temp, units):
    if units == 'f2c':
        new_temp = (temp - 32) * 5/9
        print(f'{temp} degreed F is equal to {new_temp} degrees C')

