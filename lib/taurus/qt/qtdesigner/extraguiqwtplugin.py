# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guiqwt/__init__.py for details)

"""
guiqwtplugin
============

guiqwt widgets plugins for Qt Designer
"""

from guiqwt.qtdesigner import create_qtdesigner_plugin

PlotPlugin = create_qtdesigner_plugin("guiqwt", "guiqwt.plot", "CurveWidget",
                                  icon="curve.png")

ImagePlotPlugin = create_qtdesigner_plugin("guiqwt", "guiqwt.plot", "ImageWidget",
                                  icon="image.png")