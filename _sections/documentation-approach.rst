Documentation
=============

General Approach
----------------

* Publicly document as much as possible

  * Methodology *and* results

* Store documentation alongside code

  * Single source for project info

* Host as a website with `ReadTheDocs <https://about.readthedocs.com/>`_

Website as Documentation
------------------------

* Easy to navigate and share
* Allows for interactivity
* Simple formatting of code snippets
* **Free hosting for open-source projects**
  
  * Land-Use documentation - ReadTheDocs
  * This presentation - GitHub Pages

* Automatically rebuilds

Example
-------

.. revealjs-section::
   :data-state: notitle
   :data-background-image: _static/images/documentation_text_example.png
   :data-background-size: contain

Example
-------

.. revealjs-section::
   :data-state: notitle
   :data-background-image: _static/images/documentation_results_example.png
   :data-background-size: contain

Tools
-----

* ``Sphinx``
  
  * Python module - works with existing setup
  * Documentation written in ``.rst`` format
  * Same approach used for this presentation!

* ``jinja2`` - templating
* ``matplotlib`` - (static) graphs
* ``folium`` - interactive maps