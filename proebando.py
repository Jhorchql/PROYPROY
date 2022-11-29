importar  streamlit  como  st
importar  pandas  como  pd
importar  numpy  como  np

#título
st . título ( 'Índices Soberanos 2010 - 2022' )
st . subtítulo ( "Miembros del equipo" )
st . descuento ( """
- Palacios Ninahuanca, Ninoska
-Orozco Chupos, Frank
-Quispe Laura, Jhorch
- Parillo Sánchez, Yassmin Diana
""" )
st . descuento ( """
---
La información contenida en esta página web permite acceder al Dataset “Índices Soberanos 2010 - 2022”
elaborado por el Ministerio de Economía y Finanzas del Perú.
Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/%C3%ADndices-soberanos-2010-2022)
---
""" )
def  cargar_datos ():
    url = "https://raw.githubusercontent.com/Frank10OC/proyecto/main/indices_soberanos%20(1).csv"
    devolver  p.d. _ leer_csv ( url )
st . casilla de verificación ( "Usar ancho de contenedor" , valor = Falso , clave = "use_container_width" )

df  =  cargar_datos ()
st . marco de datos ( df , use_container_width = st . session_state . use_container_width )
url = "https://raw.githubusercontent.com/Frank10OC/proyecto/main/indices_soberanos%20(1).csv"
c = pd . leer_csv ( url )
#comparacion del indice nominal e indice real
df  =  c . drop ( columnas  = [ "FECHA" , "INDICE_NOMINAL" , "INDICE_REAL" ])
st . marco de datos ( df , use_container_width = st . session_state . use_container_width )
st . gráfico_de_líneas ( df )
#"INDICE_NOMINAL","RENT_ANUAL_IN"
i1 =  c . drop ( columnas  = [ "FECHA" , "INDICE_REAL" , "RENT_ANUAL_IR" ])
st . marco de datos ( i1 , use_container_width = st . session_state . use_container_width )
#"INDICE_NOMINAL","RENT_ANUAL_IN"
i2 =  c . drop ( columnas  = [ "FECHA" , "INDICE_NOMINAL" , "RENT_ANUAL_IN" ])
st . marco de datos ( i2 , use_container_width = st . session_state . use_container_width )

df1 =  c
set_fecha =  np . ordenar ( df1 [ "FECHA" ]. dropna (). único ())
#Seleccion del departamento
opcion_fecha  =  st . selectbox ( 'Selecciona una fecha' , set_fecha )
df_fecha  =  df1 [ df1 [ "FECHA" ] ==  opcion_fecha ]
num_filas  =  len ( df_fecha . ejes [ 0 ])
