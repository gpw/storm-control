#!/usr/bin/python
#
# Camera class for controlling a single (non-detached) camera.
#
# Hazen 11/12
#

from PyQt4 import QtCore, QtGui

# Debugging
import halLib.hdebug as hdebug

# UIs
import qtdesigner.camera_display_ui as cameraDisplayUi
import qtdesigner.camera_params_ui as cameraParamsUi

import camera.singleCamera as singleCamera
import camera.cameraDisplay as cameraDisplay
import camera.cameraParams as cameraParams

class ClassicSingleCamera(singleCamera.SingleCamera):

    @hdebug.debug
    def __init__(self, parameters, camera_frame, camera_params_frame, parent = None):
        singleCamera.SingleCamera.__init__(self, parameters, parent)

        camera_display_ui = cameraDisplayUi.Ui_Frame()
        self.camera_display = cameraDisplay.CameraDisplay(parameters,
                                                          camera_display_ui,
                                                          "camera1",
                                                          show_record_button = True,
                                                          show_shutter_button = True,
                                                          parent = camera_frame)

        camera_params_ui = cameraParamsUi.Ui_GroupBox()
        self.camera_params = cameraParams.CameraParams(camera_params_ui,
                                                       parent = camera_params_frame)
            
        # Connect ui elements.
        self.camera_display.ui.cameraShutterButton.clicked.connect(self.toggleShutter)
        self.camera_params.gainChange.connect(self.handleGainChange)

#
# The MIT License
#
# Copyright (c) 2012 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
