from rnn_deep_net import LSTM_Cell
import numpy as np


fget_inweight = np.ones((3, 1))
fget_hidweight = np.ones((3, 1))
fget_bias = 1
iget_inweight = np.ones((3, 1))
iget_hidweight = np.ones((3, 1))
iget_bias = 1
oget_inweight = np.ones((3, 1))
oget_hidweight = np.ones((3, 1))
oget_bias = 1
pstate = 1
cstate = 1
phid = 1
chid = 1
cin = 1
fget_act = 'tanh'
iget_act = 'tanh'
oget_act = 'sigmoid'

testlstm = LSTM_Cell.LSTMCell(fget_inweight, fget_hidweight, fget_bias, iget_inweight, iget_hidweight, iget_bias, oget_inweight, oget_hidweight, oget_bias, pstate, cstate, phid, chid, cin, fget_act, iget_act, oget_act)
forget_weight = testlstm.get_forget_weight()
print(forget_weight[5])