# -*- coding: utf-8 -*-
"""PolarImaginario.ipynb


Original file is located at
    https://colab.research.google.com/drive/1FI8x_wq4RSqMXEdA0xgqgNLb7oIIh_Pc
"""

import cmath
import math

def complex_to_polar(complex_num_str):
    """Converte número complexo para coordenadas polares (magnitude e graus)."""
    try:
        complex_num = complex(complex_num_str)
        magnitude = abs(complex_num)
        phase_rad = cmath.phase(complex_num)
        phase_deg = math.degrees(phase_rad)
        return magnitude, phase_deg
    except ValueError:
        return "Erro: Número complexo inválido."

def polar_to_complex(magnitude, angle_deg):
    """Converte coordenadas polares para número complexo."""
    try:
        angle_rad = math.radians(float(angle_deg))
        real = magnitude * math.cos(angle_rad)
        imag = magnitude * math.sin(angle_rad)
        return complex(real, imag)
    except ValueError:
        return "Erro: Valores polares inválidos."

def main():
    while True:
        print("\n** Conversor de Coordenadas **")
        print("1. Complexo → Polar")
        print("2. Polar → Complexo")
        print("3. Sair")

        choice = input("Escolha uma opção (1/2/3): ")

        if choice == '1':
            complex_str = input("Digite o número complexo (ex: 3+4j): ")
            result = complex_to_polar(complex_str)

            if isinstance(result, tuple):
                mag, phase = result
                print(f"\nMagnitude: {mag:.2f}")
                print(f"Ângulo: {phase:.2f}°\n")
            else:
                print(result)

        elif choice == '2':
            try:
                mag = float(input("Magnitude: "))
                angle = float(input("Ângulo (graus): "))
                result = polar_to_complex(mag, angle)
                print(f"\nNúmero complexo: {result:.2f}\n")
            except ValueError:
                print("Erro: Insira valores numéricos válidos.")

        elif choice == '3':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
