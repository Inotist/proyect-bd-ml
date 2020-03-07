const defaultColor = "#0EA800" // Especifica el color de los elementos que no se pueden medir
const gradient = orangeGradient // Especifica el gradiente de colores que se va a utilizar para medir los elementos del mapa
const outlier = -20 // Utilizar esta variable si existen valores atípicos que alteran la visibilidad del gradiente
// Se pueden usar tanto valores negativos como positivos según sea necesario, y esto permite que los distintos elementos queden bien diferenciados

const opacity = 0.7 // Especifica la opacidad del contorno de los elementos del mapa
const fillOpacity = 0.95 // Especifica la opacidad del relleno de los elementos del mapa
const defaultOpacity = 0.15 // Especifica la opacidad de los elementos que no se pueden medir

const chartWidth = 1000 // Ancho del svg donde se va a pintar el gráfico de barras
const chartHeight = 500 // Alto del svg donde se va a pintar el gráfico de barras
const legendWidth = 752 // Ancho del svg donde se va a pintar la leyenda
const legendHeight = 15 // Alto del svg donde se va a pintar la leyenda
const legendSeparation = 2 // Píxeles de separación entre los colores de la leyenda

const thickness = 60; // Grosor de los rectángulos del chart