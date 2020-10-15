# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
import random as rdn
import numpy as np

### Algorithm ###

def set_pixel(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
	
	# pygame.display.flip()
	glFlush()

	# print("{}\t{}".format(x, y))
	# print(x,y)
	# pygame.time.wait(1)

def color_pixel(width, height, x, y, size):
	rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size , 
						GL_RGB, GL_UNSIGNED_BYTE, None)
	return list(rgb)

def DDA(x0, y0, x1, y1, r, g, b, size):
	points = []
	dx = x1 - x0
	dy = y1 - y0

	x = x0
	y = y0

	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)

	xi = dx / steps
	yi = dy / steps

	set_pixel(round(x), round(y), r, g, b, size)
	points.append((round(x), round(y)))
	for k in range(int(steps)):
		x += xi
		y += yi
		set_pixel(round(x), round(y), r, g, b, size)
		points.append((round(x), round(y)))
	return points

def DrawPolygon(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(len(vertices) - 1):
		x0, y0 = vertices[k]
		x1, y1 = vertices[k + 1]
		DDA(x0, y0, x1, y1, r, g, b, size)

def DrawPolygon_(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(len(vertices) - 1):
		# print(vertices[k])
		x0, y0 = vertices[k][:2]
		x1, y1 = vertices[k + 1][:2]
		DDA(x0, y0, x1, y1, r, g, b, size)
	vertices.pop()

def Traslate(vertices, tx, ty):
	T = [
		[1, 0, tx], 
		[0, 1, ty], 
		[0, 0, 1]
	]
	print("----- matriz de transformacion")
	for i in T:
		print(i)
	print("------------------------------")
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	print("---- los nuevos puntos en vectores")
	for i in result:
		print(i)
	print("------------------------------")	
	return result

def Rotation(vertices, angle):
	angle = math.radians(angle)
	T = [
		[math.cos(angle), -math.sin(angle), 0],
		[math.sin(angle), math.cos(angle), 0],
		[0, 0, 1]
	]
	print("----- matriz de transformacion")
	for i in T:
		print(i)
	print("------------------------------")
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	print("---- los nuevos puntos en vectores")
	for i in result:
		print(i)
	print("------------------------------")	
	return result

def Escalamiento(vertices, tx, ty):
	
	T = [
		[tx,0,0],
		[0,ty,0],
		[0, 0,1]
	]
	print("----- matriz de transformacion")
	for i in T:
		print(i)
	print("------------------------------")
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	print("---- los nuevos puntos en vectores")
	for i in result:
		print(i)
	print("------------------------------")	
	return result

def ReflexionEjeX(vertices):
	T = [
		[1, 0, 0], 
		[0, -1, 0], 
		[0, 0, 1]
	]
	print("----- matriz de transformacion")
	for i in T:
		print(i)
	print("------------------------------")
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	print("---- los nuevos puntos en vectores")
	for i in result:
		print(i)
	print("------------------------------")		
	return result

def ReflexionEjeY(vertices):
	T = [
		[-1, 0, 0], 
		[0,1, 0], 
		[0, 0, 1]
	  ]
	print("----- matriz de transformacion")
	for i in T:
		print(i)
	print("------------------------------")
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	print("---- los nuevos puntos en vectores")
	for i in result:
		print(i)
	print("------------------------------")	
	return result

def Deformation(vertices,shx,shy):
	T = [
		[1, shx ,0], 
		[shy, 1,0],
    [0,0,1]
	  ]
	print("----- matriz de transformacion")
	for i in T:
		print(i)
	print("------------------------------")
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	print("---- los nuevos puntos en vectores")
	for i in result:
		print(i)
	print("------------------------------")	
	return result
  
def floatRgb(mag, cmin, cmax):
    """ Return a tuple of floats between 0 and 1 for R, G, and B. """
    # Normalize to 0-1
    try: x = float(mag-cmin)/(cmax-cmin)
    except ZeroDivisionError: x = 0.5 # cmax == cmin
    blue  = min((max((4*(0.75-x), 0.)), 1.))
    red   = min((max((4*(x-0.25), 0.)), 1.))
    green = min((max((4*math.fabs(x-0.5)-1., 0.)), 1.))
    return red, green, blue

### Draw
def display_openGL(width, height, scale):
	pygame.display.set_mode((width, height), pygame.OPENGL)

	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glScalef(scale, scale, 0)

	gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)