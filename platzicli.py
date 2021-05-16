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
    while True:
        print(Fore.BLUE + 'Elija una opción de como calcular')
        print(Fore.BLUE + '1. Con radio y altura')
        print(Fore.BLUE + '2. Con area y altura')
        opcion = ingrese_numero('la opción')

        if opcion in (1, 2):
            break

        print(Fore.RED + 'Opción no valida')

    while True:
        altura = ingrese_numero('la altura')

        if altura > 0:
            break

        print(Fore.RED + 'La altura es menor o igual a 0')

    if opcion == 1:
        while True:
            radio = ingrese_numero('el radio')

            if radio > 0:
                break

            print(Fore.RED + 'El radio es menor o igual a 0')

        volumen = math.pi * (radio ** 2) * altura
    elif opcion == 2:
        while True:
            area = ingrese_numero('el área')

            if area > 0:
                break

            print(Fore.RED + 'El área es menor o igual a 0')

        volumen = area * altura

    return volumen


def tetraedro():
    while True:
        arista = ingrese_numero('la arista')

        if arista > 0:
            break

        print(Fore.RED + 'El valor de la arista es menor o igual a 0')

    volumen = (math.sqrt(2) / 12) * (arista ** 3)

    return volumen


def cubo():
    while True:
        arista = ingrese_numero('la arista')

        if arista > 0:
            break

        print(Fore.RED + 'El valor de la arista es menor o igual a 0')

    volumen = arista ** 3

    return volumen


def ortoedro():
    pass
    while True:
        arista_a = ingrese_numero('la arista a')

        if arista_a > 0:
            break

        print(Fore.RED + 'El valor de la arista es menor o igual a 0')

    while True:
        arista_b = ingrese_numero('la arista b')

        if arista_b > 0:
            break

        print(Fore.RED + 'El valor de la arista es menor o igual a 0')

    while True:
        arista_c = ingrese_numero('la arista c')

        if arista_c > 0:
            break

        print(Fore.RED + 'El valor de la arista es menor o igual a 0')

    volumen = arista_a * arista_b * arista_c

    return volumen


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
        while True:
            base = ingrese_numero('la base')
            altura = ingrese_numero('la altura')

            if base < 1:
                print(Fore.RED + 'La base es 0 o menor a 0')
            elif altura < 1:
                print(Fore.RED + 'La altura es 0 o menor a 0')
            else:
                break

        area = (base * altura) / 2
        tria_tipo = 4
    elif tipo_calculo == 'lados':
        while True:
            while True:
                lado_1 = ingrese_numero('el lado 1')

                if lado_1 > 0:
                    break

                print(Fore.RED + 'El lado 1 no puede ser menor o igual a 0')

            while True:
                lado_2 = ingrese_numero('el lado 2')

                if lado_2 > 0:
                    break

                print(Fore.RED + 'El lado 2 no puede ser menor o igual a 0')

            while True:
                lado_3 = ingrese_numero('el lado 3')

                if lado_3 > 0:
                    break

                print(Fore.RED + 'El lado 3 no puede ser menor o igual a 0')

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
    opciones_volumenes = {
        1: cilindro,
        2: tetraedro,
        3: cubo,
        4: ortoedro
    }

    while True:
        logging.debug('En calculadora de volumenes')
        print(Fore.BLUE + "Eliga que figura desea calcular")
        print(Fore.BLUE + "1. Cilindro")
        print(Fore.BLUE + "2. Tetraedro")
        print(Fore.BLUE + "3. Cubo")
        print(Fore.BLUE + "4. Ortoedro")
        opcion = ingrese_numero('la opcion')

        if opcion not in range(1, 5):
            print(Fore.RED + 'Opción erronea, elija entre 1 y 4')
            continue

        volumen = opciones_volumenes[opcion]()
        nombre = opciones_volumenes[opcion].__name__

        print(Fore.CYAN + f'El volumen del {nombre} es {volumen}')
        break


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

