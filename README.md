# Portfolio y página blog de Fabian Sato

Podés usar este portfolio rápido y fácilmente para tu proyecto

## Instalación

Agrega esta linea dentro de tu página `Gemfile` dentro de tu sitio creado en Jekyll:


```ruby
gem "jekyll-theme-clean-portfolio"
```
Y agregá esta linea en tu página  `_config.yml`:

```yaml
theme: jekyll-theme-clean-portfolio
```

y luego ejecutá:

    bundle

O instalalo desde cero en:

    gem install jekyll-theme-clean-portfolio

## Usage

Just create a repository named `<yourusername>.github.io` and then copy all files from this repostory into that repository

Make appropriate changes to the _config.yml file. The configuration is pretty trivial.

## Features:
- Con el poder de bootstrap 4
- Resume generated using a canvas element and PDF.js
- Support for diagrams using mermaid

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/ad1tyawagh/hello. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Development

To set up your environment to develop this theme, run `bundle install`.

Your theme is setup just like a normal Jekyll site! To test your theme, run `bundle exec jekyll serve` and open your browser at `http://localhost:4000`. This starts a Jekyll server using your theme. Add pages, documents, data, etc. like normal to test your theme's contents. As you make modifications to your theme and to your content, your site will regenerate and you should see the changes in the browser after a refresh, just like normal.

When your theme is released, only the files in `_layouts`, `_includes`, `_sass` and `assets` tracked with Git will be bundled.
To add a custom directory to your theme-gem, please edit the regexp in `jekyll-theme-clean-portfolio.gemspec` accordingly.

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

