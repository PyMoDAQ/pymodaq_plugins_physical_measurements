## To modify by developper(s) of the plugin
SHORT_PLUGIN_NAME = 'physical_measurements'  #for instance daqmx
package_url = 'https://github.com/CEMES-CNRS/pymodaq_plugins_physical_measurements' #to modify
description = 'Set of PyMoDAQ plugins for various physical measurements: multimeter, lockin, oscilloscope, indus cameras...'



author = 'Sébastien Weber'
author_email = 'sebastien.weber@cemes.fr'

#packages required for your plugin:
packages_required = ['pyvisa',
                     'bitstring',
                     'opencv-python',
                     #'harvesters', #for genicam compliant cameras
                 ]
##