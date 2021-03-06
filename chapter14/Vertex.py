#encoding:UTF-8

########################################################################
class Vertex(object):
    """"""
    __slots__ = '_element'
    
    #----------------------------------------------------------------------
    def __init__(self, x):
        """Constructor"""
        self._element = x
    
    #----------------------------------------------------------------------
    def element(self):
        """"""
        return self._element
    
    #----------------------------------------------------------------------
    def __hash__(self):
        """"""
        return hash(id(self))
    