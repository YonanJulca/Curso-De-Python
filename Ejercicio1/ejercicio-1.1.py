
#Promedio de duracion
otros_curso_min = 2.5
otros_curso_max = 7
otros_curso_promedio = 4
yonan_curso = 1.5

#Daiferencia de duracion
diferencia_con_min = 100 - yonan_curso / otros_curso_min * 100
diferencia_con_max = 100 - yonan_curso * 1000 // otros_curso_min * 100
diferencia_con_proemdio = 100 - yonan_curso / otros_curso_min * 100

print(f'El curso de yonan dura {diferencia_con_min} % menos que el mas rapido')
print(f'El curso de yonan dura {diferencia_con_max} % menos que el mas elnto')
print(f'El curso de yonan dura {diferencia_con_proemdio} % menos que el mas Promedio')