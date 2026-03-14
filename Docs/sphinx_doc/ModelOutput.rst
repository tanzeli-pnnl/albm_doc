.. _ModelOutput:

Model Output
============

ALBM writes model output to NetCDF files in the directory specified by
``archive_dir`` in the ``[archive]`` namelist group. One output file is
created per lake per simulation.

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
   * - ``tw``
     - K
     - Water temperature profile.
   * - ``DO``
     - mg L⁻¹
     - Dissolved oxygen concentration profile.
   * - ``Dco2``
     - μmol L⁻¹
     - Dissolved CO₂ concentration profile.
   * - ``Dch4``
     - μmol L⁻¹
     - Dissolved CH₄ concentration profile.
   * - ``chla``
     - μg L⁻¹
     - Chlorophyll *a* concentration profile (phytoplankton biomass).

Ice and Surface
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Variable
     - Units
     - Description
   * - ``ice``
     - m
     - Ice thickness.
   * - ``iceon``
     - day of year
     - Ice-on date (lake freeze-up).
   * - ``iceoff``
     - day of year
     - Ice-off date (lake ice break-up).

Gas Fluxes
~~~~~~~~~~

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Variable
     - Units
     - Description
   * - ``fco2``
     - g C m⁻² day⁻¹
     - Diffusive CO₂ flux at the lake surface (positive = emission).
   * - ``fch4_diff``
     - g C m⁻² day⁻¹
     - Diffusive CH₄ flux at the lake surface.
   * - ``fch4_ebul``
     - g C m⁻² day⁻¹
     - Ebullitive (bubble) CH₄ flux at the lake surface.

Output File Naming
------------------

Output files are named following the convention::

   <archive_dir>/<lake_id>_output.nc

where ``<lake_id>`` is the integer identifier of the lake as listed in
``lakeid_file``.

Visualization
-------------

Output NetCDF files can be visualized with standard tools such as:

* `ncview <https://cirrus.ucsd.edu/ncview/>`_ — lightweight interactive
  NetCDF browser
* `Panoply <https://www.giss.nasa.gov/tools/panoply/>`_ — NASA's
  cross-platform data viewer
* Python libraries (``xarray``, ``matplotlib``, ``cartopy``)
* MATLAB/NCO/CDO utilities
