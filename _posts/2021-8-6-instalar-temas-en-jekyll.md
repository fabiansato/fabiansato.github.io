---
layout: post
---
Podemos colocar facilmente temas (themes) a nuestro trabajos en jekyll simplemente
tenemos que ir a la pagina de [Página oficial de Ruby Gems][ruby-gems]  y buscar el tema que queremos usar. Generalmente se buscan fácilmente colocando "jekkyll-theme" o parecido en el buscador.
Dentro del tema encontrado podemos ir al apartado "página" que muy probable que nos redirija a la página de github donde podremos ver como funciona el template y seguramente un demo de como funciona el mismo.
Buscamos el tema que mas nos guste y allí guardaremos el nombre del mismo (el mismo que parece en la página de rubygems)

Una vez que enemos el tema agregado volvemos a nuestro proyecto y vamos a gemfile.
Agremaos otra entrada  abajo de gem "minima", "~> 2.5" algo asi como
gem "nombre-del-tema"
ejemplo
{% highlight ruby %}
gem "jekyll-theme-bootstrap5"
{% endhighlight %}

y luego en el terminal colocamos
{% highlight ruby %}
bundle install
{% endhighlight %}

Con esto último lo que hace el terminal es buscar dentro del config la nueva "gema" y la instala denmtro de nuestra área de trabajo.

Ahora vamos a {% highlight ruby %}_config.yml{% endhighlight %} y cambiamos el theme jekyll-theme-bootstrap5 (o el nombre que le hayamos puesto a nustro proyecto)

Si todo está ok ejecutaremos nuestro servidor con
{% highlight ruby %}
bundle exec jekyll serve
{% endhighlight %}

Nos fijamos que la pagina se queda en blanco. Nos fijamos el terminal los errores que marcan (generalmente en amarillo) en éste nos muestra que no tenemos el layout faltante o alguna  pagina llamada home

Tenemos que ir al github del template y buscar la carpeta _layouts y anotar todos los que estan dentro.

Ahí directamente buscaremos dentro de nuestro repositorio local y subtituiremos por los layouts faltantes.

Y listo podremos tener nuestro repositorio adaptado para ser usado con el nuevo template.

Opcion B instalar desde el repositorio
Opcional tambien es chequear si el repositorio se puede bajar el repositorio completo en un zip desde la página oficial del template. Dezipear el proyecto y luego realizar:

{% highlight ruby %}
bundle install
{% endhighlight %}

y para cargar el servidor local:

{% highlight ruby %}
bundle exec jekyll serve
{% endhighlight %}


[ruby-gems]: https://rubygems.org


