#!/usr/bin/env python
"""
The HAL testing module, basically this just sends messages
to HAL and verifies that response / behavior is correct.

Testing is done by sub-classing this module and providing
it with a series of test actions, a little bit like what
Dave does when controlling HAL.

Hazen 04/17
"""

import storm_control.hal4000.halLib.halMessage as halMessage
import storm_control.hal4000.halLib.halModule as halModule


class Testing(halModule.HalModule):

    def __init__(self, module_params = None, qt_settings = None, **kwds):
        super().__init__(**kwds)

        self.all_modules = None
        self.current_action = None
        self.test_actions = []

        #
        # This message is not actually sent, it is just the default
        # message filter name for a test action. It keeps HalMessage.isType()
        # from complaining that the message does not exist.
        #
        halMessage.addMessage("na",
                              validator = {"data" : None, "resp" : None})

    def handleActionDone(self):

        #
        # If there are no more actions, spoof the 'close event' message
        # from 'hal' to finish up.
        #
        if (len(self.test_actions) == 0):
            self.newMessage.emit(halMessage.HalMessage(source = self.all_modules["hal"],
                                                       m_type = "close event"))

        #
        # Otherwise start the next action.
        #
        else:            
            if self.current_action is not None:
                self.current_action.actionDone.disconnect()
            self.current_action = self.test_actions[0]
            self.current_action.actionDone.connect(self.handleActionDone)
            self.test_actions = self.test_actions[1:]
            self.newMessage.emit(halMessage.HalMessage(source = self.all_modules[self.current_action.getSourceName()],
                                                       m_type = self.current_action.getMessageType(),
                                                       data = self.current_action.getMessageData()))

    def handleResponses(self, message):

        if message.isType(self.current_action.getResponseFilter()):
            self.current_action.handleResponses(message)

    def processL1Message(self, message):

        if message.isType("start"):
            self.handleActionDone()

        if self.current_action is not None:
            if message.isType(self.current_action.getMessageFilter()):
                self.current_action.handleMessage(message)