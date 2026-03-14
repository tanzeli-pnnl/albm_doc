.. _Inputs:

Model Inputs
============

ALBM is configured through a Fortran namelist file named ``namelist.bLake``
located in the ``src`` directory. The namelist is divided into the
following groups.

Namelist Groups
---------------

``&general``
~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``run_mode``
     - ``'regular'``
     - Simulation mode. Options: ``'regular'`` (forward run),
       ``'bayesian'`` (Bayesian parameter estimation), or
       ``'sensitivity'`` (sensitivity analysis).
   * - ``lake_file``
     - —
     - Path to the NetCDF file containing lake morphometry and
       geographic attributes for all simulated lakes (e.g.,
       ``Lakes_ISIMIP.nc``).
   * - ``lakeid_file``
     - —
     - Path to a text file listing the lake IDs to simulate (e.g.,
       ``Lakes_ISIMIP_id.list``).
   * - ``lake_range``
     - —
     - Integer range ``start, end`` specifying which lakes (by index
       in ``lakeid_file``) to simulate in the current run.
   * - ``bthmtry_dir``
     - —
     - Directory containing per-lake bathymetry files.
   * - ``param_dir``
     - —
     - Directory containing per-lake parameter files.

``&simulation``
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``Thermal_Module``
     - ``.True.``
     - Activate the thermal module.
   * - ``Bubble_Module``
     - ``.False.``
     - Activate the CH₄ ebullition module.
   * - ``Diagenesis_Module``
     - ``.False.``
     - Activate the sediment diagenesis module.
   * - ``Carbon_Module``
     - ``.False.``
     - Activate the carbon cycling module.
   * - ``Hydro_Module``
     - ``.False.``
     - Activate the hydrological (water balance) module.
   * - ``Start_Year``
     - —
     - Simulation start year (integer).
   * - ``Start_Month``
     - —
     - Simulation start month (1–12).
   * - ``Start_Day``
     - —
     - Simulation start day (1–31).
   * - ``End_Year``
     - —
     - Simulation end year (integer).
   * - ``End_Month``
     - —
     - Simulation end month (1–12).
   * - ``End_Day``
     - —
     - Simulation end day (1–31).
   * - ``Spinup_Month``
     - —
     - Month at which the spin-up period begins each year.
   * - ``Spinup_Day``
     - —
     - Day at which the spin-up period begins each year.
   * - ``nSpinup``
     - —
     - Number of spin-up years.

``&resolution``
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``NWLAYER``
     - 50
     - Number of water-column vertical layers.
   * - ``NSLAYER``
     - 40
     - Number of sediment vertical layers.
   * - ``NRLAYER``
     - 10
     - Number of riparian/runoff layers.

``&radiation``
~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``solar_dir``
     - —
     - Directory containing solar radiation input files.
   * - ``gas_dir``
     - —
     - Directory containing atmospheric gas (CO₂, O₃) input files.
   * - ``albedo_dir``
     - —
     - Directory containing surface albedo input files.
   * - ``co2_file``
     - —
     - Path to the NetCDF file with atmospheric CO₂ concentrations.
   * - ``o3_file``
     - —
     - Path to the NetCDF file with ozone column amounts.
   * - ``aod_file``
     - —
     - Path to the NetCDF file with aerosol optical depth at 550 nm.

``&rundata``
~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``forcing_tstep``
     - ``'day'``
     - Temporal resolution of climate forcing files (``'day'`` or
       ``'month'``).
   * - ``forcing_dir``
     - —
     - Directory (prefix) containing climate forcing files. ALBM
       expects daily near-surface air temperature, precipitation,
       wind speed, humidity, and downwelling radiation.
   * - ``hydro_dir``
     - —
     - Directory (prefix) containing hydrological forcing files
       (used when ``Hydro_Module = .True.``).
   * - ``tref_file``
     - —
     - Path to a NetCDF file with reference temperature climatology.
   * - ``soc_file``
     - —
     - Path to a gridded NetCDF file with soil organic carbon content.
   * - ``veg_file``
     - —
     - Path to a gridded NetCDF file with vegetation/tree cover fraction.
   * - ``wlnd_file``
     - —
     - Path to a gridded NetCDF file with wetland fraction.

``&archive``
~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``archive_tstep``
     - ``'day'``
     - Temporal resolution at which to write model output (``'day'``
       or ``'month'``).
   * - ``archive_dir``
     - —
     - Directory to which model output NetCDF files are written.

``&bayesian``
~~~~~~~~~~~~~

These parameters are used only when ``run_mode = 'bayesian'``.

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``NMAXSAMPLE``
     - 75000
     - Total number of MCMC samples to draw.
   * - ``sample_range``
     - —
     - Range of sample indices for the current run (allows
       parallelisation across multiple jobs).
   * - ``obs_dir``
     - —
     - Directory containing observation files for calibration.
   * - ``obs_var``
     - —
     - Comma-separated list of observation variable names
       (e.g., ``'tw,DO,Dco2,ice,iceon,iceoff,chla'``).
   * - ``obs_weight``
     - —
     - Comma-separated list of weights for each observation variable.
   * - ``mc_file``
     - —
     - Path to the output file for MCMC parameter samples.
   * - ``sa_file``
     - —
     - Path to the output NetCDF file for the sensitivity analysis.

``&dbg``
~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``DEBUG``
     - ``.False.``
     - Enable verbose debug output.
   * - ``RESUBMIT``
     - ``.False.``
     - Restart from a previous checkpoint (if supported).

Input Data Files
----------------

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

Lake Morphometry
~~~~~~~~~~~~~~~~

Lake morphometry data (depth, surface area, bathymetry) must be
provided in NetCDF format. A curated dataset for the ISIMIP lake
ensemble is available from:

   https://doi.org/10.6084/m9.figshare.22635064

The same DOI provides additional ALBM input datasets referenced by the
manual (radiation support files, auxiliary geospatial layers, and
configuration inputs).
