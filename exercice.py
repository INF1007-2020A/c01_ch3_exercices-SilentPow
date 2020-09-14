#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    moyenne = 0
    valeurs = [a,b,c]

    for i in range(len(valeurs)):
        moyenne += valeurs[i]
    moyenne / len(valeurs)

    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    valeurExacte = angle_degs + angle_mins / 60 + angle_secs / 3600
    
    return valeurExacte * math.pi / 180


def to_degrees(angle_rads: float) -> tuple:
    valeurExacte = angle_rads * 180 / math.pi
    angle_degrees = math.trunc(valeurExacte)
    minutes = math.trunc(valeurExacte - and)

    return 0.0, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    return 0.0


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
