import zope.interface

class IName(zope.interface.Interface):
    @property
    def name(self):
        pass

class ISurname(zope.interface.Interface):
    @property
    def surname(self):
        pass


class foo(ISurname):
    zope.interface.implements(ISurname)







