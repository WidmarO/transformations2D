# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from utils import *

def menu():
	print("************* MENU OPERACIONES GRAFICAS *************")
	print("* 1. Traslacion                                     *")
	print("* 2. Rotacion                                       *")
	print("* 3. Escalamiento                                   *")
	print("* 4. Reflexion                                      *")
	print("* 5. Deformacion                                    *")
	print("* 6. Agregar poligono                               *")
	print("* 7. Limpiar display                                *")
	print("* 8. Salir                                          *")
	print("*****************************************************")

def pmedio(vertices_p1):
	xp = 0
	yp = 0
	for x in range(len(vertices_p1)):
		xp += vertices_p1[x][0]
		yp += vertices_p1[x][1]
	print("punto medio: ",xp/len(vertices_p1),yp/len(vertices_p1))

def main():
	scale = 3
	width, height = scale * 200, scale * 200
	pygame.init()
	pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)

	reiniciar = 1
	while(reiniciar == 1):

		# Dibujando eje X y su label
		DDA(-300,0,300,0, 0/255, 0/255, 255/255, scale)
		DDA(-300,5,-290,15, 0/255, 100/255, 100/255, scale)
		DDA(-300,15,-290,5, 0/255, 100/255, 100/255, scale)
		# Dibujando eje Y y su label
		DDA(0,-300,0,300, 0/255, 0/255, 255/255, scale)
		DDA(-15,295,-9,290, 0/255, 100/255, 100/255, scale)
		DDA(-5,294,-15,285, 0/255, 100/255, 100/255, scale)
		for i in range(-300,300,10):
			DDA(i, -2, i, 2, 0/255, 0/255, 255/255, scale)
			DDA(-2, i, 2, i, 0/255, 0/255, 255/255, scale)

		opcion = -1
		nro_puntos = int(input('cuantos puntos son ?: '))
		puntos = []
		vertices_p1 = []
		print("Ingrese los puntos un punto por linea x y ejemplo: 20 30")
		for i in range(nro_puntos):
			aux = input().split()
			x , y = int(aux[0]) , int(aux [1])
			puntos.append((x,y))
			vertices_p1.append([x,y,1])

		DrawPolygon(puntos, 255/255, 0/255, 0/255, scale)
		pmedio(vertices_p1)
		while(opcion != 7):
			menu()
			opcion = int(input("Ingrese la opcion: "))
			if (opcion == 1):
				# Traslate
				print("*********** TRASLACION ***********")
				auxt = input("Ingrese x y para trasladar: ").split()
				tx = int(auxt[0])
				ty = int(auxt[1])
				vertices_p1 = Traslate(vertices_p1, tx, ty)							
				DrawPolygon_(vertices_p1, 0/255, 255/255, 0/255, scale)
				pmedio(vertices_p1)

			elif(opcion == 2):
				# Rotation
				print("************ ROTACION ************")
				angle = int(input("Ingrese cuantos grados quiere rotar: "))			
				vertices_p1 = Rotation(vertices_p1, angle)
				# print(vertices_p1)
				DrawPolygon_(vertices_p1, 0/255, 255/255, 0/255, scale)
				pmedio(vertices_p1)

			elif(opcion == 3):
				# scale
				print("********** ESCALAMIENTO **********")					
				auxt = input("Ingrese x y para escalar: ").split()
				tx = int(auxt[0])
				ty = int(auxt[1])
				vertices_p1 = Escalamiento(vertices_p1,tx,ty)
				DrawPolygon_(vertices_p1, 0/255, 255/255, 0/255, scale)
				pmedio(vertices_p1)

			elif(opcion == 4):
				print("*********** REFLEXION ************")
				print("1 . Reflexion en X")
				print("2 . Reflexion en Y")
				ans = int(input("Ingrese opcion: "))
				if(ans == 1):
					vertices_p1 = ReflexionEjeX(vertices_p1)
				elif(ans == 2):
					vertices_p1 = ReflexionEjeY(vertices_p1)
				DrawPolygon_(vertices_p1, 0/255, 255/255, 0/255, scale)
				pmedio(vertices_p1)

			elif(opcion == 5):
				print("*********** DEFORMACION **********")
				auxt = input("Ingrese x y para la deformacion: ").split()
				tx = int(auxt[0])
				ty = int(auxt[1])
				vertices_p1 = Deformation(vertices_p1,tx,ty)
				DrawPolygon_(vertices_p1, 0/255, 255/255, 0/255, scale)			
				pmedio(vertices_p1)

			elif(opcion == 6 ):
				print("******** Agregar poligono ********")
				opcion = -1
				nro_puntos = int(input('cuantos puntos son ?: '))
				puntos = []
				print("Ingrese los puntos un punto por linea x y ejemplo: 20 30")
				for i in range(nro_puntos):
					aux = input().split()
					x , y = int(aux[0]) , int(aux [1])
					puntos.append((x,y))
					vertices_p1.append([x,y,1])
				DrawPolygon(puntos, 255/255, 0/255, 0/255, scale)
				pmedio(vertices_p1)
				
			elif(opcion == 7):
				print("******** Limpiar display ********")
				print(" Display limpio puede ingresar nuevos valores ...")
				
			elif(opcion == 8):
				reiniciar = 0
				opcion = 7
			# opcion = int(input("ingrese opcion"))
		
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glFlush()		
		# pygame.display.flip()


	print("Gracias por usar este programa ... :') ")
	print("Finish...")

	 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

if __name__ == '__main__':
	main()