.. _open_apdl:

Opening APDL
========================

Opening APDL through workbench uses the shared license, so you can't modify a mechanical session while using APDL. This script writes the input file and gives the commands to open the file in apdl.
 
.. code-block:: python

    apdldir = "C:\\scratch\\APDL\\"
    executable = r'C:\Program Files\ANSYS Inc\v240\ansys\bin\winx64\mapdl'

    import datetime
    import os

    def get_analysis():
        return _get_analysis(ExtAPI.DataModel.Tree.ActiveObjects[0])

    def _get_analysis(obj):
        if obj.GetType() == Ansys.ACT.Automation.Mechanical.Analysis:
        return obj
        if hasattr(obj, "Parent"):
        return _get_analysis(obj.Parent)
        raise ValueError("no workingdir or parent for selecteditem")

    now = datetime.datetime.now().strftime('%Y-%m-%d--%I-%M')
    apdldir = apdldir+now
    os.system("mkdir -p "+apdldir)

    print(r"""
    cd {}
    "{}" -g -lch -p prepost ^
    -dir "{}" ^
    -j file -l en-us -d win32 -s noread -dis -mip INTELMPI -np 4
    """.format(apdldir, executable, apdldir))

    print("/INPUT, 'input', 'dat',")

    analysis = get_analysis()
    analysis.WriteInputFile(apdldir+"\\input.dat")

