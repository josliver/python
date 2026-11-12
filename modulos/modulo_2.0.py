import sys
sys.path.append("/home/pi/Public/dockerVolumes/pyApp/funciones")
print(sys.path)
import crear_funciones as fun

#print(sys.path)
#print(sys.builtin_module_names)

print(fun.factorial(10))
