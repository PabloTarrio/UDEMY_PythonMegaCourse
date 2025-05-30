a = 1
b = "2"
# print (int(2.5)
print (int(2.5))
# print (a + b)
print (str(a) + b)
print (a + float(b))

# print (c)
# print (a/0)

#############
#  File "C:\Users\pablo\Documents\99999_Cursos\UDEMY_PythonMegaCourse\Section16_Fixing_Programming_Errors\144_Runtime_Errors.py", line 3
#    print (int(2.5)
#          ^
#SyntaxError: '(' was never closed
#
#El error siempre está antes del posicionador, por lo que este primer error no está en la suma, está antes: Le falta un paréntesis cerrando el print anterior.
#############
#############
# Traceback (most recent call last):
#   File "C:\Users\pablo\Documents\99999_Cursos\UDEMY_PythonMegaCourse\Section16_Fixing_Programming_Errors\144_Runtime_Errors.py", line 5, in <module>
#     print (a + b)
#            ~~^~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# No podemos imprimir la suma de un entero y un string
#############
#############
# Traceback (most recent call last):
#   File "C:\Users\pablo\Documents\99999_Cursos\UDEMY_PythonMegaCourse\Section16_Fixing_Programming_Errors\144_Runtime_Errors.py", line 9, in <module>
#     print (c)
#            ^
# NameError: name 'c' is not defined
# No existe un error de sintaxis, simplemente la varriable c no existe.
#############
#############
# Traceback (most recent call last):
#   File "C:\Users\pablo\Documents\99999_Cursos\UDEMY_PythonMegaCourse\Section16_Fixing_Programming_Errors\144_Runtime_Errors.py", line 10, in <module>
#     print (a/0)
#            ~^~
# ZeroDivisionError: division by zero
# En python no es posible la divison entre 0
#############