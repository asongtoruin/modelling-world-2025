Coding Approach
===============

``DVector``
-----------

* Core structure used to represent data
* Implemented as part of TfN's ``caf.base`` module
* Stores representation of:

  * Geography (e.g. LSOA)
  * Segmentation (e.g. "#adults in household")

* Uses ``DataFrame`` from ``pandas`` to store the data "under the hood"

Advantages of Using ``DVector``
-------------------------------

* Built-in validation

  * Incompatible segments
  * Warnings if a provided dataset is incomplete

* Easy geographical translations
