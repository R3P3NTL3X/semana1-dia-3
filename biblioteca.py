biblioteca = {}

print("bienvenido al menu de la biblioteca principal")
def menu():
    while True:
        print("\n1.Agregar 2.Mostrar 3.Buscar ID 4.Buscar Título 5.Actualizar 6.Eliminar 7.Salir")
        op = input("Opción: ")
        if op == "1":
            i = input("ID: ")
            if i in biblioteca: print("ID ya registrado."); continue
            t, a, y = input("Título: "), input("Autor: "), input("Año: ")
            biblioteca[i] = {'titulo': t, 'autor': a, 'anio': y}
        elif op == "2":
            [print(f"ID: {i} | Título: {d['titulo']} | Autor: {d['autor']} | Año: {d['anio']}") for i, d in biblioteca.items()]
        elif op == "3":
            i = input("ID: ")
            print(f"ID: {i} | Título: {biblioteca[i]['titulo']} | Autor: {biblioteca[i]['autor']} | Año: {biblioteca[i]['anio']}" if i in biblioteca else "No encontrado.")
        elif op == "4":
            t = input("Título: ").lower()
            e = [f"ID: {i} | Título: {d['titulo']} | Autor: {d['autor']} | Año: {d['anio']}" for i, d in biblioteca.items() if d['titulo'].lower() == t]
            print("\n".join(e) if e else "No encontrado.")
        elif op == "5":
            i = input("ID: ")
            if i in biblioteca:
                a, y = input("Nuevo autor (enter = igual): "), input("Nuevo año (enter = igual): ")
                if a: biblioteca[i]['autor'] = a
                if y: biblioteca[i]['anio'] = y
                print("Actualizado.")
            else: print("No encontrado.")
        elif op == "6":
            i = input("ID: ")
            print("Eliminado." if biblioteca.pop(i, None) else "No encontrado.")
        elif op == "7":
            break
        else:
            print("Opción inválida.")

menu()
