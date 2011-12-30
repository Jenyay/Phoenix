#---------------------------------------------------------------------------
# Name:        etgtools/generators.py
# Author:      Robin Dunn
#
# Created:     3-Nov-2010
# Copyright:   (c) 2011 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

"""
Just some base classes and stubs for the various generators
"""


class WrapperGeneratorBase(object):
    def __init__(self):
        pass    
    def generate(self, module, destFile=None):
        raise NotImplementedError
        
    
class DocsGeneratorBase(object):
    def __init__(self):
        pass        
    def generate(self, module):
        raise NotImplementedError
    
    
class StubbedDocsGenerator(DocsGeneratorBase):
    def generate(self, module):
        pass


class SphinxGenerator(DocsGeneratorBase):
    def generate(self, module):
        pass

#---------------------------------------------------------------------------
# helpers

def nci(text, numSpaces=0, stripLeading=True):
    """
    Normalize Code Indents
    
    First use the count of leading spaces on the first line and remove that
    many spaces from the front of all lines, and then indent each line by
    adding numSpaces spaces. This is used so we can convert the arbitrary
    indents that might be used by the tweaker code into what is expected for
    the context we are generating for.
    """
    def _getLeadingSpaceCount(line):
        count = 0
        for c in line:
            assert c != '\t', "Use spaces for indent, not tabs"
            if c != ' ':
                break
            count += 1
        return count
    
    def _allSpaces(text):
        for c in text:
            if c != ' ':
                return False
        return True

    
    lines = text.rstrip().split('\n')
    if stripLeading:
        numStrip = _getLeadingSpaceCount(lines[0])
    else:
        numStrip = 0
    
    for idx, line in enumerate(lines):
        assert _allSpaces(line[:numStrip]), "Indentation inconsistent with first line"
        lines[idx] = ' '*numSpaces + line[numStrip:]

    newText = '\n'.join(lines) + '\n'
    return newText

#---------------------------------------------------------------------------
