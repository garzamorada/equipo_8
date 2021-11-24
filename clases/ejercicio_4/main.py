from emuladorDB import emuladorDB
DB = emuladorDB()

DB.createUsuario("juancarlos@gmail.com", "Mansilla", "Juan",  "password", "cliente")
DB.createUsuario("ppicapiedras@gmail.com", "Picapiedras", "Pedro",  "password", "cliente")
DB.createUsuario("pablomarmol@gmail.com", "Marmol", "Pablo",  "password", "cliente")
DB.createUsuario("fmoreno@gmail.com", "Moreno", "Francisco P",  "password", "cliente")
DB.createUsuario("garzamorada@gmail.com", "Allievi", "Andres",  "admin123", "admin")
DB.createUsuario("reporter@gmail.com", "Kent", "Clark",  "reporter123", "reporter")
DB.listarUsuarios()
DB.listarUsuarios("admin")
DB.listarUsuarios("reporter")

DB.createProducto("00001","Papél Higiénico",104,10)
DB.createProducto("00002","Papél de Lija",25,100)
DB.createProducto("00003","Papél de Regalo",20,5)
DB.createProducto("00004","Resma de papél",205,99)

#tester = DB.listaUsuarios[0]
#tester.menuOpciones(DB)
print(' ')
print('-----------------------------------------')
email = input('ingrese su email: ')
password = input('ingrese su password: ')
print('-----------------------------------------')
print(' ')
usuarioActual=DB.retornaUsuario(email,password)
usuarioActual.print()
if usuarioActual.level == 'cliente':
    usuarioActual.menuOpciones(DB)
elif usuarioActual.level == 'admin':
    usuarioActual.menuAdmin(DB.listaUsuarios)
elif usuarioActual.level == 'reporter':
    usuarioActual.menuReporter(DB.listaUsuarios)
    
