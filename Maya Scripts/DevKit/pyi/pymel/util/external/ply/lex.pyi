from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union
import exceptions
import sys
import re
import copy
import os
import types


"""
# -----------------------------------------------------------------------------
# ply: lex.py
#
# Copyright (C) 2001-2009,
# David M. Beazley (Dabeaz LLC)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.  
# * Redistributions in binary form must reproduce the above copyright notice, 
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.  
# * Neither the name of the David Beazley or Dabeaz LLC may be used to
#   endorse or promote products derived from this software without
#  specific prior written permission. 
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------
"""


if False:
    from typing import Dict, List, Tuple, Union, Optional

class NullLogger(object):
    """
    # Null logger is used when no output is generated. Does nothing.
    """
    
    
    
    def __call__(self, *args, **kwargs): ...
    def __getattribute__(self, name): ...
    __dict__ : dictproxy
    
    __weakref__ : getset_descriptor


class LexToken(object):
    """
    # Token class.  This class is used to represent the tokens produced.
    """
    
    
    
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    __dict__ : dictproxy
    
    __weakref__ : getset_descriptor


class LexError(exceptions.Exception):
    def __init__(self, message, s): ...
    __weakref__ : getset_descriptor


class PlyLogger(object):
    def __init__(self, f): ...
    def critical(self, msg, *args, **kwargs): ...
    def debug(self, msg, *args, **kwargs): ...
    def error(self, msg, *args, **kwargs): ...
    def info(self, msg, *args, **kwargs): ...
    def warning(self, msg, *args, **kwargs): ...
    __dict__ : dictproxy
    
    __weakref__ : getset_descriptor


class Lexer:
    def __init__(self): ...
    def __iter__(self):
        """
        # Iterator interface
        """
        ...
    def __next__(self): ...
    def begin(self, state):
        """
        # ------------------------------------------------------------
        # begin() - Changes the lexing state
        # ------------------------------------------------------------
        """
        ...
    def clone(self, object='None'): ...
    def current_state(self):
        """
        # ------------------------------------------------------------
        # current_state() - Returns the current lexing state
        # ------------------------------------------------------------
        """
        ...
    def input(self, s):
        """
        # ------------------------------------------------------------
        # input() - Push a new string into the lexer
        # ------------------------------------------------------------
        """
        ...
    def next(self): ...
    def pop_state(self):
        """
        # ------------------------------------------------------------
        # pop_state() - Restores the previous state
        # ------------------------------------------------------------
        """
        ...
    def push_state(self, state):
        """
        # ------------------------------------------------------------
        # push_state() - Changes the lexing state and saves old on stack
        # ------------------------------------------------------------
        """
        ...
    def readtab(self, tabfile, fdict):
        """
        # ------------------------------------------------------------
        # readtab() - Read lexer information from a tab file
        # ------------------------------------------------------------
        """
        ...
    def skip(self, n):
        """
        # ------------------------------------------------------------
        # skip() - Skip ahead n characters
        # ------------------------------------------------------------
        """
        ...
    def token(self):
        """
        # ------------------------------------------------------------
        # opttoken() - Return the next token from the Lexer
        #
        # Note: This function has been carefully implemented to be as fast
        # as possible.  Don't make changes unless you really know what
        # you are doing
        # ------------------------------------------------------------
        """
        ...
    def writetab(self, tabfile, outputdir="''"):
        """
        # ------------------------------------------------------------
        # writetab() - Write lexer information to a table file
        # ------------------------------------------------------------
        """
        ...


class LexerReflect(object):
    """
    # -----------------------------------------------------------------------------
    # LexerReflect()
    #
    # This class represents information needed to build a lexer as extracted from a
    # user's input file.
    # -----------------------------------------------------------------------------
    """
    
    
    
    def __init__(self, ldict, log='None', reflags='0'): ...
    def get_all(self):
        """
        # Get all of the basic information
        """
        ...
    def get_literals(self):
        """
        # Get the literals specifier
        """
        ...
    def get_rules(self): ...
    def get_states(self): ...
    def get_tokens(self):
        """
        # Get the tokens map
        """
        ...
    def validate_all(self):
        """
        # Validate all of the information
        """
        ...
    def validate_file(self, filename): ...
    def validate_literals(self):
        """
        # Validate literals
        """
        ...
    def validate_rules(self):
        """
        # Validate all of the t_rules collected
        """
        ...
    def validate_tokens(self):
        """
        # Validate the tokens
        """
        ...
    __dict__ : dictproxy
    
    __weakref__ : getset_descriptor




def input(self, s):
    """
    # ------------------------------------------------------------
    # input() - Push a new string into the lexer
    # ------------------------------------------------------------
    """
    ...
def runmain(lexer='None', data='None'): ...
def get_caller_module_dict(levels): ...
def token(self):
    """
    # ------------------------------------------------------------
    # opttoken() - Return the next token from the Lexer
    #
    # Note: This function has been carefully implemented to be as fast
    # as possible.  Don't make changes unless you really know what
    # you are doing
    # ------------------------------------------------------------
    """
    ...
def _statetoken(s, names): ...
def TOKEN(r): ...
def _form_master_re(relist, reflags, ldict, toknames): ...
def _names_to_funcs(namelist, fdict): ...
def _funcs_to_names(funclist, namelist): ...
def lex(module='None', object='None', debug='0', optimize='0', lextab="'lextab'", reflags='0', nowarn='0', outputdir="''", debuglog='None', errorlog='None'):
    """
    # -----------------------------------------------------------------------------
    # lex(module)
    #
    # Build all of the regular expression rules from definitions in the supplied module
    # -----------------------------------------------------------------------------
    """
    ...
def func_code(f): ...


lexer : Lexer
__version__ : str
_is_identifier : re.SRE_Pattern
StringTypes : tuple

