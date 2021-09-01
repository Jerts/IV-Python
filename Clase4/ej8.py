mensaje  = input('Ingresa el texto que quieras guardar por favor')
nombreArchivo = 'mensaje.txt'
new_file = open(nombreArchivo,'w')
new_file.write(mensaje)
new_file.close()

new_file = open(nombreArchivo,'r')
mensaje1=new_file.readline()
new_file.close()
print(f'El mensaje en el archivo: {nombreArchivo} es ->')
print(mensaje1)