from rnn_deep_net import LSTM_Cell
import numpy as np


fget_inweight = np.ones((3, 1))
fget_hidweight = np.ones((3, 1))
fget_bias = np.ones((1, 1))
iget_inweight = np.ones((3, 1))
iget_hidweight = np.ones((3, 1))
iget_bias = np.ones((1, 1))
oget_inweight = np.ones((3, 1))
oget_hidweight = np.ones((3, 1))
oget_bias = np.ones((1, 1))
pstate = np.ones((1, 1))
cstate = np.ones((1, 1))
phid = np.ones((1, 1))
chid = np.ones((1, 1))
cin = np.ones((1, 1))
fget_act = 'tanh'
iget_act = 'tanh'
oget_act = 'sigmoid'

testlstm = LSTM_Cell.LSTMCell(fget_inweight, fget_hidweight, fget_bias, iget_inweight, iget_hidweight, iget_bias, oget_inweight, oget_hidweight, oget_bias, pstate, cstate, phid, chid, cin, fget_act, iget_act, oget_act)
# forget_weight = testlstm.get_forget_weight()
# print(forget_weight[5])
# print(testlstm.get_forget_weight())
print(np.shape(testlstm.current_input))
