# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ciglesia <ciglesia@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/04 23:03:36 by ciglesia          #+#    #+#              #
#    Updated: 2020/09/05 00:19:32 by ciglesia         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import collections.abc, itertools, operator, __future__

class MetaClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kw):
        return (collections.OrderedDict())

    def __new__(cls, name, bases, namespace, **kw):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return (result)

class Polynomial(metaclass=MetaClass):
	"""docstring for Polynomial"""

	class _expression(collections.abc.MutableMapping):
		"""docstring for _expression"""
		def __init__(self, exp):
			super(collections.MutableMapping, self).__init__(exp)


	def __init__(self, *args):
            super(Polynomial, self).__init__(*args)
            #self.expression = self._expression(*args)

            def __convert_format(): pass

	"""
	Polynomial method's docstring
	"""

# 1 + 2x + 3x^2 + 5x^4 + 9x^7
p = Polynomial()
p = Polynomial([1, 2, 3, 0, 5, 0, 0, 9])
p = Polynomial(1, 2, 3, 0, 5, 0, 0, 9)
p = Polynomial({1:0, 2:1, 3:2, 5:4, 9:7})
p = Polynomial('1 + 2x + 3x^2 + 5x^4 + 9x^7')
