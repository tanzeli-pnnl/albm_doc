.. _ModelConfigs:

Model Configurations
====================

ALBM simulation is configured through a Fortran namelist file named ``namelist.bLake``
located in the ``src`` directory. The namelist is divided into the following groups. 

.. _namelist-groups:

Namelist Groups
---------------

``general``
~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``run_mode``
     - ``'regular'``
     - Simulation mode. Options: ``'regular'`` (forward run) or
       ``'sensitivity'`` (ensemble run for sensitivity analysis or parameter calibration).
   * - ``lake_file``
     - —
     - Path (relative or absolute) to the NetCDF file containing lake geographic attributes
       for all simulated lakes (e.g., ``'./Lakes_benchmark.nc'`` for ``Lakes_benchmark.nc`` 
       in the ``src`` directory). See :ref:`lake-attributes` for details.
   * - ``lake_range``
     - —
     - Integer range ``start, end`` specifying which lakes (by index in ``lake_file``) 
       to simulate in the current run (e.g., ``1, 10`` to simulate the first 10 lakes).
   * - ``bathy_file``
     - —
     - Path (relative or absolute) to the NetCDF file containing bathymetry data for 
       all simulated lakes (e.g., ``'./Lakes_benchmark_bathymetry.nc'`` for 
       ``Lakes_benchmark_bathymetry.nc`` in the ``src`` directory). 
       See :ref:`bathymetry-inputs` for details.
   * - ``opt_file``
     - ``''``
     - Path (relative or absolute) to the parameter file for the current simulation. 
       If empty, a default lake-type-specific parameter file in the ``src/Parameters`` 
       directory will be used. See :ref:`model-parameters` for details.

``simulation``
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``Thermal_Module``
     - ``.True.``
     - Activate the WTM and STM modules (see :ref:`model-modules`).
   * - ``Bubble_Module``
     - ``.False.``
     - Activate the BTM module (see :ref:`model-modules`).
   * - ``Diagenesis_Module``
     - ``.False.``
     - Activate the SBM module (see :ref:`model-modules`).
   * - ``Carbon_Module``
     - ``.False.``
     - Activate the WBM module (see :ref:`model-modules`).
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
     - 7
     - Month at which the spin-up period begins.
   * - ``Spinup_Day``
     - 1
     - Day at which the spin-up period begins.
   * - ``nSpinup``
     - 2
     - Number of spin-up years.

``resolution``
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``NWLAYER``
     - 50
     - Number of water-column vertical layers (see :ref:`model-resolution`).
   * - ``NSLAYER``
     - 40
     - Number of sediment vertical layers (see :ref:`model-resolution`).
   * - ``NRLAYER``
     - 10
     - Number of bubble radius bands.
   * - ``NSCOL``
     - 5
     - Number of sediment columns (see :ref:`model-resolution`).

``bayesian``
~~~~~~~~~~~~~

These parameters are used only when ``run_mode = 'sensitivity'``.

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``NMAXSAMPLE``
     - 10000
     - Total number of MCMC samples to draw.
   * - ``sample_range``
     - 1, 10000
     - Integer range ``start, end`` specifying which samples (by index in ``mc_file``) 
       to simulate in the current run (e.g., ``1, 1000`` to simulate the first 1000 samples).
   * - ``mc_file``
     - —
     - Path (relative or absolute) to the parameter sample file that contains 
       MCMC parameter samples (e.g., ``'./model_parameters.dat'`` for 
       ``model_parameters.dat`` in the ``src`` directory). See :ref:`parameter-sample-file` for details.
   * - ``SA_Start_Year``
     - —
     - Start year to output the sensitivity run (integer).
   * - ``SA_Start_Month``
     - —
     - Start month to output the sensitivity run (1–12).
   * - ``SA_Start_Day``
     - —
     - Start day to output the sensitivity run (1–31).
   * - ``SA_End_Year``
     - —
     - End year to output the sensitivity run (integer).
   * - ``SA_End_Month``
     - —
     - End month to output the sensitivity run (1–12).
   * - ``SA_End_Day``
     - —
     - End day to output the sensitivity run (1–31).

``radiation``
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

.. _model-parameters:

Model Parameters
------------------

Tunable ALBM parameters are defined in ``shr_param_mod.f90`` and set through 
a parameter file which is specified by ``opt_file`` in the ``general`` namelist group. 
Default lake-type-specific parameter files are provided in the ``src/Parameters`` 
directory (e.g., ``optpar_yedoma.dat`` for Yedoma lakes). 

``general``
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
