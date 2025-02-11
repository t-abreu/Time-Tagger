# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:11:22 2020

@author: liu
"""


from time import sleep
from TimeTagger import createTimeTagger, freeTimeTagger, Coincidence, Countrate,Counter

# create a Time Tagger instance
tagger = createTimeTagger()
tagger.reset()

# sets test signal to channels 1, 2, 3, 4
tagger.setTestSignal([1, 2, 3,4], True)
tagger.sync()

channels=[1,2,3,4]
print('\nTest signal is activated at channels',channels)

# run the triple-coincidence measurement
# cw = coincidence window
# play with coincidence window and notice changes in the countrate
# alternatively, introduce delays at channels [1, 2, 3] to change the result
cw = 64 # ps
coinc = Coincidence(tagger, channels, cw)
coinc_channel = coinc.getChannel()
print(f'\nCoincidence is assigned to virtual channel {coinc_channel}.')
print(f'Coincidence window is set to {cw} ps.',coinc)

# measure average countrate in counts per second on all channels
cr = Countrate(tagger, [channels,coinc_channel])
cr = Countrate(tagger, [1, 2, 3, 4, coinc_channel])
sleep(1.0) # collect data for 1 s
cr_data = cr.getData()
cr1 = cr_data[0]
cr2 = cr_data[1]
# cr3 = cr_data[2]
# cr4 = cr_data[3]
cr_coinc = cr_data[2]

# display the countrates
print(f'\nCountrate on channel 1 is {int(cr1)} cps.')
print(f'Countrate on channel 2 is {int(cr2)} cps.')
# print(f'Countrate on channel 3 is {int(cr3)} cps.')
# print(f'Countrate on channel 4 is {int(cr4)} cps.')
print(f'\nCountrate on coincidence channel is {int(cr_coinc)} cps.')

# release the Time Tagger
freeTimeTagger(tagger)