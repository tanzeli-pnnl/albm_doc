.. _ModelDescription:

Scientific Description
======================

Overview
--------

ALBM includes five major modules: Water Thermal Module (WTM), Sediment Thermal Module (STM), 
Water BGC Module (WBM), Sediment BGC Module (SBM), 
and Bubble Transport Module (BTM). WTM simulates water temperature 
and ice and snow phenology. STM simulates sediment temperature and ice phenology. 
WBM simulates phytoplankton growth and respiration, heterotrophic respiration, 
oxic methane production, aerobic methane oxidation, and dissolved gas transport. 
SBM simulates anaerobic methane production, aerobic carbon decomposition, 
bubble formation, and dissolved gas transport. BTM simulates bubble transport 
in the water column. WTM & STM, WBM & BTM, and WBM & SBM are two-way coupled. 
SBM & BTM, WTM & WBM, and STM & SBM are only one-way coupled.  


Model Modules
-------------

Thermal Module
~~~~~~~~~~~~~~

The thermal module simulates heat transport through the water column and
sediments. It accounts for:

* Solar radiation penetration and absorption
* Convective mixing and turbulent diffusion
* Ice phenology (ice formation and melt)
* Sediment heat storage and conduction

Radiative Transfer Module
~~~~~~~~~~~~~~~~~~~~~~~~~

The radiative transfer module computes the downwelling shortwave and
longwave radiation reaching the lake surface and the attenuation of
solar radiation through the water column. Inputs include:

* Downwelling solar radiation (from forcing data)
* Atmospheric CO₂ and ozone concentrations
* Aerosol optical depth
* Surface albedo (ice, snow, and open water)

Carbon Cycling Module
~~~~~~~~~~~~~~~~~~~~~

The carbon module simulates the cycling of organic and inorganic carbon
in both the water column and sediments, including:

* Primary production by phytoplankton
* Decomposition of organic matter
* CO₂ production and diffusive exchange with the atmosphere
* Sediment organic carbon burial

Methane (CH₄) Module
~~~~~~~~~~~~~~~~~~~~~

The methane module represents CH₄ production in anoxic sediments, its
transport through diffusion and ebullition (bubble flux), and oxidation
in the water column. Key processes include:

* Methanogenesis in sediment layers
* Dissolved CH₄ diffusion in the water column
* Bubble nucleation and transport (ebullition)
* Aerobic CH₄ oxidation

Phytoplankton Module
~~~~~~~~~~~~~~~~~~~~~

The phytoplankton module simulates the growth and loss of phytoplankton
biomass as a function of light availability, water temperature, and
nutrient concentrations. It provides chlorophyll *a* as a model output.

Diagenesis Module
~~~~~~~~~~~~~~~~~

The diagenesis module represents early diagenesis in lake sediments,
including anaerobic decomposition, nutrient recycling, and the production
of dissolved gases (CO₂, CH₄) in pore water.

Coordinate System and Resolution
---------------------------------

ALBM uses a one-dimensional vertical coordinate. The model domain is
divided into:

* ``NWLAYER`` water-column layers (default: 50)
* ``NSLAYER`` sediment layers (default: 40)
* ``NRLAYER`` riparian/run-off layers (default: 10)

These values can be modified in the ``[resolution]`` section of the
namelist file (see :ref:`Inputs`).
