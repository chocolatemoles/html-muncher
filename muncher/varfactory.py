#!/usr/bin/env python
# Copyright 2011 Craig Campbell
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math

class VarFactory:
    """class to keep multiple counters and turn numeric counters into alphabetical ones"""
    types = {}
    letters = map(chr, range(97, 123))

    @staticmethod
    def getNext(type):
        """gets the next letter name based on counter name

        Arguments:
        type -- name of counter we want the next value for

        Returns:
        string

        """
        i = VarFactory.getVersion(type)
        return VarFactory.getSmallName(i)

    @staticmethod
    def getVersion(type):
        """gets the next number in the counter for this type

        Arguments:
        type -- name of counter we are incrementing

        Resturns:
        int

        """
        if not type in VarFactory.types:
            VarFactory.types[type] = 0
            return 0

        VarFactory.types[type] += 1

        return VarFactory.types[type]

    @staticmethod
    def getSmallName(index):
        a = int(index) + 1

        if a < 27:
            return chr(a + 96)
            
        elif a < 702:
            b = 0
            while a > 26:
                b += 1
                a = a - 26

            b = chr(b + 96)
            a = chr(a + 96)
            return b + a
            
        else:    
            b = 0        
            c = 0
            while a > 26:
                b += 1
                a = a - 26

            while b > 26:
                c += 1
                b = b - 26
                
            c = chr(c + 96)
            b = chr(b + 96)
            a = chr(a + 96)
            return c + b + a
