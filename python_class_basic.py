# /////////////////////////// #
# Simple class example Python #
# /////////////////////////// #
import numpy as np


class complx(object):
    """Class to implement complex numbers"""

    scl = 2
    num_var = 0

    def __init__(self, a_val, b_val):
        self._a_val = a_val
        self._b_val = b_val
        complx.num_var += 1

    def __del__(self):
        print('object deleted')

    def get_vals(self):
        return self._a_val, self._b_val

    def scl_cmplx(self):
        self._a_val *= self.scl
        self._b_val *= self.scl

    def __add__(self, other):
        av, bv = other.get_vals()
        return complx(self._a_val + av, self._b_val + bv)

    # def __str__(self):
    #     return '%3.3f + i%3.3f' % (self._a_val, self._b_val)

    @classmethod
    def set_scl(cls, scl_fac):
        cls.scl = scl_fac

    @staticmethod
    def check_unity(u1, u2):
        if np.sqrt(u1**2 + u2**2) == 1:
            print('Unit number\n')
        else:
            print('Not an unit number\n')


class more_complx(complx):
    """Derived from COMPLX class"""
    def __init__(self, a_val, b_val, c_val):
        super().__init__(a_val, b_val)
        self._c_val = c_val

    def __repr__(self):
        return 'more_complx({}, {}, {})'.format(self._a_val, self._b_val, self._c_val)

    def normalize_vec(self):
        nf = np.sqrt(self._a_val**2 + self._b_val**2 + self._c_val**2)
        self._a_val *= (1 / nf)
        self._b_val *= (1 / nf)
        self._c_val *= (1 / nf)

    @property
    def vals(self):
        return 'some value'

    @property
    def get_vals(self):
        return 'aval, bval, cval'

    @vals.setter
    def vals(self, av):
        self._a_val = av[0]
        self._b_val = av[1]
        self._c_val = av[2]

    @vals.getter
    def get_vals(self):
        return self._a_val, self._b_val, self._c_val


ac = complx(2, 3)
bc = complx(4, 6)
print(ac.__doc__)

a = ac + bc
print('Sum before scaling: {}'.format(a))
print('No of complex variable created: {}'.format(a.num_var))

ac.scl = 4
ac.scl_cmplx()
bc.scl_cmplx()
b = ac + bc
print('Sum after scaling: {}'.format(b))
print('No of complex variable created: {}\n'.format(complx.num_var))

# del ac     # optional
# del bc

print('Using class methods')
a1 = complx(1, 2)
a2 = complx(5, 4)
complx.set_scl(8)
a1.scl_cmplx()
a2.scl_cmplx()
print('a1 = {}'.format(a1))
print('a2 = {}'.format(a2))
print('Sum after scaling: {}'.format(a1 + a2))
print('No of complex variable created: {}\n'.format(complx.num_var))

print('Using static method')
a1.check_unity(0.6, 0.8)

print('Using inheritance')
b1 = more_complx(5, 1, 2)

print('Before normalization b1 = {}'.format(b1))
b1.normalize_vec()
print('After normalization b1 = {}'.format(b1))
print(b1)
b1.vals = [0.1, 0.6, 0.7]                             # use decorator setter
print(b1)
print(b1.__doc__)
print(b1.get_vals)                                    # use decorator getter
