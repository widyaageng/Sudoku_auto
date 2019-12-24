import numpy as np


class LSTMCell:
    def __init__(
            self,
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
            activated_forget_ft,
            activated_input_it,
            activated_output_ot,
    ):
        self.forget_input_weight_wf = forget_input_weight_wf
        self.forget_hidden_weight_uf = forget_hidden_weight_uf
        self.forget_bias_bf = forget_bias_bf
        self.input_input_weight_wi = input_input_weight_wi
        self.input_hidden_weight_ui = input_hidden_weight_ui
        self.input_bias_bi = input_bias_bi
        self.output_input_weight_wo = output_input_weight_wo
        self.output_hidden_weight_wo = output_hidden_weight_wo
        self.output_bias_bo = output_bias_bo
        self.previous_state = previous_state
        self.current_state = current_state
        self.previous_hidden = previous_hidden
        self.current_hidden = current_hidden
        self.activated_forget_ft = activated_forget_ft
        self.activated_input_it = activated_input_it
        self.activated_output_ot = activated_output_ot

    def get_forget_weight(self):
        return self.forget_input_weight_wf, self.forget_hidden_weight_uf, self.forget_bias_bf


LSTM_unit = LSTMCell(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(LSTM_unit.get_forget_weight())