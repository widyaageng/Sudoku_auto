from util import act_sigmoid
import numpy as np

test = [i for i in range(10)]
test = [test for i in range(10)]
print(test)
test = np.array(test)
print(test)
dumtest = act_sigmoid.sigmoid(test)
print(dumtest)
print(dumtest.shape)
