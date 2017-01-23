#!/usr/bin/python
#
## @file
#
# QPD / Objective Z based focus lock 
# control specialized for STORM3.
#
# Hazen 3/12
#

import storm_control.sc_library.parameters as params

# qpd, stage and motor.
import storm_control.sc_hardware.madCityLabs.mclController as mclController
import storm_control.sc_hardware.thorlabs.uc480Camera as uc480Cam
#import phreshPhotonics.phreshQPD as phreshQPD
#import prior.prior as prior

# focus lock control thread.
import storm_control.hal4000.focuslock.stageOffsetControl as stageOffsetControl

# ir laser control
import storm_control.sc_hardware.thorlabs.LDC210 as LDC210

# focus lock dialog.
import storm_control.hal4000.focuslock.focusLockZ as focusLockZ

#
# Focus Lock Dialog Box specialized for STORM3
# with Phresh QPD and MCL objective Z positioner.
#
class AFocusLockZ(focusLockZ.FocusLockZCam):
    def __init__(self, hardware, parameters, parent = None):

        # STORM3 specific focus lock parameters
        lock_params = parameters.addSubSection("focuslock")
        lock_params.add("qpd_zcenter", params.ParameterRangeFloat("Piezo center position in microns",
                                                                  "qpd_zcenter",
                                                                  50.0, 0.0, 100.0))
        lock_params.add("qpd_scale", params.ParameterRangeFloat("Offset to nm calibration value",
                                                                "qpd_scale",
                                                                50.0, 0.1, 1000.0))
        lock_params.add("qpd_sum_min", 50.0)
        lock_params.add("qpd_sum_max", 256.0)
        lock_params.add("is_locked_buffer_length", 10)
        lock_params.add("is_locked_offset_thresh", 0.01)
        lock_params.add("ir_power", params.ParameterInt("", "ir_power", 6, is_mutable = False))

        # STORM3 Initialization.
        cam = uc480Cam.CameraQPD(camera_id = 1, 
                                 x_width = 200, 
                                 y_width = 50, 
                                 offset_file = "cam_offsets_storm3_1.txt")

        stage = mclController.MCLStage("c:/Program Files/Mad City Labs/NanoDrive/")
        lock_fn = lambda (x): -0.02 * x
        control_thread = stageOffsetControl.StageCamThread(cam,
                                                           stage,
                                                           lock_fn,
                                                           lock_params.get("qpd_sum_min"),
                                                           lock_params.get("qpd_zcenter"),
                                                           lock_params.get("is_locked_buffer_length"),
                                                           lock_params.get("is_locked_offset_thresh"))

        #ir_laser = LDC210.LDC210("PCI-6722", 1)
        ir_laser = LDC210.LDC210PWMNI("PCI-MIO-16E-4", 0)
        focusLockZ.FocusLockZCam.__init__(self,
                                          parameters,
                                          control_thread,
                                          ir_laser,
                                          parent)


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
