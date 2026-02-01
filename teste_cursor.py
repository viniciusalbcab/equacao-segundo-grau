"""
Resolve equação do segundo grau: ax² + bx + c = 0
A partir dos coeficientes a, b e c informados pelo usuário.
"""

import cmath


def resolve_equacao_segundo_grau(a: float, b: float, c: float) -> None:
    """
    Resolve ax² + bx + c = 0 e exibe delta, tipo de raízes e valores.
    """
    if a == 0:
        print("O coeficiente 'a' não pode ser zero em uma equação do segundo grau.")
        return

    delta = b**2 - 4 * a * c

    print(f"\n--- Equação: {a}x² + {b}x + {c} = 0 ---")
    print(f"Delta (Δ) = {delta}")

    if delta > 0:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        print("Duas raízes reais diferentes.")
        print(f"x₁ = {x1}")
        print(f"x₂ = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print("Duas raízes reais iguais (raiz dupla).")
        print(f"x₁ = x₂ = {x}")
    else:
        # Raízes complexas conjugadas
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        print("Duas raízes complexas conjugadas.")
        print(f"x₁ = {x1}")
        print(f"x₂ = {x2}")


def main():
    print("Resolução da equação do segundo grau: ax² + bx + c = 0")
    print("Informe os coeficientes:\n")

    try:
        a = float(input("Coeficiente a: "))
        b = float(input("Coeficiente b: "))
        c = float(input("Coeficiente c: "))
    except ValueError:
        print("Erro: digite apenas números.")
        return

    resolve_equacao_segundo_grau(a, b, c)


if __name__ == "__main__":
    main()
