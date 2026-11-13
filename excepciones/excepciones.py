from mi_excepcion import MyException as Me

def sumar_dos():
    a = input("N1: ")
    b = input("N2: ")
    try:
        resultado = int(a) + int(b)
    except Exception as e:
        print(f"Error: {type(e).__name__} -> {e}")
    else:
        print("se ejecuta")
    finally:
        print("Siempre")

    return resultado

print(sumar_dos())