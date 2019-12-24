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
            current_input,
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
        self.current_input = current_input
        self.activated_forget_ft = activated_forget_ft
        self.activated_input_it = activated_input_it
        self.activated_output_ot = activated_output_ot




    def dim_check(wrapped_function):
        def check_dim(self):
            try:
                assert (np.shape(self.forget_input_weight_wf)[1] == np.shape(self.current_input)[0])
                assert (np.shape(self.forget_hidden_weight_uf)[1] == np.shape(self.previous_hidden)[0])
                assert (np.shape(self.forget_bias_bf)[1] == np.shape(self.forget_input_weight_wf)[0])
                wrapped_function
            except AssertionError:
                print('Dimension mismatch in \'forget\' constructor!')
        return check_dim()

    @dim_check
    def get_forget_weight(self):
        return self.forget_input_weight_wf, self.forget_hidden_weight_uf, self.forget_bias_bf

    @dim_check
    def get_input_weight(self):
        return self.input_input_weight_wi, self.input_hidden_weight_ui, self.input_bias_bi

    @dim_check
    def get_output_weight(self):
        return self.output_input_weight_wo, self.output_hidden_weight_wo, self.output_bias_bo


