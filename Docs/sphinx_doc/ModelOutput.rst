.. _ModelOutput:

Model Output
============

ALBM writes model output to NetCDF files in the directory specified by
``archive_dir`` in the ``[archive]`` namelist group.

Output Variables
----------------

The following variables are written to the output files. All variables
are stored on the model vertical grid with the time axis determined by
``archive_tstep``.

Water Column
~~~~~~~~~~~~

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Variable
     - Units
     - Description
   * - ``watertemp``
     - K
     - Water temperature profile.
   * - ``do``
     - mol m^-3
     - Dissolved oxygen concentration profile.
   * - ``dco2``
     - mol m^-3
     - Dissolved CO₂ concentration profile.
   * - ``dch4``
     - mol m^-3
     - Dissolved CH₄ concentration profile.
   * - ``doc``
     - mol m^-3
     - Dissolved organic carbon concentration profile.
   * - ``srp``
     - mol m^-3
     - Soluble reactive phosphorus concentration profile.
   * - ``chl``
     - g m^-3
     - Chlorophyll *a* concentration profile (phytoplankton biomass).
   * - ``phytobio``
     - mol m^-3
     - Phytoplankton functional group biomass profile.

Ice and Surface
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Variable
     - Units
     - Description
   * - ``icethick``
     - m
     - Ice thickness.
   * - ``snowthick``
     - m
     - Snow thickness on ice cover.
   * - ``lakeheatf``
     - W m^-2
     - Downward net heat flux at the water-air interface.
   * - ``latentheatf``
     - W m^-2
     - Latent heat flux at the water-air interface.
   * - ``sensheatf``
     - W m^-2
     - Sensible heat flux at the water-air interface.

Gas Fluxes
~~~~~~~~~~

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Variable
     - Units
     - Description
   * - ``fco2``
     - mol m^-2 d^-1
     - Total CO₂ flux at the lake surface (positive = emission).
   * - ``fch4d``
     - mol m^-2 d^-1
     - Diffusive CH₄ flux at the lake surface.
   * - ``fch4e``
     - mol m^-2 d^-1
     - Ebullitive (bubble) CH₄ flux at the lake surface.

Output File Naming
------------------

According to the ALBM manual, output files are named following the
convention::

  bLakeOut.<varname>.<date0>_<date1>.nc

where ``<varname>`` is the variable name (for example ``watertemp``),
``<date0>`` is the simulation start date from ``Start_Year``/
``Start_Month``/``Start_Day``, and ``<date1>`` is the simulation end
date from ``End_Year``/``End_Month``/``End_Day``.

There is also a special grid-description file:

::

  bLakeOut.zw.nc

Additional manual variables
---------------------------

Depending on activated modules, ALBM can also produce:

* ``lwup``: upward longwave radiation at the water-air interface (W m^-2)
* ``swup``: upward shortwave radiation at the water-air interface (W m^-2)
* ``momf``: momentum energy flux at the water-air interface (kg m^-1 s^-2)
* ``sedheatf``: upward heat flux at the water-sediment interface (W m^-2)
* ``dno3``: dissolved nitrate (not available yet) (mol m^-3)
* ``dnh4``: dissolved ammonium (not available yet) (mol m^-3)

Visualization
-------------

Output NetCDF files can be visualized with standard tools such as:

* `ncview <https://cirrus.ucsd.edu/ncview/>`_ — lightweight interactive
  NetCDF browser
* `Panoply <https://www.giss.nasa.gov/tools/panoply/>`_ — NASA's
  cross-platform data viewer
* Python libraries (``xarray``, ``matplotlib``, ``cartopy``)
* MATLAB/NCO/CDO utilities
