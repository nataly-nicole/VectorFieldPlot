
# VectorFieldPlot

**VectorFieldPlot** (VFPt) es un script escrito en Python que crea gráficos de líneas de campo de alta calidad en el formato gráfico vectorial **svg**.

* Traducción al español de: https://commons.wikimedia.org/wiki/User:Geek3/VectorFieldPlot#Field_calculation
* Sitio del autor original: https://commons.wikimedia.org/wiki/User:Geek3
* Traducción y algunos aportes relativas al uso de esta versión por Nataly Nicole Ibarra Vera (natalynicole.ibarravera@gmail.com).

## Sobre VectorFieldPlot

**VectorFieldPlot** fue especialmente diseñado para el uso en **Wikipedia Commons**. La falta de diagramas de campo físicos correctos de alta calidad en **Wikimedia Commons** me ha inspirado a compensar esto y proveer una herramienta que permita a los usuarios crear los diagramas de campo que éstos requieran. **VectorFieldPlot** ha crecido más allá de la etapa de un simple y pequeño script que ya podría realizar la tarea de crear gráficos de campos físicos. En cambio, intenta cumplir sus requerimientos de la mejor manera posible, que son:

* Corrección/Precisión Física.
* Pequeño tamaño de archivo/Eficiencia de procesamiento.
* Claridad y belleza de la imagen.
* Reutilización de imágenes.
* Otros aspectos son sólo de orden secundario. **VectorFieldPlot** no se desenvolverá de lo mejor en:
    * Simplicidad del código.
    * Fácil uso.
    * Velocidad de ejecución.
    * Efectos gráficos elegantes.

## Código

La versión origian de **VectorFieldPlot** está escrito en **Python 3** y usa muchas características de **SciPy** y **lxml**. Se puede ejecutar directamente después de insertar la descripción de su imagen al final del [código del programa](https://commons.wikimedia.org/wiki/User:Geek3/VectorFieldPlot#Field_calculation).

**Comentarios respecto de la versión en Github**:
* En esta versión, el script original (versión=3.1) se ha modularizado para ser instalado y cargado en los notebooks que ejemplifican su uso. Se recalca que hasta el momento no se ha realizado ninguna modificación significativa a la versión original

* Instalación en Linux:
```
git clone https://github.com/nataly-nicole/VectorFieldPlot.git
cd VectorFieldPlot
pip install -r requirements.txt
python setup.py install
```
* Además se verifica que si bien el código original está escrito en **Python 3**, también funciona sin inconvenientes en **Python 2**.


## Registro de cambios

* 1.0: Versión inicial.
* 1.1: Se añade soporte para campos configurados por el usuario.
* 1.2: Soporte para el primer paso de integración arbitrario.
* 1.3: Se agregó una nueva función de contorno.
* 1.4: Se agregó el campo de discos cargados.
* 1.5: Se agregó fórmula analítica más rápida para anillos de corriente.
* 1.6: Se agregó cable cargado en el plano de la imagen.
* 1.7: Adaptación menor para manejar `Nones` sin advertencia de desaprobación
* 1.8: Corrección de error: las esquinas de las líneas de campo no se detectaron en algunos casos
* 1.9: Se permite dibujos en el fondo detrás de las líneas de campo.
* 1.10: Soporte agregado para imágenes rasterizadascampos escalares.
* 2.0: Sintaxis actualizada para la definición de elementos de campo. Ahora cada elemento usa un diccionario con variables descriptivas. Funciones agregadas para campos potenciales.
* 2.1: Más potenciales implementados: `Charged_wire`, `Charged_plane`, `Charged_rect` y `Charged_disc`.
* 2.2: Funciones individuales invocables creadas para cada tipo de elemento de campo.
* 2.3: Dibujo agregado de curvas de nivel equipotenciales. Permitir colocar flechas en valores potenciales fijos.
* 2.4: Función de condición agregada para flechas y dipolo 2D agregado.
* 2.5: Se permite color de fondo arbitrario.
* 3.0: Se actualiza a Python 3.
* 3.1: Aceleración en aproximadamente un factor de tres, utilizando el algoritmo de Bulirsch y menos funciones de SciPy.

## ¿Cómo funciona?

### Cálculo de Campo

**VectorFieldPlot** proporciona fórmulas para calcular el campo eléctrico en cualquier punto del plano de la imagen. El usuario puede juntar algunos elementos generadores de campo como cargas o cables. Los campos de esos elementos se suman y constituyen el campo total.

### Integración de las líneas de campo

Cada línea de campo comienza en un punto dado por el usuario. Luego se lleva adelante utilizando el método clásico de Runge-Kutta a cuarto orden con adaptación de tamaño escalonado. Bueno, SciPy nos proporciona una rutina para cosas como esa, es decir, odeint. Sin embargo, **VectorFieldPlot** utiliza su propia rutina, ya que hay toneladas de casos especiales como singularidades, bordes o cierres de bucles, todos los cuales necesitan un tratamiento especial.

La integración pasa de un punto a otro hasta que excede algunos límites dados, llega a una singularidad o cierra un ciclo. Después de eso, se proporciona una rutina densa de salida, que hace que la línea de campo completa sea accesible como una función paramétrica eficiente.

Con algunos elementos de campo aparecen ubicaciones no diferenciables. En estos casos, **VectorFieldPlot** proporciona algunas rutinas sofisticadas para detectar eso, ubicarlos con precisión y pasar cerca de ellos sin generar errores significativos.

### Creación de polilíneas (Polyline creation)

**VectorFieldPlot** está supuesto para crear salida vectorial. Por lo tanto, todos los caminos deben representarse de manera adecuada. Las curvas cúbicas de Bézier son una forma de hacer esto, pero el inconveniente de adaptarlas a una curva dada dentro de los límites de precisión dados ha hecho que los segmentos de líneas rectas simples sean la primera opción.

**VectorFieldPlot** ejecuta un proceso iterativo de colocar segmentos de línea en el camino, mediendo los errores resultantes y, en consecuencia, adaptando la longitud del segmento. El resultado es una ruta bastante eficiente en memoria, que satisface los precisos requerimientos dados más allá de las desviaciones observables.

### Exportar imagen

**VectorFieldPlot** usa la biblioteca **lxml** para generar **xml** y especialmente código **svg**. Todos los elementos de la imagen son traducidos al lenguaje **svg** y se escritos en el archivo de imagen. Las imágenes vectoriales pueden ser visualizadas directamente con firefox, eye de gnome, rsvg-view y muchos más. Los programas gráficos como gimp permiten la conversión a imágenes rasterizadas en formato **png** si es necesario.

### Uso
Link.

# Ejemplos

## [Galería] (https://commons.wikimedia.org/wiki/User:Geek3/VectorFieldPlot#/media/File).

## Mejoras y errores

**VectorFieldPlot** es una pieza complicada de código. Es posible que todavía haya algunos errores que esperan su oportunidad de aparecer. Si descubre uno o se enfrenta a algún comportamiento extraño, la mejor manera es utilizar la [página de discusiones](https://commons.wikimedia.org/wiki/User_talk:Geek3/VectorFieldPlot). Evite realizar modificaciones directamente en el [código fuente de la página](https://commons.wikimedia.org/wiki/User:Geek3/VectorFieldPlot#Field_calculation), ya que pueden sobrescribirse. Si tienes ideas, mejoras o parches, publíquelo en la página de discusiones o cree su propio clon de **VectorFieldPlot** de acuerdo con los términos de la licencia.

## Futuros desarrollos

**VectorFieldPlot** se puede ampliar de muchas formas imaginables. Las extensiones más probables que pueden surgir en el futuro previsible son:

* Creación de animaciones.
* Inclusión de superficies metálicas.

## Licence

**VectorFieldPlot** está licenciado bajo los términos de la Licencia Pública General GNU (https://www.gnu.org/licenses/gpl.html). Esto lo convierte en software gratuito.


```python

```
