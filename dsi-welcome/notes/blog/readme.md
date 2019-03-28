## Blogging

![](http://media.giphy.com/media/lXiRzPb8C5JTJcfPq/giphy.gif)

## What?

* Your personal experience (like a journal)
* Explaining a topic/technique
* Sharing a data science case study
* Your project(s)
* Anything and Everything!
* [Art](https://soundcloud.com/sample_noise/shazuffle-ii-shazam-me)

## Why?

* Build a Personal Brand
* Share your experience (and meet some people -- virtually)
* Do good by educating the world
* [this](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)

## Where?

* Personal Blog
* Bootcamp Review Sites
* Other People's blog
* Content outlets (tutorial sites, guest posts, articles, etc.)

## Getting Started

The landscape of blogging can be daunting especially considering that for a lot of Data Science content you would want Latex Math equations and many plots.  There are a few solutions all with varying levels of flexibility.

The main issues that you have to consider when picking a platform are:

* Formatting (markdown vs. HTML vs. code vs. images/video)
* Hosting (where do my files live)
* Styling (how do I make my blog pretty)
* Sharing (social buttons)
* Why is it so hard to render Latex/equations on the internet?!?!?!

We will be using [Github Pages](https://pages.github.com/) to host our blogs since it is free, easy to use, and works well with Markdown + code examples.

### Static Site Generators

Static site generators are a way to programatically generate static HTML.  This drastically simplifies the hosting process of your content.  I will cover Jekyll here since it is integrated with Github pages.

> [Jekyll docs](http://jekyllrb.com/docs/home/)

To make this easy and automatic here is a template you can fork: https://github.com/dirkfabisch/mediator

1. Fork that repo.
2. Follow the instructions [here](https://pages.github.com/) (you need to create your own repo @ username.github.io and push the template there)
3. Start writing.

_Here is an example of what the blank template can look like with content in it_

[![](http://jekyllthemes.io/previews/23502084.png)](http://blog.base68.com/)

And look to the [tools.md](tools.md#jekyll-and-github-pages) for example of other template to use with Jekyll.

### Docs

* [Using Jekyll with Github Pages](https://help.github.com/articles/using-jekyll-with-pages/)

> If you want to incorporate IPython notebooks: http://cscorley.github.io/2014/02/21/blogging-with-ipython-and-jekyll/

## Examples

### Companies

* [O'Reilly](https://www.oreilly.com/learning/operations-in-pandas)
* [yHat (the best in breed blog)](http://blog.yhathq.com/)
* [Plotly](http://blog.plot.ly/)
* [Dato (formerly Graphlab)](http://blog.dato.com/)

### Personal

* [Greg Reda](http://www.gregreda.com/)
* [Tom Levine](https://thomaslevine.com/)
* [Sebastian Raschka](http://sebastianraschka.com/)

### Past Students

* [Ikechukwu Okonkwo](http://yet-another-data-blog.blogspot.com/2014/04/zipfian-academy-all-12-weeks.html)
* [Dan Saber](http://sabermetricinsights.blogspot.com/2014/05/bayesian-linear-regression-with-pymc.html)
* [Jonny Lee](http://liljonnystyle.blogspot.com/2014/05/markov-where-are-my-umbrellas.html)
* [Erin Burnside](http://www.erinburnside.com/)
* [Mickael Le Gal](http://www.mickaellegal.com/)

## References

### Advice from the Experts

* [How To Achieve Ultimate Blog Success In One Easy Step](http://blog.codinghorror.com/how-to-achieve-ultimate-blog-success-in-one-easy-step/)
* [You Should Blog Even if you have no readers](http://nathanmarz.com/blog/you-should-blog-even-if-you-have-no-readers.html)
* [How to make a personal website, in 9001 easy steps](https://thomaslevine.com/!/making-your-personal-website/)

### Platforms

>I have laid out many of the most popular blog engines here, but unless you have a reason otherwise I would recommend going with Wordpress or Medium.  And the first step is always to simply start writing!

#### Completely Hosted

* [Medium](https://medium.com/)
* [Wordpress](http://stackoverflow.com/a/21142578)

#### Semi-Automated

* [Ghost](https://ghost.org/)
* [Cactus](http://cactusformac.com/)
* [Github Pages](http://dannguyen.github.io/github-for-portfolios/)
* [IPython on Github + `nbconvert`](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)

#### Roll your Own

* Static Site Generator
    * [Pelican](https://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/)
    * [Nikola](http://www.damian.oquanta.info/posts/deploy-your-nikola-powered-blog-content-from-the-ipython-notebook.html)
* [Amazon S3](http://www.allthingsdistributed.com/2011/08/Jekyll-amazon-s3.html)

#### Interactivity

If you want executable Jupyter there are a few awesome projects out there to help us.

* [Thebe](https://oreillymedia.github.io/thebe/): Make static pages executable (doesn't have to be IPython notebook)
* [Binder](http://mybinder.org/): Turn any Github repo into executable notebooks
* [tmpnb.org](): What [try.jupyter.org](https://try.jupyter.org/) uses behind the scenes.
