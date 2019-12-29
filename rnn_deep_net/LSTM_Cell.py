import numpy as np


class LSTMCell:
    #
    # # utilitites to determine the parameter type
    # weight_callname_dict = {
    #     0: 'forget',
    #     1: 'input',
    #     2: 'output'
    # }

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
        def check_dim(self, some_function):
            try:
                assert (np.shape(some_function(self)[1])[1] == np.shape(self.current_input)[0])
                assert (np.shape(some_function(self)[1])[2] == np.shape(self.previous_hidden)[0])
                assert (np.shape(some_function(self)[1])[3] == np.shape(some_function(self)[1])[0])
                wrapped_function
            except AssertionError:
                print('Dimension mismatch in %s constructor!' % some_function[0])

        return check_dim(wrapped_function)

    @dim_check
    def get_forget_weight(self):
        return 'forget', self.forget_input_weight_wf, self.forget_hidden_weight_uf, self.forget_bias_bf

    @dim_check
    def get_input_weight(self):
        return 'input', self.input_input_weight_wi, self.input_hidden_weight_ui, self.input_bias_bi

    @dim_check
    def get_output_weight(self):
        return 'output', self.output_input_weight_wo, self.output_hidden_weight_wo, self.output_bias_bo


