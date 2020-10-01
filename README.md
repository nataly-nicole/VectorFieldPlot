
# Vector Field Plot

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
git clone 
cd vectorfieldplot
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


    * 
### Uso

**VectorFieldPlot** es utilizado pegando el código que define la imagen justo al final del archivo del programa. Con un entorno de Python instalado, el programa puede ser ejecutado directamente y el archivo de la imagen se escribirá en el directorio local.

Si ya ha instalado **VectorFieldPlot**, puede cargarlo escribiendo:
    * `import vectorfieldplot.vfp as vfp` (manera recomendada).
    * `from vectorfieldplot.vfp import *` (manera no recomendada)2.

La definición de una imagen dentro de **VectorFieldPlot** consiste básicamente en tres pasos:

1. Crea el documento de la imagen:

    ` doc = vfp.FieldplotDocument(name='Nombre de archivo', width=800, height=600, unit=100) `

    En esta instancia, la clase `FieldplotDocument` que representa un entorno de imagen y tiene la capacidad de escribirse en un archivo de imagen más adelante.

    Los parámetros de `FieldplotDocument` son:

    * **`name`**: Nombre de la imagen y el archivo en el que se guardará.
    * **`width`** (`800`): Ancho de la imagen en pixeles.
    * **`height`** (`600`): Altura de la imagen en pixeles.
    * **`digits`** (`3.8`): Precisión de las líneas de campo en unidades, utilizadas para calcular el espacio entre puntos y el redondeo de números. Se recomienda utilizar 2 < dígitos ≤ 5.
    * **`unit`** (`100`): Número de pixeles de una unidad.
    * **`center`** (`[width/2, height/2]`): Posicón del centro del sistema de coordenadas en pixeles.
    * **`licence`** (`cc-by-sa`): Licencia de la imagen (`cc-by-sa` y `None` son proporcionadas).
    * **`commons`** (`False`): Añade un link a Wikimedia Commons (útil si la imagen será publicada bajo el mismo nombre).

2. Configura el campo:

    `field = vfp.Field([['monopole', {'x':-1., 'y':0., 'Q':1.}]])`

    La clase `Field` contiene la configuración teórica y proporciona todas las funciones para calcular el campo físico. El `field` tiene sólo un parámetro:

    * **`elements`** (`[]`): Lista de elementos de campo. Ver #Field elements.

3. Elementos adicionales pueden ser añadidos después o anexados a la lista `Field.elements`.

    `field.elements.append(['monopole', {'x':1.5, 'y':0., 'Q':-1.}])`

### Encuentra puntos donde las líneas de campo se inician

La clase `Startpath` ayuda a crear puntos de inicio para líneas de campo que están espaciadas inversamente proporcional a la intensidad del campo. Para esto, primero se define una función paramétrica `func(t)` personalizada en 2D en la que se ubicarán todos los puntos de inicio. Un punto de inicio individual es obtenido desde la función `startpos(s)`, con `s` como un parámetro reescalado proporcional a la intensidad de campo inverso barrido:

`start_p = vfp.Startpath(field, func).startpos(s)`

Varios (n) puntos de inicio uniformemente espaciado son obtenidos con la función `npoints`

`start_p_list = vfp.Startpath(field, func).npoints(n)`

Todas las opciones:

* **`field`**: necesita ser una instancia de `Field` válido.
* **`func`**: una función paramétrica `fxy(t)` que retorna un par de coordenadas 2D desde el parámetro `t`.
* **`t0`** (`0`): el parámetro mínimo `t` en que el camino comienza.
* **`t0`** (`1`): el parámetro máximo `t` en que el camino finaliza.
* **`Fmax`** (`1e4`): la magnitud absoluta del campo se recortará si se vuelve mayor que `Fmax`.
* **`F_rescale`** (`None`): una función escalar opcional que reescala la intensidad absoluta del campo, por ejemplo `sqrt` o `lambda t: t**0.2`.

### Integrar el camino de la línea de campo

El usuario debe elegir un punto de partida. Si la dirección en este punto es ambigua, una velocidad de inicio debe ser proporcionada:

`line = vfp.FieldLine(field, [-1, 0], start_v=[0, 1], directions='forward')`

Esto genera una línea de campo y calcula su progresión.

Parámetros de `FieldLine`:

* **`field`**: debe ser una instancia de `Field` válida.
* **`start_p`**: lista `[x, y]` donde el cálculo de la línea comienza.
* **`start_v`** (`None`): dirección inicial opcional. Esto sólo tiene sentido si la dirección del campo en `start_p` es ambigua, por ej, en el punto de una carga.
* **`start_d`** (`None`): primer paso de integración opcional (debe ser pequeño). Útil por ejemplo si la integración comienza en un dipolo.
* **`directions`** (`forward`): Puede ser `forward`, `backward` o `both`. Esto indica las direcciones a las que se seguirá la línea de campo.
* **`maxn`** (`1000`): número máximo de pasos o intentos de integración.
* **`maxr`** (`300`): longitud máxima de línea en unidades.
* **`hmax`** (`1.0`): ancho máximo del paso de integración en unidades.
* **`pass_dipoles`** (`0`): número máximo de dipolos a pasar (`None` significa que no hay límite).
* **`path_close_tol`** (`5e-3`): tolerancia de distancia para cerrar bucles de línea de campo
* **`bounds_func`** (`None`): una función que agrega límites de imagen adicionales donde se evalúa como positivo. Las líneas de campo son truncadas después del proceso de integración.
* **`stop_funcs`** (`None`): `[func_backward, func_forward]`, dos funciones que detienen la integración inmediatamente donde se evalúan como positivo.

### Dibujar contenido en el documento de imagen

Dibuja una línea de campo con sus flechas:

`doc.draw_line(line)`

Parámetros de `vfp.FieldplotDocument.draw_line`:

* **`fieldline`**: necesita ser una instancia válida de `FieldLine`.
* **`maxdist`** (`10`): distancia máxima del punto en el camino dibujo en unidades.
* **`linewidth`** (`2`): ancho de la línea en pixeles.
* **`linecolor`** (`'#000000'`): color de líneas de campo y vectores.
* **`attributes`** (`'[]'`): lista de pares de atributo y valor válidos de **svg** como listas.
* **`arrows_style`** (`None`): estilo de vectores como un diccionario. Los posibles parámetros son:
    * **`min_arrows`** (`1`): número mínimo de vectores por línea de campo.
    * **`max_arrows`** (`None`): número máximo de vectores por línea de campo.
    * **`dist`** (`1.0`): distancia promedio entre dos vectores en unidades.
    * **`scale`** (`1.0`): factor de escala de vectores relativas al ancho de la línea. 
    * **`offsets`** (`{'start':0.5, 'leave_image':0.5, 'enter_image':0.5, 'end':0.5}`): distancia relativa de la flecha en los extremos de la línea `([start, leaving image border, entering image border, end])`.
    * **`fixed_ends`** (`{'start':False, 'leave_image':False, 'enter_image':False, 'end':False}`): No estire la distancia de la flecha en las posiciones especificadas en las compensaciones.
    * **`at_potentials`** (`None`): lista de valores potenciales. Si se dan, las flechas se colocarán donde el potencial toma los valores dados.
    * **`potential`** (`None`): Campo potencial escalar `V(xy)` que se evaluará para la ubicación de la flecha. Si falta, el potencial del campo empleado será utilizado.
    * **`condition_func`**: sólo dibuja una flecha si `f(xy)` se evalua como `True`.

Un campo escalar personalizado puede ser dibujado como una imagen rasterizada de fondo con una codificación de mapa de colores, utilizando la función:

`doc.draw_scalar_field(func, cmap, vmin, vmax)`

* **`func`**: Una función escalar de argumento vectorial `xy` que determina el color. Cualquier función personalizada puede ser ingresada. Ejemplos: `lambda xy: sc.linalg.norm(field.F(xy))` (la intensidad de campo absoluta) o `field.V` (el potencial).
* **`cmap`**: Cualquier mapa de colores de matplotlib. Los mapas de colores predefinidos son `doc.cmap_WtGnBu` y `doc.cmap_AqYlFs`.
* **`vmin` and `vmax`**: valores de campo en los que el primer y último color del mapa de colores son usados y los valores del campo serán recortados.

Líneas equipotenciales de un campo escalar personalizado puede ser dibujado, utilizando la función:

`doc.draw_contours(func, levels, resolution_px, linewidth, linewidths, linecolor, linecolors, dasharray, dasharrays, attributes)`

Internamente, esto usa el algoritmo de cuadrados de marcha de matplotlib.

* **`func`**: Una función escalar del argumento vectorial `xy` que determina los valores del campo. Se puede dar cualquier función personalizada. Ejemplos: `lambda xy: sc.linalg.norm(field.F(xy))` (la intensidad de campo absoluta) o `field.V` (el potencial).
* **`levels`**: lista de niveles en los que los contornos son dibujados.
* **`resolution_px`** (`0.5`): Los contornos son inicialmente evaluados en una cuadrícula regular con espaciado de cuadrícula en píxeles.  Los valores más pequeños dan un dibujo más preciso (sin incrementar el tamaño del archivo, ya que los contornos se simplificarán adecuadamente). Los valores más grandes permiten un cálculo mucho más rápido.
* **`linewidth`** (`0.8`): ancho de línea de todos los contornos en píxeles.
* **`linewidths`** (`None`): lista de anchos de línea para cada contorno en píxeles. La lista se repetirá.
* **`linecolor`** (`#000000`): color para todos los contornos, por defecto es negro.
* **`linecolors`** (`None`): lista de colores de línea individuales para cada contorno. La lista se repetirá.
* **`dasharray`** (`None`): colección de guiones de longitudes alternas (como conjunto flotante, valores en píxeles)
* **`dasharrays`** (`None`): lista de colecciones de guiones para cada contorno.
* **`attributes`** (`{}`): atributos svg adicionales que se pasarán a cada contorno, como stroke-linejoin.


Dibuja todos los símbolos en nuestro campo de un tipo:

`doc.draw_charges(field)`

Posibles símbolos:

* **`draw_charges, draw_dipoles, draw_currents, draw_magnets, charges, dipoles and currents`** can take scale as parameter.

Los objetos autodefinidos pueden ser dibujados mediante

`doc.draw_object('circle', {'cx':0, 'cy':0, 'r':1})`

con parámetros:

* **`name`**: nombre svg especificado: `'circle'`, `'path'`, `'g'`, `'rect'`, etc.
* **`params`**: un diccionario de parámetros svg válidos.
* **`group`** (`None`): un objeto previamente dibujado que tiene tipo "g". El nuevo objeto será un subelemento.

### Elementos de Campo

Cuando crea un campo en **VectorFieldPlot**, el parámetro principal será un diccionario de Python, que incluye el nombre de cada componente de campo y una lista de listas de argumentos, que contienen los parámetros esenciales de este componente. P.ej.:

`field = vfp.Field([['monopole':{'x':-1, 'y':0, 'Q':1}], ['monopole':{'x':1, 'y':0, 'Q':-1}]])`

Los siguientes elementos están incluidos en **VectorFieldPlot** y se pueden usar de inmediato:

#### `'homogeneous'`:  {Fx, Fy}

Crea un campo constante sobre el plano completo de la imagen. Parámetros:

* **`Fx, Fy`**: componente en $x$ e $y$ de campo constante.

#### `'monopole'`: {x, y, Q}

Crea un monopolo eléctrico o magnético, es decir, una carga. Parámetros:

* **`x, y`**: posición del monopolo ($\vec{r}^{\,\prime}$).
* **`Q`**: magnitud positiva o negativa de la carga ($Q$).

$$\vec F_\mathrm{m}(\vec{r}^{\,\prime} + \vec{r}) = \frac{Q}{4\pi} \cdot \frac{\vec{r}}{||\vec{r}||^3}.$$

#### `'dipole'`: {x, y, px, py}

Crea un dipolo eléctrico o magnético en forma de punto. Parámetros

* **`x, y`**: posición del dipolo ($\vec{r}^{\,\prime}$).
* **`px, py`**: componentes del momento dipolar ($\vec{p}$).

$$\vec{F}_\mathrm{p}(\vec{r}^{\,\prime} + \vec{r}) = \frac{3(\vec{p} \cdot \vec{r}) \vec{r} - (\vec{r} \cdot\vec{ r}) \vec{p}}{4\pi |\vec{r}|^5}.$$

#### `'dipole2d'`: {x, y, px, py}

Crea un dipolo bidimensional eléctrico o magnético, es decir, dos líneas cargadas infinitas en la dirección $z$ que están infinitesimalmente cercanas. Parámetros:

* **`x, y`**: posición del dipolo ($\vec{r}^{\,\prime}$).
* **`px, py`**: componentes del momento dipolar ($\vec{p}$).

$$\vec{F}_\mathrm{p}(\vec{r}^{\,\prime} + \vec{r}) = \frac{2(\vec{p} \cdot \vec{r})\vec{r} - (\vec{r} \cdot \vec{r})\vec{p}}{2\pi |\vec{r}|^4}.$$

#### `'quadrupole'`: {x, y, Qxx, Qxy, Qyy}

Crea un cuadrupolo eléctrico o magnético en forma de punto. La matriz de cuadrupolos es
$Q=\begin{pmatrix}
Q_{xx} & Q_{xy} & 0 \\
Q_{xy} & Q_{yy} & 0\\
0      & 0      & -Q_{xx}-Q_{yy}\\
\end{pmatrix}$
ya que todos los componentes relacionados con la coordenada z no afectan el campo en el plano $xy$. Parámetros:

* **`x, y`**: posición del cuadrupolo ($\vec{r}^{\,\prime}$).
* **`Qxx, Qxy, Qyy`**: componentes del tensor cuadrupolar.

$$\vec{F}_\mathrm{q}(\vec{r}^{\,\prime} + \vec{r}) = \frac{1}{2} \frac{5(\vec{r} \cdot Q \cdot \vec{r})\vec{r} - 2r^2 (Q\cdot\vec{r})}{4\pi|\vec{r}|^7}.$$

#### `'wire'`: {x, y, I}

Crea un cable infinito perpendicular al plano de la imagen que lleve la corriente hacia afuera del plano de la imagen. Parámetros:

* **`x, y`**: posición del cable ($\vec{r}^{\,\prime}$).
* **`I`**: corriente.

$$\vec{F}_\mathrm{w}(\vec{r}^{\,\prime} + \vec{r}) = I\,\hat{z} \times \frac{\vec{r}}{2\pi\,r^2}.$$

#### `'charged_wire'`: {x, y, q}

Crea un cable infinito perpendicular al plano de la imagen que poseea una carga $q$ por unidad de longitud. Parámetros:

* **`x, y`**: posición del cable ($\vec{r}^{\,\prime}$).
* **`q`**: carga por unidad de longitud.

$$\vec{F}_\mathrm{cw}(\vec{r}^{\,\prime} + \vec{r}) = \hat{r}\frac{q}{2\pi\,r}.$$

#### `'charged_line'`: {x0, y0, x1, y1, Q}

Crea una línea cargada homogénea dentro del plano de la imagen. Parámetros:

* **`x0, y0`**: comienzo de la línea.
* **`x1, y1`**: final de la línea.
* **`Q`**: carga total.

#### `'charged_plane'`: {x0, y0, x1, y1, q}

Crea un plano cargado homogéneo perpendicular a la imagen y que se expande hasta el infinito. Parámetros:

* **`x0, y0`**: primer borde.
* **`x1, y1`**: segundo borde.
* **`q`**: carga por unidad de longitud en la dirección $z$.

#### `'charged_rect'`: {x0, y0, x1, y1, Lz, Q}

Crea un rectángulo cargado homogéneamente perpendicular a la imagen y de longitud `Lz` en la dirección $z$. Parámetros:

* **`x0, y0`**: primer borde.
* **`x1, y1`**: segundo borde.
* **`Lz`**: longitud del rentángulo en la dirección $z$.
* **`Q`**: carga total.

#### `'charged_disc'`: {x0, y0, x1, y1, Q}

Crea el campo eléctrico (o campo magnético $\vec{H}$) de un disco redondo delgado cargado homogéneamente con su eje de simetría hacia dentro del plano de la imagen. Parámetros:

* **`x0, y0`**: punto del primer borde del disco en el plano de la imagen.
* **`x1, y1`**: punto del segundo borde del disco en el plano de la imagen.
* **`Q`**: carga totan en el disco.

#### `'sheetcurrent'`: {x0, y0, x1, y1, I}

Crea el campo magnético de una corriente a través de una hoja plana, finita en el plano $xy$ pero expandiéndose hasta el infinito en la dirección $z$. Parámetros:

* **`x0, y0`**: primer borde la hoja.
* **`x1, y1`**: segundo borde de la hoja.
* **`I`**: corriente total por la hoja ( en la dirección del eje $z$ hacia afuera del plano de la imagen).

#### `'ringcurrent'`: {x0, y0, phi, R, I}

Crea el campo magnético de un anillo redondo con su eje de simetría dentro del plano de la imagen. Parámetros:

* **`x0, y0`**: centro del anillo.
* **`phi`**: dirección angular del eje del anillo desde el eje $x$ al eje $y$ medido en radianes.
* **`R`**: radio del anillo.
* **`I`**: corriente por el anillo (en sentido horario con respecto a la dirección del eje).

#### `'coil'`: {x0, y0, phi, R, Lhalf, I}

Crea el campo magnético de una bobina ideal con su eje de simetría dentro del plano de la imagen. ¡El campo también es correcto para el campo $\vec{B}$ de los imanes cilíndricos! Parámetros:

* **`x0, y0`**: centro de la bobina.
* **`phi`**: dirección angular del eje de la bobina medido desde el eje $x$ al $y$ en radianes.

angular direction of the coil axis from x- to y-axis in radians $\vec{m} = (\cos(\varphi), \sin(\varphi))$.
* **`R`**: radio de la bobina.
* **`Lhalf`**: la mitad de la longitud de la bobina.
* **`I`**: corriente a través de la bobina multiplicada por su número de bobinado (en sentido horario con respecto a la dirección del eje).

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
