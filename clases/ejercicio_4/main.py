from sistema import Sistema
from menu import Menu
main = Sistema()
menu= Menu(main)

main.createUsuario("juancarlos@gmail.com", "Mansilla", "Juan",  "password", "cliente")
main.createUsuario("ppicapiedras@gmail.com", "Picapiedras", "Pedro",  "password", "cliente")
main.createUsuario("pablomarmol@gmail.com", "Marmol", "Pablo",  "password", "cliente")
main.createUsuario("fmoreno@gmail.com", "Moreno", "Francisco P",  "password", "cliente")
main.createUsuario("garzamorada@gmail.com", "Allievi", "Andres",  "admin123", "admin")
main.createUsuario("reporter@gmail.com", "Kent", "Clark",  "reporter123", "reporter")
main.listarUsuarios()
main.listarUsuarios("admin")
main.listarUsuarios("reporter")

main.createProducto("00001","Papél Higiénico",104,10)
main.createProducto("00002","Papél de Lija",25,100)
main.createProducto("00003","Papél de Regalo",20,5)
main.createProducto("00004","Resma de papél",205,99)

menu.muestraMenu()
    
