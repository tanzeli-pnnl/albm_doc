.. _Inputs:

Model Inputs
============

ALBM is configured through a Fortran namelist file named ``namelist.bLake``
located in the ``src`` directory. The namelist is divided into the
following groups (see :doc:`ModelConfigs` for details).

.. _lake-attributes:

Lake Attributes
---------------

Lake geographic attributes (e.g., location, surface area, depth) must be

.. _forcing-inputs:

Forcing Data
------------

Climate Forcing
~~~~~~~~~~~~~~~

ALBM expects daily climate forcing data in NetCDF-3 format. The required
variables are:

* Near-surface air temperature (K)
* Near-surface daily minimum air temperature (K)
* Near-surface daily maximum air temperature (K)
* Relative humidity (%)
* Surface pressure (Pa)
* Precipitation rate (kg m⁻² s⁻¹)
* Snowfall flux (kg m⁻² s⁻¹)
* Near-surface wind speed (m s⁻¹)
* Downwelling shortwave radiation (W m⁻²)
* Downwelling longwave radiation (W m⁻²)

An example atmospheric forcing file layout is::

  netcdf forcing_obs_Allequash {
  dimensions:
    time = UNLIMITED ;
  variables:
    int date ;
      date:units = "YYYYMMDD" ;
    float tas(time) ;
    float tasmin(time) ;
    float tasmax(time) ;
    float hurs(time) ;
    float ps(time) ;
    float pr(time) ;
    float prsn(time) ;
    float rsds(time) ;
    float rlds(time) ;
    float sfcWind(time) ;
  }

Hydrology Forcing
~~~~~~~~~~~~~~~~~

Hydrology forcing should also be in NetCDF-3 format when
``Hydro_Module = .True.``. An example layout is::

  netcdf forcing_hydro_example {
  dimensions:
    time = UNLIMITED ;
  variables:
    int time(time) ;
    float Qsi(time) ;
    float tQsi(time) ;
    float dQsi(time) ;
    float DICQsi(time) ;
    float DOCQsi(time) ;
    float POCQsi(time) ;
    float SRPQsi(time) ;
    float Qso(time) ;
  }

The ISIMIP2b climate forcing data used in published ALBM simulations
are available from the ISIMIP data portal
(https://www.isimip.org/outputdata/).

.. _bathymetry-inputs:

Bathymetry Data
----------------

Lake morphometry data (depth, surface area, bathymetry) must be
provided in NetCDF format. A curated dataset for the ISIMIP lake
ensemble is available from:

   https://doi.org/10.6084/m9.figshare.22635064

The same DOI provides additional ALBM input datasets referenced by the
manual (radiation support files, auxiliary geospatial layers, and
configuration inputs).

.. _parameter-sample-file:

Parameter Sample File
---------------------

A sample namelist file with example input paths and parameter values is

.. _other-inputs:

Other Input Datasets
---------------------

In addition to the above, ALBM also requires several auxiliary datasets for