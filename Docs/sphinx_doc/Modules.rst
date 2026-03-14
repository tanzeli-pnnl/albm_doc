.. _Modules:

Source Code Modules
===================

ALBM is organized into a set of Fortran 90 modules. The table below
summarizes the main source files and their roles.

.. list-table:: ALBM Source Modules
   :widths: 30 70
   :header-rows: 1

   * - Module file
     - Description
   * - ``bLake.f90``
     - Main program entry point; reads the namelist, initializes the
       model, and calls the time-stepping loop.
   * - ``simulation_mod.f90``
     - Top-level simulation coupler; orchestrates calls to the
       individual process modules at each time step.
   * - ``thermal_mod.f90``
     - Water-column heat transport, convective mixing, and ice
       phenology.
   * - ``soil_thermal_mod.f90``
     - Sediment heat conduction and storage.
   * - ``radiation_mod.f90``
     - Shortwave and longwave radiative transfer through the atmosphere
       and water column.
   * - ``carbon_cycle_mod.f90``
     - Carbon cycling in the water column (CO₂ production, primary
       production, and air–water gas exchange).
   * - ``bubble_mod.f90``
     - CH₄ ebullition (bubble) flux from sediments to the atmosphere.
   * - ``diagenesis_mod.f90``
     - Early diagenesis and pore-water chemistry in lake sediments.
   * - ``boundary_mod.f90``
     - Lateral boundary conditions and catchment runoff inputs.
   * - ``read_data_mod.f90``
     - Reading of all input datasets (climate forcing, lake morphometry,
       auxiliary data).
   * - ``io_utilities_mod.f90``
     - NetCDF-based input/output helper routines.
   * - ``shr_param_mod.f90``
     - Shared model parameters and physical constants.
   * - ``shr_ctrl_mod.f90``
     - Shared control variables and simulation flags.
   * - ``shr_typedef_mod.f90``
     - Shared derived type definitions.
   * - ``phy_const_mod.f90``
     - Physical constants (e.g., gravitational acceleration, density of
       water and ice).
   * - ``bg_const_mod.f90``
     - Biogeochemical constants.
   * - ``math_utilities_mod.f90``
     - Mathematical helper routines (e.g., interpolation, integration).
   * - ``phy_utilities_mod.f90``
     - Physical helper routines (e.g., saturation vapor pressure).
   * - ``bg_utilities_mod.f90``
     - Biogeochemical helper routines.
   * - ``data_buffer_mod.f90``
     - In-memory buffers for time-interpolated forcing data.
   * - ``sensitivity_mod.f90``
     - Sensitivity analysis utilities.
   * - ``bayesian_mod.f90``
     - Bayesian parameter estimation via Markov chain Monte Carlo.
   * - ``costfunc_mod.f90``
     - Cost function evaluation for parameter calibration.
