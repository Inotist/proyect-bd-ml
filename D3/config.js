const defaultColor = "#0EA800" // Especifica el color de los elementos que no se pueden medir
const gradient = orangeGradient // Especifica el gradiente de colores que se va a utilizar para medir los elementos del mapa
const outlier = -20 // Utilizar esta variable si existen valores atípicos que alteran la visibilidad del gradiente
// Se pueden usar tanto valores negativos como positivos según sea necesario, y esto permite que los distintos elementos queden bien diferenciados

const opacity = 0.7 // Especifica la opacidad del contorno de los elementos del mapa
const fillOpacity = 0.95 // Especifica la opacidad del relleno de los elementos del mapa
const defaultOpacity = 0.15 // Especifica la opacidad de los elementos que no se pueden medir

const legendWidth = 654 // Ancho del svg donde se va a pintar la leyenda
const legendHeight = 15 // Alto del svg donde se va a pintar la leyenda
const legendSeparation = 2 // Píxeles de separación entre los colores de la leyenda

const margin = {top: 20, right: 20, bottom: 70, left: 40} // Márgenes del gráfico de barras con respecto al svg en el que se encuentra
const chartWidth = 1000 - margin.left - margin.right // Ancho del svg donde se va a pintar el gráfico de barras (solo se debe editar el número, los márgenes se vuelven a sumar en la creación del svg)
const chartHeight = 500 - margin.top - margin.bottom // Alto del svg donde se va a pintar el gráfico de barras (solo se debe editar el número, los márgenes se vuelven a sumar en la creación del svg)
const barColor = "#DB5E44" // Color de las barras del gráfico