import ray
# from deep_lfd.learning_driving.deep_learner import *
from gym_driving.envs.agents.dart_agent import *

class RayDartAgent(DartAgent):

	"""Wrapper Class for enabling ease of weight transfer"""

	def __init__(self, *args):
		super(RayDartAgent, self).__init__(*args)

		# loss = self.learner.net.loss
		# sess = self.learner.net.sess

		# self.variables = ray.experimental.TensorFlowVariables(loss, sess)

	def get_weights(self):
		return self.variables.get_weights()

	def set_weights(self, weights):
		self.variables.set_weights(weights)

	def get_params(self):
		pass

	def set_params(self,params):
		#self.iterations = params[0]
		self.eps = params[0]
		#self.alg_type = params[2]

