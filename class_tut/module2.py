

class A(object):
    """Talk about A"""

    class_att = "hi"

    def __init__(self, var1=None):
        self.var1 = var1

    def amethod(self):
        return str(self.var1)

    @classmethod
    def clsmethod(cls):
        return cls.class_att

    @classmethod
    def alterninit(cls):
        return object.__new__(cls)

    @staticmethod
    def namespacing():
        return True

    @property
    def vartwice(self):
        return f"{self.var1} {self.var1}"

    def abstract_interface(self, in1=None):
        raise NotImplementedError

    def __repr__(self):
        return (
            f"class: {type(self)}\n"
            f"mydict: {self.__dict__}\n"
            f"classdiict: {type(self).__dict__}"
        )


class B(A):
    """Talk about B"""

    class_att = "world"

    def abstract_interface(self, in1=1):
        return in1
