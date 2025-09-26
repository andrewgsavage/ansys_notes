.. _thermal:

Thermal Analysis
================

Convection
----------



.. code-block:: python

    solution = ExtAPI.DataModel.AnalysisManager.Analyses[0].Solution
    solution = ExtAPI.DataModel.Tree.FirstActiveObject

    plots = [
        {
            "Name": "Heat Transfer Coefficient [W/m²K]",
            "ScopingMethod": GeometryDefineByType.ResultFileItem,
            "ItemType": ResultFileItemType.ElementNameIDs,
            "SolverComponentIDs": r'SURF152',
            "Expression": r'nmisc5',

    ]

    user_defined_result = solution.AddUserDefinedResult()
    for plot in plots:
        for key, value in plot.items():
            setattr(user_defined_result, key, value)

    user_defined_result.ScopingMethod = GeometryDefineByType.ResultFileItem
    user_defined_result.ItemType = ResultFileItemType.ElementNameIDs
    user_defined_result.SolverComponentIDs = r'SURF152'
    user_defined_result.Expression = r'nmisc5'
