from rnn_deep_net import LSTM_Cell
import numpy as np


fget_inweight = np.ones((3, 1))
fget_hidweight = np.ones((3, 1))
fget_bias = 1

iget_inweight = np.ones((3, 1))
fget_hidweight = np.ones((3, 1))
fget_bias = 1

forget_input_weight_wf,
forget_hidden_weight_uf,
forget_bias_bf,
input_input_weight_wi,
input_hidden_weight_ui,
input_bias_bi,
output_input_weight_wo,
output_hidden_weight_wo,
output_bias_bo,
previous_state,
current_state,
previous_hidden,
current_hidden,
current_input,
activated_forget_ft,
activated_input_it,
activated_output_ot,