"""
CLI para la resolución de problemas propuestos en data academy
"""

import logging
import math
import random

import colorama
import coloredlogs
import click
from colorama import Fore


colorama.init()
logger = logging.getLogger(__name__)


#############################################################################
# Funciones de utilidades
#############################################################################
def ingrese_numero(titulo='el valor', tipo=int):
    print(Fore.GREEN + f'Ingrese {titulo}')
    while True:
        try:
            value = tipo(input(Fore.GREEN + ">> "))
            break
        except ValueError:
            print(Fore.RED + 'Ingrese un número')

    return value


def cilindro():
    pass


def tetraedro():
    pass


def cubo():
    pass


def ortoedro():
    pass




#############################################################################
# CLI
#############################################################################
@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    debug_on = 'INFO' if debug is False else True
    coloredlogs.install(level=debug_on)
    click.echo(f"Modo debug esta en {'on' if debug else 'off'}")


@cli.command()
@click.option(
    '--tipo-calculo',
    type=click.Choice(['base_altura', 'lados'], case_sensitive=False),
    default='base_altura',
    help="'base_altura' cuando se tiene base y altura y 'lados' "
    "teniendo solo los lados"
)
def triangulo(tipo_calculo):
    logger.debug('En Triangulo')
    logger.info(tipo_calculo)
    triangulos = {
        1: 'equilatero',
        2: 'isósceles',
        3: 'escaleno',
        4: 'no se puede terminar'
    }

    if tipo_calculo == 'base_altura':
        base = ingrese_numero('la base')
        altura = ingrese_numero('la altura')

        area = (base * altura) / 2
        tria_tipo = 4
    elif tipo_calculo == 'lados':
        while True:
            lado_1 = ingrese_numero('el lado 1')
            lado_2 = ingrese_numero('el lado 2')
            lado_3 = ingrese_numero('el lado 3')

            # Validación del triangulo
            es_valido = all([
                (lado_1 + lado_2) > lado_3, (lado_1 + lado_3) > lado_2,
                (lado_2 + lado_3) > lado_1
            ])

            if es_valido is True:
                semi = (lado_1 + lado_2 + lado_3) / 2
                tria_tipo = len(set([lado_1, lado_2, lado_3]))
                area = math.sqrt(
                    semi * (semi - lado_1) * (semi - lado_2) * (semi - lado_3)
                )
                break
            else:
                print(
                    Fore.RED + 'Los valores de los lados no crean un triangulo'
                )
    else:
        raise Exception('Error with option tipo_calculo')

    print(Fore.CYAN + f"El área total es: {area}")
    print(Fore.CYAN + f"El tipo de triangulo es '{triangulos[tria_tipo]}'")


@cli.command()
@click.option(
    '--tipo-juego',
    type=click.Choice(['1X1', '3o2'], case_sensitive=False),
    default='1X1',
    help="'1x1' un reto nadamas, '3o2' se juegan 3 veces quien gane 2 gana "
    "la partida"
)
def piedra_papel_tijera(tipo_juego):
    logging.debug('En piedra_papel_tijera')
    juego_opts = {
        'piedra': {
            'papel': False,
            'tijeras': True,
            'piedra': None
        },
        'papel': {
            'piedra': True,
            'tijeras': False,
            'papel': None
        },
        'tijeras': {
            'piedra': False,
            'papel': True,
            'tijeras': None
        }
    }
    opciones = ('piedra', 'papel', 'tijeras')
    repeaters = 1 if tipo_juego == '1X1' else 3
    tiradas = []
    jugadas = []
    for i in range(repeaters):
        while True:
            opcion = input(
                Fore.GREEN + "ingrese su opción [piedra, papel, tijeras]>> "
            ).lower()

            if opcion in opciones:
                player_2 = random.choice(opciones)
                gana = juego_opts[opcion][player_2]

                if gana is None:
                    print(Fore.YELLOW + 'Empate, tira de nuevo')
                    continue

                tiradas.append(gana)
                jugadas.append([opcion, player_2])
                break
            else:
                print(
                    Fore.RED +
                    'Error, por favor ingrese una de las opciones'
                    ' [piedra, papel, tijeras]'
                )

    if tipo_juego == '1X1':
        gano = 'player 1' if tiradas[0] is True else 'player 2'
    else:
        gana_total = len([t for t in tiradas if t is True])
        gano = 'player 1' if gana_total > 1 else 'player 2'

    print(Fore.CYAN + f'gano el player: {gano}')
    print(Fore.CYAN + 'las jugadas fueron')
    print(Fore.CYAN + 'player 1, player 2')

    for i in jugadas:
        print(Fore.CYAN + str(i))


@cli.command()
@click.option(
    '--tipo-conversion',
    type=click.Choice(['KM2Mi', 'Mi2KM'], case_sensitive=False),
    default='KM2Mi'
)
def conversor(tipo_conversion):
    logging.debug('En conversor')
    titulo = 'los kilometros' if tipo_conversion == 'KM2Mi' else 'las millas'
    convertido = 'las millas' if tipo_conversion == 'KM2Mi' \
        else 'los kilometros'
    valor = ingrese_numero(titulo, float)

    total = valor * 1.609344 if tipo_conversion == 'Mi2KM' else valor * .621371
    print(
        Fore.CYAN + f'el valor de {titulo}: {valor} a {convertido}'
        f' es: {total:.6f}'
    )


@cli.command()
def volumenes():
    logging.debug('En calculadora de volumenes')
    print(Fore.BLUE + "Eliga que figura desea calcular")
    print(Fore.BLUE + "1. Cilindro")
    print(Fore.BLUE + "2. Tetraedro")
    print(Fore.BLUE + "3. Cubo")
    print(Fore.BLUE + "4. Ortoedro")
    opcion = ingrese_numero('la opcion')


@cli.command()
def rangos():
    logging.debug('En rangos de numeros')
    while True:
        inferior = ingrese_numero('el limite inferior')
        superior = ingrese_numero('el limite superior')

        if inferior >= superior:
            print(
                Fore.RED + 'Los limites inferior y superior son iguales '
                'o el inferior supera al inferior'
            )
            continue
        else:
            break

    while True:
        comparacion = ingrese_numero('el numero a comparar')

        if inferior <= comparacion <= superior:
            print(
                Fore.CYAN +
                f'El número {comparacion} esta dentro de'
                f' [{inferior}, {superior}]'
            )
            break
        elif comparacion < inferior:
            print(
                Fore.RED +
                f'El número {comparacion} es menor que el '
                f'límite inferior: {inferior}'
            )
        elif comparacion > superior:
            print(
                Fore.RED +
                f'El número {comparacion} es mayor que el '
                f'límite superior: {superior}'
            )


if __name__ == '__main__':
    cli()

