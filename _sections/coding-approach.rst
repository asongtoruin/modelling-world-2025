Coding Approach
===============

General Principles
------------------

* Use TfN's existing modules where possible
* Prioritise flexibility - different scenarios to be tested
* Make entry points clear

  * Store constants in a single location
  * Scenario-specific inputs out in config files

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
* Easy segment modification
* Immediate compatibility with other TfN workstreams


Example Config [#]_
-------------------

.. code-block:: yaml

   input_root_directory: I:\NorMITs Land Use\2023\import
   output_directory: F:\Deliverables\Land-Use\2024-12 Release\Employment
   
   base_data:
       lad_raw_4_digit_sic:
           file_path: BRES2022\Employment\preprocessing\bres_employment22_lad_4digit_sic.hdf
           geographical_level: LAD2021+SCOTLANDLAD
           input_segments: [sic_4_digit]

.. [#] Simplified example from scenario_configurations/iteration_5/base_employment_config.yml

Example Processing Code [#]_
----------------------------

.. code-block:: python

   from argparse import ArgumentParser
   from pathlib import Path
   
   import yaml
   
   from land_use import data_processing
   
   
   parser = ArgumentParser('Land-Use base employment command line runner')
   parser.add_argument('config_file', type=Path)
   args = parser.parse_args()
   
   with open(args.config_file, 'r') as text_file:
       config = yaml.load(text_file, yaml.SafeLoader)
   
   # Get output directory for intermediate outputs from config file
   OUTPUT_DIR = Path(config["output_directory"])
   OUTPUT_DIR.mkdir(exist_ok=True)
   
   # read in the data from the config file
   lad_raw_4_digit_sic = data_processing.read_dvector_from_config(
       config=config,
       data_block='base_data',
       key='lad_raw_4_digit_sic'
   )

.. [#] Simplified example from base_employment.py