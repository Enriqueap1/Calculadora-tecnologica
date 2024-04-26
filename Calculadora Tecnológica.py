#importar libreria
import tkinter as tk
import math

#metemos el color por defecto
color = "lightblue"
ventanas_abiertas = []

#estas tres funciones sirven para cerrar la ventana actual y volver a la anterior
def cerrar_todas_las_ventanas():
    for ventana in ventanas_abiertas:
        ventana.destroy()
    ventanas_abiertas.clear()
    ventana_principal.destroy()

def volver_pantalla_principal(ventana_principal, ventana_actual, texto_subpagina):
    ventana_actual.destroy()
    ventanas_abiertas.remove(ventana_actual)
    if texto_subpagina == "Fisica" or texto_subpagina == "Tecnologia" or texto_subpagina == "Termodinamica" or texto_subpagina == "Ajustes":
        ventana_principal.deiconify()
        titulo_principal.configure(bg=color)  # Actualizar el color del título

#creamos la ventana por defecto que se creara siempre
def crear_ventana_color(ventana_principal, color, texto_boton):
    ventana_principal.withdraw()
    ventana_color = tk.Toplevel(ventana_principal)
    ventanas_abiertas.append(ventana_color)
    ventana_color.title(texto_boton)
    ventana_color.attributes('-fullscreen', True)
    ventana_color.configure(bg=color)
    #creamos los atributos de la pantalla

    cerrar_boton = tk.Button(ventana_color, text="Cerrar", font=("Helvetica", 18), command=cerrar_todas_las_ventanas)
    cerrar_boton.place(relx=0.9, rely=0.05)
    #creamos el boton de cerrar

    volver_boton = tk.Button(ventana_color, text="Volver al menú principal", font=("Helvetica", 24),
                             command=lambda: volver_pantalla_principal(ventana_principal, ventana_color, texto_boton))
    volver_boton.place(relx=0.05, rely=0.85)
    #creamos el boton de menu principal para todas las pantallas que no sean el menu principal

    titulo = tk.Label(ventana_color, text=texto_boton, font=("Helvetica", 36), bg=color)
    titulo.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    #creamos el titulo y sus atributos

    #creamos una funcion que segun el boton que elijas se crean unos botones o otros
    if texto_boton == "Tecnologia":
        ensayos = ["Ensayos de dureza y Resilencia", "Ensayo de tracción", "Termodinámica"]
        for i, ensayo in enumerate(ensayos):
            btn = tk.Button(ventana_color, text=ensayo, font=("Helvetica", 24),
                            command=lambda ensayo=ensayo: crear_subpagina(ventana_color, ensayo))
            btn.place(relx=1 / 6, rely=1 / 5 + i * 1 / 6, relwidth=2 / 3)

    elif texto_boton == "Fisica":
        ensayos = ["Trabajo y energia", "Gravitacion", "Induccion"]
        for i, ensayo in enumerate(ensayos):
            btn = tk.Button(ventana_color, text=ensayo, font=("Helvetica", 24),
                            command=lambda ensayo=ensayo: crear_subpagina(ventana_color, ensayo))
            btn.place(relx=1 / 6, rely=1 / 3 + i * 1 / 6, relwidth=2 / 3)
            
#creamos el boton de ajustes 
    elif texto_boton == "Ajustes":
#esta funcion sirve para cambiar el color de fondo y de los titulos
        def modo_oscuro():
            global color
            print("Modo Oscuro Activado")
            color = "gray"
            ventana_principal.configure(bg=color)
            titulo.configure(bg=color)

        def modo_claro():
            global color
            print("Modo Claro Activado")
            color = color
            ventana_principal.configure(bg=color)
            titulo.configure(bg=color)

        # Botón Modo Oscuro
        btn_oscuro = tk.Button(ventana_color, text="Modo Oscuro", font=("Helvetica", 24), command=modo_oscuro)
        btn_oscuro.place(relx=1 / 6, rely=1 / 3, relwidth=2 / 3)

        # Botón Modo Claro
        btn_claro = tk.Button(ventana_color, text="Modo Claro", font=("Helvetica", 24), command=modo_claro)
        btn_claro.place(relx=1 / 6, rely=1 / 2, relwidth=2 / 3)
        
#esta funcion sirve para crear la primera subbpagina
def crear_subpagina(ventana_padre, texto_subpagina):
    ventana_subpagina = tk.Toplevel(ventana_padre)
    ventanas_abiertas.append(ventana_subpagina)
    ventana_subpagina.title(texto_subpagina)
    ventana_subpagina.attributes('-fullscreen', True)
    ventana_subpagina.configure(bg=color)

    cerrar_boton = tk.Button(ventana_subpagina, text="Cerrar", font=("Helvetica", 18), command=cerrar_todas_las_ventanas)
    cerrar_boton.place(relx=0.9, rely=0.05)

    titulo = tk.Label(ventana_subpagina, text=texto_subpagina, font=("Helvetica", 36), bg=color)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    volver_boton = tk.Button(ventana_subpagina, text="Volver atras", font=("Helvetica", 24), command=lambda: volver_pantalla_principal(ventana_padre, ventana_subpagina, texto_subpagina))
    volver_boton.place(relx=0.05, rely=0.85)
#crea los botones segun el boton que elijas 
    if texto_subpagina == "Ensayos de dureza y Resilencia":
        ensayos = ["Brinnel", "Rockwell", "Vickers", "Charpy"]
        for i, ensayo in enumerate(ensayos):
            btn = tk.Button(ventana_subpagina, text=ensayo, font=("Helvetica", 24),
                            command=lambda ensayo=ensayo: crear_sub_subpagina(ventana_subpagina, ensayo))
            btn.place(relx=1 / 6, rely=1 / 3 + i * 1 / 6, relwidth=2 / 3)

    elif texto_subpagina == "Ensayo de tracción":
        ensayos = ["Calcular E", "Calcular T", "Calcular ε"]
        for i, ensayo in enumerate(ensayos):
            btn = tk.Button(ventana_subpagina, text=ensayo, font=("Helvetica", 24),
                            command=lambda ensayo=ensayo: crear_sub_subpagina(ventana_subpagina, ensayo))
            btn.place(relx=1 / 6, rely=1 / 3 + i * 1 / 6, relwidth=2 / 3)

    elif texto_subpagina == "Termodinámica":
        ensayos = ["Motores", "Maquinas Frigorificas", "Maquinas Termicas"]
        for i, ensayo in enumerate(ensayos):
            btn = tk.Button(ventana_subpagina, text=ensayo, font=("Helvetica", 24),
                            command=lambda ensayo=ensayo: crear_sub_subpagina(ventana_subpagina, ensayo))
            btn.place(relx=1 / 6, rely=1 / 3 + i * 1 / 6, relwidth=2 / 3)
            
    elif texto_subpagina == "Trabajo y energia":
        ensayos = ["Velocidad Final","Teorema de las fuerzas vivas","Posicion Mrua"]
        for i, ensayo in enumerate(ensayos):
            btn = tk.Button(ventana_subpagina, text=ensayo, font=("Helvetica", 24),
                            command=lambda ensayo=ensayo: crear_sub_subpagina(ventana_subpagina, ensayo))
            btn.place(relx=1 / 6, rely=1 / 3 + i * 1 / 6, relwidth=2 / 3)
            
    elif texto_subpagina == "Gravitacion":
        ensayos = ["Fuerza de campo","Intensidad de campo","Velocidad de escape "]
        for i, ensayo in enumerate(ensayos):
            btn = tk.Button(ventana_subpagina, text=ensayo, font=("Helvetica", 24),
                            command=lambda ensayo=ensayo: crear_sub_subpagina(ventana_subpagina, ensayo))
            btn.place(relx=1 / 6, rely=1 / 3 + i * 1 / 6, relwidth=2 / 3)
    
    elif texto_subpagina == "Induccion":
        ensayos = ["Flujo magnetico","Angulo que forma", "Superficie de la espira"]
        for i, ensayo in enumerate(ensayos):
            btn = tk.Button(ventana_subpagina, text=ensayo, font=("Helvetica", 24),
                            command=lambda ensayo=ensayo: crear_sub_subpagina(ventana_subpagina, ensayo))
            btn.place(relx=1 / 6, rely=1 / 3 + i * 1 / 6, relwidth=2 / 3)

#creamos la sub_subpagina que es la que realmente hará los calculos
def crear_sub_subpagina(ventana_padre, texto_sub_subpagina):
    ventana_sub_subpagina = tk.Toplevel(ventana_padre)
    ventanas_abiertas.append(ventana_sub_subpagina)
    ventana_sub_subpagina.title(texto_sub_subpagina)
    ventana_sub_subpagina.attributes('-fullscreen', True)
    ventana_sub_subpagina.configure(bg=color)

    cerrar_boton = tk.Button(ventana_sub_subpagina, text="Cerrar", font=("Helvetica", 18), command=cerrar_todas_las_ventanas)
    cerrar_boton.place(relx=0.9, rely=0.05)

    titulo = tk.Label(ventana_sub_subpagina, text=texto_sub_subpagina, font=("Helvetica", 36), bg=color)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    volver_boton = tk.Button(ventana_sub_subpagina, text="Volver atras", font=("Helvetica", 24), command=lambda: volver_pantalla_principal(ventana_padre, ventana_sub_subpagina, texto_sub_subpagina))
    volver_boton.place(relx=0.05, rely=0.85)
    #creamos la funcion para crear los botones y los calculos correspondientes 
    if texto_sub_subpagina == "Brinnel": # Esta parte sirve para calcular Brinnel 
        
        texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para realizar la operación de Brinnel:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Fuerza (kp):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.28, rely=0.32, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Diámetro Penetrador (mm):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.2245, rely=0.42, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Diámetro huella (mm):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.243, rely=0.52, anchor=tk.CENTER)

        # Cuadros editables para ingresar valores
        valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))

        valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
        valor2.place(relx=0.35, rely=0.4, relwidth=0.3)
        valor3.place(relx=0.35, rely=0.5, relwidth=0.3)


        def calcular_brinell(): #subfuncion para calcular
            try:
                fuerza = float(valor1.get())
                diametrop = float(valor2.get())
                diametroh = float(valor3.get())
                f = diametrop - (((diametrop**2) - diametroh**2) ** 0.5)
                resultado = round((fuerza * 2 / (3.14159 * f * diametrop)), 2)

                resultado_label = tk.Label(ventana_sub_subpagina, text=f"Resultado: {resultado} HB", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_brinell)
        calcular_boton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        
    elif texto_sub_subpagina == "Vickers":
            # Texto adicional
            texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para realizar la operación de Vickers:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Fuerza (kp):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.29, rely=0.32, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Diagonal (mm):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.28, rely=0.42, anchor=tk.CENTER)

            # Cuadros editables para ingresar valores
            valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))

            valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
            valor2.place(relx=0.35, rely=0.4, relwidth=0.3)

            def calcular_vickers():
                try:
                    fuerza = float(valor1.get())
                    diagonal = float(valor2.get())
                    resultado = round((fuerza * 1.854 / (diagonal**2)), 2)

                    resultado_label = tk.Label(ventana_sub_subpagina, text=f"Resultado: {resultado} HV", font=("Helvetica", 24), bg=color)
                    resultado_label.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
                except ValueError:
                    resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                    resultado_label.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

            calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_vickers)
            calcular_boton.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

            #Aqui empiezan las sub_subpaginas para Ensayos de dureza y Resilencia
        
    elif texto_sub_subpagina == "Charpy":
            # Texto adicional
            texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para realizar la operación de Charpy:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Altura inicial(m):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.275, rely=0.32, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Altura final(m):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.28, rely=0.42, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Masa de la probeta(kg):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.25, rely=0.52, anchor=tk.CENTER)

            # Cuadros editables para ingresar valores
            valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))

            valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
            valor2.place(relx=0.35, rely=0.4, relwidth=0.3)
            valor3.place(relx=0.35, rely=0.5, relwidth=0.3)


            def Charpy():
                try:
                    m = float(valor1.get())
                    altura_1 = float(valor2.get())
                    altura_2 = float(valor3.get())
                    g = 9.8
                    resultado = round((m*g*(altura_1-altura_2))/2)

                    resultado_label = tk.Label(ventana_sub_subpagina, text=f"Resultado: {resultado} J/m²", font=("Helvetica", 24), bg=color)
                    resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
                except ValueError:
                    resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                    resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

            calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=Charpy)
            calcular_boton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        
    elif texto_sub_subpagina == "Rockwell":
            # Texto adicional
            texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para realizar la operación de Rockwell:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Altura inicial (mm):",font=("Helvetica", 24),bg=color)
            texto.place(relx=0.26, rely=0.32, anchor=tk.CENTER)
            texto=tk.Label(ventana_sub_subpagina,text="Altura final (mm):",font=("Helvetica", 24),bg=color)
            texto.place(relx=0.266, rely=0.42,anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="¿Cono (C) o Bola (B)?:",font=("Helvetica", 24),bg=color)
            texto.place(relx=0.242, rely=0.52, anchor=tk.CENTER)

            # Cuadros editables para ingresar valores
            valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))

            valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
            valor2.place(relx=0.35, rely=0.4, relwidth=0.3)
            valor3.place(relx=0.35, rely=0.5, relwidth=0.3)

            def calcular_rockwell():
                try:
                    d = float(valor2.get()) - float(valor1.get())
                    if valor3.get() == "C":
                        resultado = 100 - d
                    elif valor3.get() == "B":
                        resultado = 130 - d
                    else:
                        raise ValueError("Ingresa valores válidos (C o B)")

                    resultado_label = tk.Label(ventana_sub_subpagina, text=f"Resultado: {resultado}", font=("Helvetica", 24), bg=color)
                    resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
                except ValueError as e:
                    resultado_label = tk.Label(ventana_sub_subpagina, text=f"Error: {str(e)}", font=("Helvetica", 24), bg=color)
                    resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)




            calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_rockwell)
            calcular_boton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    elif texto_sub_subpagina == "Calcular T":
        # Texto adicional
      texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para calcular T:", font=("Helvetica", 24), bg=color)
      texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

      texto_modulo_elastico = tk.Label(ventana_sub_subpagina, text="Modulo elastico (kp):", font=("Helvetica", 24), bg=color)
      texto_modulo_elastico.place(relx=0.25, rely=0.32, anchor=tk.CENTER)

      texto_longitud_inicial = tk.Label(ventana_sub_subpagina, text="Longitud inicial(mm):", font=("Helvetica", 24), bg=color)
      texto_longitud_inicial.place(relx=0.25, rely=0.42, anchor=tk.CENTER)

      texto_longitud_final = tk.Label(ventana_sub_subpagina, text="Longitud final(mm):", font=("Helvetica", 24), bg=color)
      texto_longitud_final.place(relx=0.254, rely=0.52, anchor=tk.CENTER)

      # Cuadros editables para ingresar valores
      valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
      valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
      valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))


      valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
      valor2.place(relx=0.35, rely=0.4, relwidth=0.3)
      valor3.place(relx=0.35, rely=0.5, relwidth=0.3)
      
      def calcular_T():#no funciona lo de calcular
          try:
              valor1_num = float(valor1.get())
              valor2_num = float(valor2.get())
              valor3_num = float(valor3.get())
              
              Alargamiento=((valor3_num-valor2_num)/valor2_num)
              modulo_elastico=(valor1_num)
              resultado = round((modulo_elastico /Alargamiento), 2)
              resultado_label = tk.Label(ventana_sub_subpagina, text=f"Resultado: {resultado} Kp", font=("Helvetica", 24), bg=color)
              resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
          except ValueError:
              resultado_label = tk.Label(ventana_sub_subpagina, text=f"Error: {str(e)}", font=("Helvetica", 24), bg=color)
              resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    
      calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_T)
      calcular_boton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    elif texto_sub_subpagina == "Calcular ε":
      # Texto adicional
      texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para realizar la operación de la deformación unitaria:", font=("Helvetica", 24), bg=color)
      texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
      texto = tk.Label(ventana_sub_subpagina, text="Altura inicial (mm):", font=("Helvetica", 24), bg=color)
      texto.place(relx=0.262, rely=0.32, anchor=tk.CENTER)
      texto = tk.Label(ventana_sub_subpagina, text="Altura final (mm):", font=("Helvetica", 24), bg=color)
      texto.place(relx=0.27, rely=0.42, anchor=tk.CENTER)

      # Cuadros editables para ingresar valores
      valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
      valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))

      valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
      valor2.place(relx=0.35, rely=0.4, relwidth=0.3)

      def calcular_e():
            try:
                valor1_num = float(valor1.get())
                valor2_num = float(valor2.get())
                
                alargamiento = round((valor2_num - valor1_num) / valor1_num, 5)

                resultado_label = tk.Label(ventana_sub_subpagina, text=f"Resultado: {alargamiento} mm", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

      calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_e)
      calcular_boton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    elif texto_sub_subpagina == "Calcular E":
           # Texto adicional
      texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para calcular E:", font=("Helvetica", 24), bg=color)
      texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

      texto_tension = tk.Label(ventana_sub_subpagina, text="Tensión (kp):", font=("Helvetica", 24), bg=color)
      texto_tension.place(relx=0.28, rely=0.32, anchor=tk.CENTER)

      texto_longitud_inicial = tk.Label(ventana_sub_subpagina, text="Longitud inicial(mm):", font=("Helvetica", 24), bg=color)
      texto_longitud_inicial.place(relx=0.252, rely=0.42, anchor=tk.CENTER)

      texto_longitud_final = tk.Label(ventana_sub_subpagina, text="Longitud final(mm):", font=("Helvetica", 24), bg=color)
      texto_longitud_final.place(relx=0.258, rely=0.52, anchor=tk.CENTER)

      # Cuadros editables para ingresar valores
      valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
      valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
      valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))


      valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
      valor2.place(relx=0.35, rely=0.4, relwidth=0.3)
      valor3.place(relx=0.35, rely=0.5, relwidth=0.3)
      def calcular_E():#no funciona lo de calcular
          try:
              valor1_num = float(valor1.get())
              valor2_num = float(valor2.get())
              valor3_num = float(valor3.get())

              Alargamiento=((valor3_num-valor2_num)/valor2_num)
              Fuerza=(valor1_num)
              
              resultado = round((Fuerza /Alargamiento), 2)
              
              resultado_label = tk.Label(ventana_sub_subpagina, text=f"Resultado: {resultado} Kp", font=("Helvetica", 24), bg=color)
              resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
          except ValueError:
              resultado_label = tk.Label(ventana_sub_subpagina, text=f"Error: {str(e)}", font=("Helvetica", 24), bg=color)
              resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

      calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_E)
      calcular_boton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    elif texto_sub_subpagina =="Maquinas Frigorificas":  
     texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para la maquina termica:", font=("Helvetica", 24), bg=color)
     texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
     texto = tk.Label(ventana_sub_subpagina, text="Temperatura Foco Frio (k):", font=("Helvetica", 24), bg=color)
     texto.place(relx=0.245, rely=0.32, anchor=tk.CENTER)
     texto = tk.Label(ventana_sub_subpagina, text="Temperatura Foco Caliente (k):", font=("Helvetica", 24), bg=color)
     texto.place(relx=0.23, rely=0.42, anchor=tk.CENTER)
    
      # Cuadros editables para ingresar valores
     valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
     valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
     
     valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
     valor2.place(relx=0.35, rely=0.4, relwidth=0.3)
      
     def calcular_e():
            valor1_num = float(valor1.get())
            valor2_num = float(valor2.get())

              
            try:
                eficiencia = round(valor1_num / (valor2_num - valor1_num))

                if valor2_num < valor1_num:
                    eficiencia = 0
                
                resultado_label = tk.Label(ventana_sub_subpagina, text=f"Eficiencia = {eficiencia}", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
                
     calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_e)
     calcular_boton.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
      
    elif texto_sub_subpagina == "Maquinas Termicas":
        texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para la maquina termica:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Temperatura Foco Frio (k):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.242, rely=0.32, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Temperatura Foco Caliente (k):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.225, rely=0.42, anchor=tk.CENTER)



        
        valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        
        valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
        valor2.place(relx=0.35, rely=0.4, relwidth=0.3)

            
        
        def calcular_n():
            try:
                valor1_num = float(valor1.get())
                valor2_num = float(valor2.get())
                

                n = round(valor2_num / (valor2_num - valor1_num))

                resultado_label = tk.Label(ventana_sub_subpagina, text=f"Rendimiento: {n}", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_n)
        calcular_boton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
     #revisar ultima parte

    elif texto_sub_subpagina == "Motores":
        # Texto adicional
        texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores para realizar calcular la Motores:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Densidad combustible (kg/L):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.24, rely=0.32, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Cantidad de combustible(L):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.243, rely=0.42, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Poder calorifico combustible (kj/kg):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.215, rely=0.52, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Trabajo util (W):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.285, rely=0.62, anchor=tk.CENTER)


        # Cuadros editables para ingresar valores
        valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor4 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))


        valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
        valor2.place(relx=0.35, rely=0.4, relwidth=0.3)
        valor3.place(relx=0.35, rely=0.5, relwidth=0.3)
        valor4.place(relx=0.35, rely=0.6, relwidth=0.3)


        def calcular_motores():
            try:
                valor1_num = float(valor1.get())
                valor2_num = float(valor2.get())
                valor3_num = float(valor3.get())
                valor4_num = float(valor4.get())
                                
                trabajo_sum = (valor2_num * valor1_num * valor3_num)
                resultado = round(valor4_num/trabajo_sum, 2)


                resultado_label = tk.Label(ventana_sub_subpagina, text=f"Rendimiento: {resultado} ", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


        calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_motores)
        calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    elif texto_sub_subpagina == "Velocidad Final":
        # Texto adicional
        texto = tk.Label(ventana_sub_subpagina, text="Ingrese los valores:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Altura(m):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.31, rely=0.32, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Coeficiente de rozamiento:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.245, rely=0.42, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Angulo:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.315, rely=0.52, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Masa(kg):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.31, rely=0.62, anchor=tk.CENTER)


        # Cuadros editables para ingresar valores
        valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor4 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))


        valor1.place(relx=0.35, rely=0.3, relwidth=0.3)
        valor2.place(relx=0.35, rely=0.4, relwidth=0.3)
        valor3.place(relx=0.35, rely=0.5, relwidth=0.3)
        valor4.place(relx=0.35, rely=0.6, relwidth=0.3)

        def calcular_v():
            try:
                valor1_num = float(valor1.get()) #altura
                valor2_num = float(valor2.get()) #rozamiento
                valor3_num = float(valor3.get())  #Angulo
                valor4_num = float(valor4.get()) #masa
                                
                distancia = valor1_num/math.sin(valor3_num)
                wfr=valor4_num*9.8*math.sin(valor3_num)*valor2_num*distancia*(-1)
                Ep=valor4_num*valor1_num*9.8
                v=((Ep+wfr)*2/valor4_num)**(1/2)


                resultado_label = tk.Label(ventana_sub_subpagina, text=f"Velocidad final: {round(v, 2)} m/s", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
         
        calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_v)
        calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        
    elif texto_sub_subpagina == "Teorema de las fuerzas vivas":
         # Texto adicional
         texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores de la masa 1:", font=("Helvetica", 24), bg=color)
         texto.place(relx=0.285, rely=0.32, anchor=tk.CENTER)
         texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores de la altura 1:", font=("Helvetica", 24), bg=color)
         texto.place(relx=0.285, rely=0.42, anchor=tk.CENTER)
         texto = tk.Label(ventana_sub_subpagina, text="Introduzca los valores de la altura 2:", font=("Helvetica", 24), bg=color)
         texto.place(relx=0.283, rely=0.52, anchor=tk.CENTER)
         
        # Cuadros editables para ingresar valores
         valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
         valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
         valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
         valor4 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))

         valor1.place(relx=0.42, rely=0.3, relwidth=0.3)
         valor3.place(relx=0.42, rely=0.4, relwidth=0.3)
         valor4.place(relx=0.42, rely=0.5, relwidth=0.3)
            
         def calcular_tfv():
            try:
                valor1_num = float(valor1.get())
                valor3_num = float(valor3.get()) 
                valor4_num = float(valor4.get())    
                
                resultado = -((valor1_num*valor4_num*9.8)-(valor1_num*valor3_num*9.8))

                resultado_label = tk.Label(ventana_sub_subpagina, text=f"El trabajo total de las fuerzas es de: -{resultado} J ", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

         calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_tfv)
         calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)         

    elif texto_sub_subpagina == "Posicion Mrua":
        # Texto adicional
        texto = tk.Label(ventana_sub_subpagina, text="Introduzca los valores para calcular la posición Mrua:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Introduzca la aceleracion (N):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.27, rely=0.32, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Introduzca el valor Velocidad inicial (m/s):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.233, rely=0.42, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Introduzca el valor del tiempo (s):", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.255, rely=0.52, anchor=tk.CENTER)

        # Cuadros editables para ingresar valores
        valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        

        valor1.place(relx=0.4, rely=0.3, relwidth=0.3)
        valor2.place(relx=0.4, rely=0.4, relwidth=0.3)
        valor3.place(relx=0.4, rely=0.5, relwidth=0.3)
        

        def calcular_Posicion_Mrua():
            try:
                valor1_num = float(valor1.get())
                valor2_num = float(valor2.get())
                valor3_num = float(valor3.get())
                                
                resultado = round((valor2_num*valor3_num)+((valor1_num*valor3_num**2))/2)

                resultado_label = tk.Label(ventana_sub_subpagina, text=f"Posición: {resultado} m ", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

        calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_Posicion_Mrua)
        calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    elif texto_sub_subpagina == "Velocidad de escape ":
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca los valores para calcular la posición velocidad de escape", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Masa:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.195, rely=0.32, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Radio del planeta:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Altura:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Por 10 elevado a ", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.76, rely=0.25, anchor=tk.CENTER)
            
            # Cuadros editables para ingresar valores
            valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor4 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))



            valor1.place(relx=0.3, rely=0.3, relwidth=0.3)
            valor2.place(relx=0.3, rely=0.4, relwidth=0.3)
            valor3.place(relx=0.3, rely=0.5, relwidth=0.3)
            valor4.place(relx=0.7, rely=0.3, relwidth=0.15)

            def Velocidad_escape():
                try:
                    valor1_num = float(valor1.get())#masa
                    valor2_num = float(valor2.get())#radio
                    valor3_num = float(valor3.get())#altura
                    valor4_num = float(valor4.get())#10**masa
                    valor5_num = (valor1_num*(10**(valor4_num)))
                    valor6_num = (valor2_num + valor3_num)
                    constante  =  (6.67*(10**(-11)))

                    resultado1 = (2*(constante*valor5_num))
                    print(resultado1,1)
                    
                    resultado2 = (resultado1/(valor6_num))
                    
                    resultado =round(resultado2**(0.5),2)
                    print(resultado)


                    resultado_label = tk.Label(ventana_sub_subpagina, text=f"Resultado: {resultado} m/s", font=("Helvetica", 24), bg=color)
                    resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
                except ValueError:
                    resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                    resultado_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

            calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=Velocidad_escape)
            calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER) 


    elif texto_sub_subpagina == "Fuerza de campo":
         # Texto adicional
            texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores de la masa(kg):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.235, rely=0.32, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores de la masa 2(kg):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.235, rely=0.42, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Introduce los valores de la distancia(m):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.243, rely=0.52, anchor=tk.CENTER)
            

            # Cuadros editables para ingresar valores
            valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))


            valor1.place(relx=0.42, rely=0.3, relwidth=0.3)
            valor2.place(relx=0.42, rely=0.4, relwidth=0.3)
            valor3.place(relx=0.42, rely=0.5, relwidth=0.3)

            def Fuerza_de_campo():
                    try:
                        valor1_num = float(valor1.get())
                        valor2_num = float(valor2.get())
                        valor3_num = float(valor3.get()) 
                        
                        resultado = round(((-6.67*10**-11*valor1_num*valor2_num)/valor3_num),2)

                        resultado_label = tk.Label(ventana_sub_subpagina, text=f"La de campo en ese punto es de: {resultado} N ", font=("Helvetica", 24), bg=color)
                        resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
                    except ValueError:
                        resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                        resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
                        
            calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=Fuerza_de_campo)
            calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)  

    elif texto_sub_subpagina == "Flujo magnetico":
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca los valores:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca el valor Angulo que forma:", font=("Helvetica", 24), bg=color)
            texto.place(relx=1/4, rely=0.3, relwidth=1/3)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca el radio (si es circular, si no ponga el valor 0):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.05, rely=0.4, relwidth=0.7)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca el lado (si es cuadrada, si no ponga el valor 0):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.05, rely=0.5, relwidth=0.7)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca el angulo con la normal:", font=("Helvetica", 24), bg=color)
            texto.place(relx=1/4, rely=0.6, relwidth=1/3)
                

                # Cuadros editables para ingresar valores
            valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor1.place(relx=0.7, rely=0.3, relwidth=1/7)
            valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor2.place(relx=0.7, rely=0.4, relwidth=1/7)
            valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor3.place(relx=0.7, rely=0.5, relwidth=1/7)
            valor4 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor4.place(relx=0.7, rely=0.6, relwidth=1/7)


            def flujo_magnetico():
                    try:
                        valor1_num = float(valor1.get())
                        valor2_num = float(valor2.get())
                        valor3_num = float(valor3.get())
                        valor4_num = float(valor4.get())

                        if valor2_num == 0:
                            area = valor3_num**2 
                        
                        elif valor3_num == 0:
                            area = (valor2_num**2) * 3.1416

                        resultado = valor1_num * area * math.sin(valor4_num)

                        resultado_label = tk.Label(ventana_sub_subpagina, text=f"Flujo magnetico: {resultado} wb ", font=("Helvetica", 24), bg=color)
                        resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
                    except ValueError:
                        resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                        resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

            calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=flujo_magnetico)
            calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    elif texto_sub_subpagina == "Angulo que forma":
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca los valores:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca el valor del campo:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.25, rely=0.3, relwidth=0.4)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca el flujo (Puedes usar la calculadora):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.13, rely=0.4, relwidth=0.5)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca la superficie:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.27, rely=0.5, relwidth=0.4)
            
                

                # Cuadros editables para ingresar valores
            valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor1.place(relx=0.6, rely=0.3, relwidth=1/7)
            valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor2.place(relx=0.6, rely=0.4, relwidth=1/7)
            valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor3.place(relx=0.6, rely=0.5, relwidth=1/7)
            


            def Angulo_forma():
                try:
                        valor1_num = float(valor1.get())#valor campo
                        valor2_num = float(valor2.get())#flujo
                        valor3_num = float(valor3.get())#superficie

                        radiales=valor2_num/(valor1_num*valor3_num)
                        resultado =round(math.asin(radiales) *180/3.14159,2)


                        resultado_label = tk.Label(ventana_sub_subpagina, text=f"angulo que forma: {resultado} grados ", font=("Helvetica", 24), bg=color)
                        resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
                except ValueError:
                        resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                        resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
                    

            calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=Angulo_forma)
            calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
            
    elif texto_sub_subpagina == "Intensidad de campo":
         # Texto adicional
        texto = tk.Label(ventana_sub_subpagina, text="Introduzca la masa:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.25, rely=0.32, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="Introduzca la distancia:", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.25, rely=0.42, anchor=tk.CENTER)
        texto = tk.Label(ventana_sub_subpagina, text="por 10 elevado a ", font=("Helvetica", 24), bg=color)
        texto.place(relx=0.72, rely=0.22, anchor=tk.CENTER)

        # Cuadros editables para ingresar valores
        valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
        valor3 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))

        valor1.place(relx=0.35, rely=0.3, relwidth=0.2)
        valor2.place(relx=0.35, rely=0.4, relwidth=0.2)
        valor3.place(relx=0.62, rely=0.3, relwidth=0.2)

        def calcular_g():
            try:
                valor1_num = float(valor1.get())
                valor2_num = float(valor2.get())
                valor3_num = float(valor3.get())               
                resultado = round((6.67*(10**-11)*(valor1_num*(10**valor3_num)))/(valor2_num**2),2)

                resultado_label = tk.Label(ventana_sub_subpagina, text=f"intensidad de campo: {resultado} N", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
            except ValueError:
                resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

        calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=calcular_g)
        calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        
    elif texto_sub_subpagina == "Superficie de la espira":
         # Texto adicional
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca los valores:", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca el radio (si es circular, si no ponga el valor 0):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.15, rely=0.4, relwidth=0.5)
            texto = tk.Label(ventana_sub_subpagina, text="Introduzca el lado (si es cuadrada, si no ponga el valor 0):", font=("Helvetica", 24), bg=color)
            texto.place(relx=0.15, rely=0.5, relwidth=0.5)

                

                # Cuadros editables para ingresar valores
            valor1 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor1.place(relx=0.7, rely=0.4, relwidth=1/7)
            valor2 = tk.Entry(ventana_sub_subpagina, font=("Helvetica", 24))
            valor2.place(relx=0.7, rely=0.5, relwidth=1/7)
            


            def Calcular_superficie():
                    try:
                        valor1_num = float(valor1.get())
                        valor2_num = float(valor2.get())
                        

                        if valor1_num == 0:
                            area = valor2_num**2 
                        
                        elif valor2_num == 0:
                            area = (valor1_num**2) * 3.1416

                        resultado = area 

                        resultado_label = tk.Label(ventana_sub_subpagina, text=f"Area: {resultado} m² ", font=("Helvetica", 24), bg=color)
                        resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
                    except ValueError:
                        resultado_label = tk.Label(ventana_sub_subpagina, text="Error: Ingresa valores válidos", font=("Helvetica", 24), bg=color)
                        resultado_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

            calcular_boton = tk.Button(ventana_sub_subpagina, text="Calcular", font=("Helvetica", 24), command=Calcular_superficie)
            calcular_boton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
            
#creamos el bucle para que se inicie la primera pantalla y los primeros tres botones 
        
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora Tecnológica")
ventana_principal.attributes('-fullscreen', True)
ventana_principal.configure(bg=color)

ventana_principal.protocol("WM_DELETE_WINDOW", cerrar_todas_las_ventanas)

cerrar_todas_ventanas_boton = tk.Button(ventana_principal, text="Cerrar", font=("Helvetica", 18), command=cerrar_todas_las_ventanas)
cerrar_todas_ventanas_boton.place(relx=0.9, rely=0.05)

titulo_principal = tk.Label(ventana_principal, text="Calculadora Tecnológica", font=("Helvetica", 48), bg=color, fg="black")
titulo_principal.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

boton1 = tk.Button(ventana_principal, text="Fisica", font=("Helvetica", 36), command=lambda: crear_ventana_color(ventana_principal, color, "Fisica"))
boton2 = tk.Button(ventana_principal, text="Tecnologia", font=("Helvetica", 36), command=lambda: crear_ventana_color(ventana_principal, color, "Tecnologia"))
boton3 = tk.Button(ventana_principal, text="Ajustes ", font=("Helvetica", 24), command=lambda: crear_ventana_color(ventana_principal, color, "Ajustes"))

boton1.place(relx=1/6, rely=1/3, relwidth=2/3)
boton2.place(relx=1/6, rely=3/5, relwidth=2/3)
boton3.place(relx=0.05, rely=0.05, relwidth=1/13)

ventana_principal.mainloop()