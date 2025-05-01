agenda = {}

def menu():
    while True:
        print("\n1.Agregar 2.Listar 3.Buscar 4.Actualizar 5.Eliminar 6.Salir")
        op = input("Opción: ")
        if op == "1":
            n = input("Nombre: ")
            if n in agenda: print("Ya existe."); continue
            t, e = input("Teléfono: "), input("Email: ")
            agenda[n] = {'tel': t, 'email': e}
        elif op == "2":
            [print(f"{n} | {d['tel']} | {d['email']}") for n, d in agenda.items()]
        elif op == "3":
            n = input("Nombre: ")
            print(f"{n} | {agenda[n]['tel']} | {agenda[n]['email']}" if n in agenda else "No encontrado.")
        elif op == "4":
            n = input("Nombre: ")
            if n in agenda:
                t = input("Nuevo teléfono (enter = igual): ")
                e = input("Nuevo email (enter = igual): ")
                if t: agenda[n]['tel'] = t
                if e: agenda[n]['email'] = e
            else: print("No encontrado.")
        elif op == "5":
            n = input("Nombre: ")
            print("Eliminado." if agenda.pop(n, None) else "No encontrado.")
        elif op == "6":
            break
        else:
            print("Opción inválida.")

menu()
