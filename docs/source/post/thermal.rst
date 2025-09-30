.. _thermal:

Plotting Thermal Results
========================

There's a pdf or video showing how to use the worksheet to select the SURF152_ or SURF252_ elements in the results file, and plot the nmisc and smisc results. I searched for 10 minutes and couldn't find it. Here's a script to create the results without a million clicks and looking back and forth between two tables in the help.


SURF152_ is the default ETYPE for convection and radiation to ambient.

SURF252_ is the default ETYPE for surface to surface radiation. 



.. collapse:: SURF152 Result Table

    =======================   =============================   ===========================================================   ==========
    Output Quantity           ETABLE and ESOL Command Input   Definition                                                    Unit
    =======================   =============================   ===========================================================   ==========
    HGTOT                     SMISC1                          Heat generation rate over entire element                      W
    HFCTOT                    SMISC2                          Convection heat flow rate over element area                   W
    HRTOT                     SMISC3                          Radiation heat flow rate over entire element                  W
    AREA                      NMISC1                          Surface area                                                  m²
    VNX                       NMISC2                          X component of unit normal vector                             -
    VNY                       NMISC3                          Y component of unit normal vector                             -
    VNZ                       NMISC4                          Z component of unit normal vector                             -
    HFILM                     NMISC5                          Film coefficient at each face node                            W/m²K
    TAVG                      NMISC6                          Average surface temperature                                   K
    TBULK                     NMISC7                          Bulk temperature at each face node                            K
    TAW                       NMISC8                          Adiabatic wall temperature                                    K
    RELVEL                    NMISC9                          Relative velocity                                             m/s
    SPHTFL                    NMISC10                         Specific heat of the fluid                                    J/kgK
    RECFAC                    NMISC11                         Recovery factor                                               -
    EMISSUR                   NMISC12                         Average emissivity of surface                                 -
    EMISEXT                   NMISC13                         Emissivity of extra node                                      -
    TEMPSUR                   NMISC14                         Average temperature of surface                                K
    TEMPEXT                   NMISC15                         Temperature of extra node                                     K
    FORM FACTOR               NMISC16                         Average form factor of element                                -
    DENS                      NMISC17                         Density                                                       kg/m³
    MASS                      NMISC18                         Mass of element                                               kg
    EL                        -                               Element Number                                                -
    SURFACE NODES             -                               Nodes - I, J, K, L                                            -
    EXTRA NODE                -                               Extra node (if present)                                       -
    MAT                       -                               Material number                                               -
    VOLU                      -                               Volume                                                        m³
    XC, YC, ZC                -                               Location where results are reported                           m
    CONV. HEAT RATE/AREA      SMISC2 / NMISC1                 Average convection heat flow rate per unit area               W/m²
    RAD. HEAT RATE/AREA       SMISC3 / NMISC1                 Average radiation heat flow rate per unit area                W/m²
    =======================   =============================   ===========================================================   ==========

.. collapse:: SURF252 Result Table


    https://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_elem/Hlp_E_SURF252.html

    ======================================= ============================= ========================================================= ==========
    Output Quantity                         ETABLE and ESOL Command Input  Definition                                               Unit
    ======================================= ============================= ========================================================= ==========
    CENTROID X                              NMISC1                        X coordinate of element centroid                          m
    CENTROID Y                              NMISC2                        Y coordinate of element centroid                          m
    CENTROID Z                              NMISC3                        Z coordinate of element centroid                          m
    AREA                                    NMISC4                        Surface area                                              m²
    TEMP                                    NMISC5                        Temperature                                               K
    EMISSIVITY                              NMISC6                        Emissivity                                                -
    Net outgoing radiation per unit area    NMISC7                        Net outgoing radiation heat flux per unit area            W/m²
    Emitted radiation per unit area         NMISC8                        Emitted radiation heat flux per unit area                 W/m²
    Reflected radiation per unit area       NMISC9                        Reflected radiation heat flux per unit area               W/m²
    Incident radiation per unit area        NMISC10                       Incident radiant heat flux per unit area                  W/m²
    Net outgoing radiation                  NMISC7 * NMISC4               Net outgoing radiation heat flux × area                   W
    Emitted radiation                       NMISC8 * NMISC4               Emitted radiation heat flux × area                        W
    Reflected radiation                     NMISC9 * NMISC4               Reflected radiation heat flux × area                      W
    Incident radiation                      NMISC10 * NMISC4              Incident radiant heat flux × area                         W
    Enclosure No.                           NMISC18                       Enclosure number                                          -
    ======================================= ============================= ========================================================= ==========
 
.. code-block:: python

    analysis_index = 0  # First analysis in the project
    # List of plot names to generate; comment out any you don't want
    selected_plot_names = [

        # SURF 151
        "Convection Heat Flow Rate [W]",
       # "Radiation Heat Flow Rate [W]",
       # "Average Surface Temperature [K]",
        "Bulk Temperature [K]",
      #  "Adiabatic Wall Temperature [K]",
      #  "Relative Velocity [m/s]",
      #  "Specific Heat of Fluid [J/kgK]",
      #  "Recovery Factor [-]",
      #  "Average Emissivity of Surface [-]",
      #  "Emissivity of Extra Node [-]",
      #  "Average Temperature of Surface [K]",
      #  "Temperature of Extra Node [K]",
      #  "Average Form Factor of Element [-]",
      #  "Density [kg/m³]",
      #  "Mass of Element [kg]",
        "Convection Heat Rate per Area [W/m²]",
      #  "Radiation Heat Rate per Area [W/m²]",
        "Heat Transfer Coefficient [W/m²K]",

        # SURF 252
        "Emissivity [-]",
        "Enclosure Number [-]",
        "Net outgoing radiation heat flux [W/m²]",
      #  "Emitted radiation heat flux [W/m²]",
      #  "Reflected radiation heat flux [W/m²]",
      #  "Incident radiant heat flux [W/m²]",
      #  "Net outgoing radiation [W]",
      #  "Emitted radiation [W]",
      #  "Reflected radiation [W]",
      #  "Incident radiant [W]",
    ]

    ##################################################

    # solution = ExtAPI.DataModel.Tree.FirstActiveObject
    solution = ExtAPI.DataModel.Project.Model.Analyses[analysis_index].Solution

    plots = [
        {
            "Name": "Convection Heat Flow Rate [W]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'smisc2',
        },
        {
            "Name": "Radiation Heat Flow Rate [W]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'smisc3',
        },
        {
            "Name": Heat Transfer Coefficient [W/m²K]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc5',
        },
        {
            "Name": "Average Surface Temperature [K]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc6',
        },
        {
            "Name": "Bulk Temperature [K]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc7',
        },
        {
            "Name": "Adiabatic Wall Temperature [K]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc8',
        },
        {
            "Name": "Relative Velocity [m/s]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc9',
        },
        {
            "Name": "Specific Heat of Fluid [J/kgK]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc10',
        },
        {
            "Name": "Recovery Factor [-]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc11',
        },
        {
            "Name": "Average Emissivity of Surface [-]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc12',
        },
        {
            "Name": "Emissivity of Extra Node [-]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc13',
        },
        {
            "Name": "Average Temperature of Surface [K]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc14',
        },
        {
            "Name": "Temperature of Extra Node [K]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc15',
        },
        {
            "Name": "Average Form Factor of Element [-]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc16',
        },
        {
            "Name": "Density [kg/m³]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc17',
        },
        {
            "Name": "Mass of Element [kg]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'nmisc18',
        },
        {
            "Name": "Convection Heat Rate per Area [W/m²]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'smisc2/nmisc1',
        },
        {
            "Name": "Radiation Heat Rate per Area [W/m²]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF152',
            "Expression": r'smisc3/nmisc1',
        },
    ]

    plots.extend([
        {
            "Name": "Emissivity [-]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc6',
        },
        {
            "Name": "Enclosure Number [-]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc18',
        },
        {
            "Name": "Net outgoing radiation heat flux [W/m²]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc7',
        },
        {
            "Name": "Emitted radiation heat flux [W/m²]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc8',
        },
        {
            "Name": "Reflected radiation heat flux [W/m²]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc9',
        },
        {
            "Name": "Incident radiant heat flux [W/m²]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc10',
        },
        {
            "Name": "Net outgoing radiation [W]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc7*nmisc4',
        },
        {
            "Name": "Emitted radiation [W]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc8*nmisc4',
        },
        {
            "Name": "Reflected radiation [W]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc9*nmisc4',
        },
        {
            "Name": "Incident radiant [W]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": 'SURF252',
            "Expression": r'nmisc10*nmisc4',
        },
    ])

    with Transaction():
        for plot in plots:
            if plot["Name"] not in selected_plot_names:
                continue
            user_defined_result = solution.AddUserDefinedResult()
            for key, value in plot.items():
                setattr(user_defined_result, key, value)
            # I don't know why this isn't set by the loop above
            user_defined_result.SolverComponentIDs = plot['SolverComponentIDs']

.. code-block:: python

    # Explicit example without loop
    user_defined_result = solution.AddUserDefinedResult()
    user_defined_result.ScopingMethod = GeometryDefineByType.ResultFileItem
    user_defined_result.ItemType = ResultFileItemType.ElementNameIDs
    user_defined_result.SolverComponentIDs = 'SURF152'
    user_defined_result.Expression = r'nmisc5'



.. _SURF152: https://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_elem/Hlp_E_SURF152.html
.. _SURF252: https://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_elem/Hlp_E_SURF252.html