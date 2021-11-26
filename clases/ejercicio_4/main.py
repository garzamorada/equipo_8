from sistema import Sistema
main = Sistema()

main.createUsuario("juancarlos@gmail.com", "Mansilla", "Juan",  "password", "cliente",main)
main.createUsuario("ppicapiedras@gmail.com", "Picapiedras", "Pedro",  "password", "cliente",main)
main.createUsuario("pablomarmol@gmail.com", "Marmol", "Pablo",  "password", "cliente",main)
main.createUsuario("fmoreno@gmail.com", "Moreno", "Francisco P",  "password", "cliente",main)
main.createUsuario("garzamorada@gmail.com", "Allievi", "Andres",  "admin123", "admin",main)
main.createUsuario("reporter@gmail.com", "Kent", "Clark",  "reporter123", "reporter",main)
main.listarUsuarios()
main.listarUsuarios("admin")
main.listarUsuarios("reporter")

main.createProducto("00001","Papél Higiénico",104,10)
main.createProducto("00002","Papél de Lija",25,100)
main.createProducto("00003","Papél de Regalo",20,5)
main.createProducto("00004","Resma de papél",205,99)

#tester = main.listaUsuarios[0]
#tester.menuOpciones(main)
print(' ')
print('-'.center(84,'-'))
email = input('ingrese su email: ')
password = input('ingrese su password: ')
print('-'.center(84,'-'))
print(' ')
usuarioActual=main.retornaUsuario(email,password)
usuarioActual.print()
if usuarioActual.level == 'cliente':
    usuarioActual.menuOpciones()
elif usuarioActual.level == 'admin':
    usuarioActual.menuAdmin()
elif usuarioActual.level == 'reporter':
    usuarioActual.menuReporter()
    
