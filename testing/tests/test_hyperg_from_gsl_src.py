#!/usr/bin/env python
# WARNING: Automatically generated file: do not edit!
#          Edited the generated source instead.
#
# Tests converted from GSL Source directory.
# Original license:
# /* specfunc/test_hyperg.c
# /* specfunc/test_hyperg.c
#  *
#  * Copyright (C) 2007, 2009, 2010 Brian Gough
#  * Copyright (C) 1996, 1997, 1998, 1999, 2000, 2004 Gerard Jungman
#  *
#  * This program is free software; you can redistribute it and/or modify
#  * it under the terms of the GNU General Public License as published by
#  * the Free Software Foundation; either version 3 of the License, or (at
#  * your option) any later version.
#  *
#  * This program is distributed in the hope that it will be useful, but
#  * WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  * General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along with this program; if not, write to the Free Software
#  * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#  */

import unittest
import pytest
import pygsl.testing.sf as sf

import sf_test_basis
from sf_test_basis import *
_test_sf_automatic = sf_test_basis._test_sf_automatic
_t_func = None
try:
    _t_func = sf.hyperg_0F1_e
except AttributeError:
    print("Not including tests for hyperg_0F1_e")

if _t_func != None:
    class test_sf_automatic_hyperg_0F1_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_0F1_e, (1, 0.5, &r),     1.5660829297563505373, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 0.5), ('1.5660829297563505373', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_0F1_e, (5, 0.5, &r),     1.1042674404828684574, TEST_TOL1, GSL_SUCCESS)'
            self._test((5, 0.5), ('1.1042674404828684574', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_0F1_e, (100, 30, &r),    1.3492598639485110176, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 30), ('1.3492598639485110176', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_0F1_e, (-0.5, 3, &r),   -39.29137997543434276,  TEST_TOL1, GSL_SUCCESS)'
            self._test((-0.5, 3), ('-39.29137997543434276', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_0F1_e, (-100.5, 50, &r), 0.6087930289227538496, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100.5, 50), ('0.6087930289227538496', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args5_1(self):
            '(s, gsl_sf_hyperg_0F1_e, (1, -5.0, &r),   -0.3268752818235339109, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, -5.0), ('-0.3268752818235339109', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args6_1(self):
            '(s, gsl_sf_hyperg_0F1_e, (-0.5, -5.0, &r),-4.581634759005381184,  TEST_TOL1, GSL_SUCCESS)'
            self._test((-0.5, -5.0), ('-4.581634759005381184', 'TEST_TOL1'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_1F1_e
except AttributeError:
    print("Not including tests for hyperg_1F1_e")

if _t_func != None:
    class test_sf_automatic_hyperg_1F1_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.5, 1, &r), 2.0300784692787049755, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1.5, 1), ('2.0300784692787049755', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.5, 10, &r),  6172.859561078406855, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1.5, 10), ('6172.859561078406855', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.5, 100, &r),  2.3822817898485692114e+42, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 1.5, 100), ('2.3822817898485692114e+42', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.5, 500, &r),  5.562895351723513581e+215, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, 1.5, 500), ('5.562895351723513581e+215', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1.5, 2.5, 1, &r), 1.8834451238277954398, TEST_TOL0, GSL_SUCCESS)'
            self._test((1.5, 2.5, 1), ('1.8834451238277954398', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args5_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1.5, 2.5, 10, &r),  3128.7352996840916381, TEST_TOL1, GSL_SUCCESS)'
            self._test((1.5, 2.5, 10), ('3128.7352996840916381', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args6_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 1.1, 1, &r),  110.17623733873889579, TEST_TOL1, GSL_SUCCESS)'
            self._test((10, 1.1, 1), ('110.17623733873889579', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args7_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 1.1, 10, &r),  6.146657975268385438e+09, TEST_TOL1, GSL_SUCCESS)'
            self._test((10, 1.1, 10), ('6.146657975268385438e+09', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args8_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 1.1, 100, &r), 9.331833897230312331e+55, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 1.1, 100), ('9.331833897230312331e+55', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args9_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 1.1, 500, &r),  4.519403368795715843e+235, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 1.1, 500), ('4.519403368795715843e+235', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args10_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 50.1, 2, &r),  1.5001295507968071788, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 50.1, 2), ('1.5001295507968071788', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args11_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 50.1, 10, &r),  8.713385849265044908, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 50.1, 10), ('8.713385849265044908', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args12_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 50.1, 100, &r),  5.909423932273380330e+18, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 50.1, 100), ('5.909423932273380330e+18', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args13_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 50.1, 500, &r),  9.740060618457198900e+165, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 50.1, 500), ('9.740060618457198900e+165', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args14_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, 1, &r),  5.183531067116809033e+07, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, 1), ('5.183531067116809033e+07', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args15_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, 10, &r),  1.6032649110096979462e+28, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, 10), ('1.6032649110096979462e+28', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args16_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, 100, &r),  1.1045151213192280064e+110, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, 100), ('1.1045151213192280064e+110', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args17_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 50.1, 1, &r),  7.222953133216603757, TEST_TOL1, GSL_SUCCESS)'
            self._test((100, 50.1, 1), ('7.222953133216603757', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args18_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 50.1, 10, &r),  1.0998696410887171538e+08, TEST_TOL1, GSL_SUCCESS)'
            self._test((100, 50.1, 10), ('1.0998696410887171538e+08', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args19_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 50.1, 100, &r),  7.235304862322283251e+63, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 50.1, 100), ('7.235304862322283251e+63', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args20_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.5, -1, &r), 0.5380795069127684191, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1.5, -1), ('0.5380795069127684191', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args21_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.5, -10, &r),  0.05303758099290164485, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 1.5, -10), ('0.05303758099290164485', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args22_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.5, -100, &r), 0.005025384718759852803, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 1.5, -100), ('0.005025384718759852803', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args23_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.5, -500, &r), 0.0010010030151059555322, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 1.5, -500), ('0.0010010030151059555322', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args24_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1, 1.1, -500, &r), 0.00020036137599690208265, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 1.1, -500), ('0.00020036137599690208265', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args25_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 1.1, -1, &r),     0.07227645648935938168, TEST_TOL1, GSL_SUCCESS)'
            self._test((10, 1.1, -1), ('0.07227645648935938168', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args26_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 1.1, -10, &r),    0.0003192415409695588126, TEST_TOL1, GSL_SUCCESS)'
            self._test((10, 1.1, -10), ('0.0003192415409695588126', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args27_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (10, 1.1, -500, &r),  -3.400379216707701408e-23, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 1.1, -500), ('-3.400379216707701408e-23', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args28_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (50, 1.1, -100, &r),   4.632883869540640460e-24, TEST_SQRT_TOL0, GSL_SUCCESS)'
            self._test((50, 1.1, -100), ('4.632883869540640460e-24', 'TEST_SQRT_TOL0'), GSL_SUCCESS)


        def test_args29_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (50, 1.1, -110.0, &r), 5.642684651305310023e-26, 0.03, GSL_SUCCESS)'
            self._test((50, 1.1, -110.0), ('5.642684651305310023e-26', '0.03'), GSL_SUCCESS)


        def test_args30_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, -1, &r),    0.0811637344096042096, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, -1), ('0.0811637344096042096', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args31_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, -10, &r),   0.00025945610092231574387, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, -10), ('0.00025945610092231574387', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args32_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, -50, &r),   2.4284830988994084452e-13, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, -50), ('2.4284830988994084452e-13', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args33_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, -90, &r),   2.4468224638378426461e-22, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, -90), ('2.4468224638378426461e-22', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args34_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, -99, &r),   1.0507096272617608461e-23, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, -99), ('1.0507096272617608461e-23', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args35_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (100, 1.1, -100, &r),  1.8315497474210138602e-24, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1.1, -100), ('1.8315497474210138602e-24', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args36_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-10, -10.1, 10.0, &r), 10959.603204633058116, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10, -10.1, 10.0), ('10959.603204633058116', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args37_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-10, -10.1, 1000.0, &r), 2.0942691895502242831e+23, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10, -10.1, 1000.0), ('2.0942691895502242831e+23', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args38_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-10, -100.1, 10.0, &r),  2.6012036337980078062, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10, -100.1, 10.0), ('2.6012036337980078062', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args39_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-1000, -1000.1, 10.0, &r),  22004.341698908631636, TEST_TOL3, GSL_SUCCESS)'
            self._test((-1000, -1000.1, 10.0), ('22004.341698908631636', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args40_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-1000, -1000.1, 200.0, &r), 7.066514294896245043e+86, TEST_TOL3, GSL_SUCCESS)'
            self._test((-1000, -1000.1, 200.0), ('7.066514294896245043e+86', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args41_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-8.1, -10.1, -10.0, &r),    0.00018469685276347199258, TEST_TOL0, GSL_SUCCESS)'
            self._test((-8.1, -10.1, -10.0), ('0.00018469685276347199258', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args42_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-10, -5.1, 1, &r),  16.936141866089601635, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10, -5.1, 1), ('16.936141866089601635', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args43_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-10, -5.1, 10, &r),  771534.0349543820541, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10, -5.1, 10), ('771534.0349543820541', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args44_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-10, -5.1, 100, &r),  2.2733956505084964469e+17, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10, -5.1, 100), ('2.2733956505084964469e+17', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args45_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, -50.1, -1, &r),  0.13854540373629275583, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, -50.1, -1), ('0.13854540373629275583', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args46_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, -50.1, -10, &r),  -9.142260314353376284e+19, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, -50.1, -10), ('-9.142260314353376284e+19', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args47_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, -50.1, -100, &r),  -1.7437371339223929259e+87, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, -50.1, -100), ('-1.7437371339223929259e+87', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args48_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, -50.1, 1, &r),  7.516831748170351173, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, -50.1, 1), ('7.516831748170351173', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args49_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, -50.1, 10, &r),  1.0551632286359671976e+11, TEST_SQRT_TOL0, GSL_SUCCESS)'
            self._test((-100, -50.1, 10), ('1.0551632286359671976e+11', 'TEST_SQRT_TOL0'), GSL_SUCCESS)


        def test_args50_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-10.5, -8.1, 0.1, &r),  1.1387201443786421724, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10.5, -8.1, 0.1), ('1.1387201443786421724', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args51_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-10.5, -11.1, 1, &r),  2.5682766147138452362, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, -11.1, 1), ('2.5682766147138452362', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args52_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100.5, -80.1, 10, &r),  355145.4517305220603, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100.5, -80.1, 10), ('355145.4517305220603', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args53_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100.5, -102.1, 10, &r),  18678.558725244365016, TEST_TOL1, GSL_SUCCESS)'
            self._test((-100.5, -102.1, 10), ('18678.558725244365016', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args54_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100.5, -500.1, 10, &r),  7.342209011101454, TEST_TOL0, GSL_SUCCESS)'
            self._test((-100.5, -500.1, 10), ('7.342209011101454', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args55_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100.5, -500.1, 100, &r),  1.2077443075367177662e+8, TEST_TOL1, GSL_SUCCESS)'
            self._test((-100.5, -500.1, 100), ('1.2077443075367177662e+8', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args56_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-500.5, -80.1, 2, &r),  774057.8541325341699, TEST_TOL4, GSL_SUCCESS)'
            self._test((-500.5, -80.1, 2), ('774057.8541325341699', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args57_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 1.1, 1, &r),  0.21519810496314438414, TEST_TOL2, GSL_SUCCESS)'
            self._test((-100, 1.1, 1), ('0.21519810496314438414', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args58_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 1.1, 10, &r),  8.196123715597869948, TEST_TOL1, GSL_SUCCESS)'
            self._test((-100, 1.1, 10), ('8.196123715597869948', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args59_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 1.1, 100, &r),  -1.4612966715976530293e+20, TEST_TOL1, GSL_SUCCESS)'
            self._test((-100, 1.1, 100), ('-1.4612966715976530293e+20', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args60_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 20.1, 1, &r),  0.0021267655527278456412, TEST_TOL2, GSL_SUCCESS)'
            self._test((-100, 20.1, 1), ('0.0021267655527278456412', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args61_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 20.1, 10, &r),   2.0908665169032186979e-11, TEST_TOL2, GSL_SUCCESS)'
            self._test((-100, 20.1, 10), ('2.0908665169032186979e-11', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args62_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 20.1, 100, &r),  -0.04159447537001340412, TEST_TOL2, GSL_SUCCESS)'
            self._test((-100, 20.1, 100), ('-0.04159447537001340412', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args63_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 1.1, -1, &r),  2.1214770215694685282e+07, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, 1.1, -1), ('2.1214770215694685282e+07', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args64_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 1.1, -10, &r),  1.0258848879387572642e+24, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, 1.1, -10), ('1.0258848879387572642e+24', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args65_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 1.1, -100, &r),  1.1811367147091759910e+67, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, 1.1, -100), ('1.1811367147091759910e+67', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args66_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 50.1, -1, &r),  6.965259317271427390, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, 50.1, -1), ('6.965259317271427390', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args67_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 50.1, -10, &r),  1.0690052487716998389e+07, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, 50.1, -10), ('1.0690052487716998389e+07', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args68_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-100, 50.1, -100, &r),  6.889644435777096248e+36, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, 50.1, -100), ('6.889644435777096248e+36', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args69_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-2.05, 1.0, 5.05, &r), 3.79393389516785e+00, TEST_TOL3, GSL_SUCCESS)'
            self._test((-2.05, 1.0, 5.05), ('3.79393389516785e+00', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args70_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-26, 2.0, 100.0, &r), 1.444786781107436954e+19, TEST_TOL3, GSL_SUCCESS)'
            self._test((-26, 2.0, 100.0), ('1.444786781107436954e+19', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args71_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1.2, 1.1e-15, 1.5, &r), 8254503159672429.02, TEST_TOL3, GSL_SUCCESS)'
            self._test((1.2, 1.1e-15, 1.5), ('8254503159672429.02', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args72_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1.0, 1000000.5, 0.8e6 + 0.5, &r), 4.999922505099443804e+00, TEST_TOL3, GSL_SUCCESS)'
            self._test((1.0, 1000000.5, '0.8e6 + 0.5'), ('4.999922505099443804e+00', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args73_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1.0, 1000000.5, 1001000.5, &r), 3480.3699557431856166, TEST_TOL4, GSL_SUCCESS)'
            self._test((1.0, 1000000.5, 1001000.5), ('3480.3699557431856166', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args74_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-1.1, 1000000.5, 1001000.5, &r), -5.30066488697455e-04, TEST_TOL3, GSL_SUCCESS)'
            self._test((-1.1, 1000000.5, 1001000.5), ('-5.30066488697455e-04', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args75_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (1.5, 1000000.5, 0.8e6 + 0.5, &r), 11.18001288977894650469927615, TEST_TOL4, GSL_SUCCESS)'
            self._test((1.5, 1000000.5, '0.8e6 + 0.5'), ('11.18001288977894650469927615', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args76_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-1.5, 1.5, -100., &r), 456.44010011787485545, TEST_TOL4, GSL_SUCCESS)'
            self._test((-1.5, 1.5, -100.0), ('456.44010011787485545', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args77_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-1.5, 1.5, 99., &r), 4.13360436014643309757065e36, TEST_TOL4, GSL_SUCCESS)'
            self._test((-1.5, 1.5, 99.0), ('4.13360436014643309757065e36', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args78_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-1.5, 1.5, 100., &r), 1.0893724312430935129254e37, TEST_TOL4, GSL_SUCCESS)'
            self._test((-1.5, 1.5, 100.0), ('1.0893724312430935129254e37', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args79_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-1.5, 1.5, 709., &r),  8.7396804160264899999692120e298, TEST_TOL4, GSL_SUCCESS)'
            self._test((-1.5, 1.5, 709.0), ('8.7396804160264899999692120e298', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args80_1(self):
            '(s, gsl_sf_hyperg_1F1_e, (-1.5, 1.5, 710., &r),  2.36563187217417898169834615e299, TEST_TOL4, GSL_SUCCESS)'
            self._test((-1.5, 1.5, 710.0), ('2.36563187217417898169834615e299', 'TEST_TOL4'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_1F1_int_e
except AttributeError:
    print("Not including tests for hyperg_1F1_int_e")

if _t_func != None:
    class test_sf_automatic_hyperg_1F1_int_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (1, 1, 0.5, &r), 1.6487212707001281468, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 0.5), ('1.6487212707001281468', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (1, 2, 500.0, &r), 2.8071844357056748215e+214, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, 2, 500.0), ('2.8071844357056748215e+214', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (1, 2, -500.0, &r), 0.002, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 2, -500.0), ('0.002', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (8, 1, 0.5, &r), 13.108875178030540372, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 1, 0.5), ('13.108875178030540372', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 1, 1.0, &r),  131.63017574352619931, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 1, 1.0), ('131.63017574352619931', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args5_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 1, 10.0, &r), 8.514625476546280796e+09, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 1, 10.0), ('8.514625476546280796e+09', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args6_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 1, 100.0, &r),  1.5671363646800353320e+56, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 1, 100.0), ('1.5671363646800353320e+56', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args7_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 20, 1.0, &r),  1.6585618002669675465, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 20, 1.0), ('1.6585618002669675465', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args8_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 20, 10.0, &r),  265.26686430340188871, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 20, 10.0), ('265.26686430340188871', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args9_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 20, 100.0, &r), 3.640477355063227129e+34, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 20, 100.0), ('3.640477355063227129e+34', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args10_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, 1.0, &r),  1.1056660194025527099, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 100, 1.0), ('1.1056660194025527099', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args11_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, 10.0, &r),  2.8491063634727594206, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 100, 10.0), ('2.8491063634727594206', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args12_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, 40.0, &r),  133.85880835831230986, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 100, 40.0), ('133.85880835831230986', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args13_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, 80.0, &r),  310361.16228011433406, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 100, 80.0), ('310361.16228011433406', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args14_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, 100.0, &r),  8.032171336754168282e+07, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 100, 100.0), ('8.032171336754168282e+07', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args15_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, 500.0, &r),  7.633961202528731426e+123, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 100, 500.0), ('7.633961202528731426e+123', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args16_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 1, 1.0, &r),  6.892842729046469965e+07, TEST_TOL1, GSL_SUCCESS)'
            self._test((100, 1, 1.0), ('6.892842729046469965e+07', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args17_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 1, 10.0, &r),  2.4175917112200409098e+28, TEST_TOL1, GSL_SUCCESS)'
            self._test((100, 1, 10.0), ('2.4175917112200409098e+28', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args18_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 1, 100.0, &r),  1.9303216896309102993e+110, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1, 100.0), ('1.9303216896309102993e+110', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args19_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 200, 1.0, &r),  1.6497469106162459226, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 200, 1.0), ('1.6497469106162459226', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args20_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 200, 10.0, &r),  157.93286197349321981, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 200, 10.0), ('157.93286197349321981', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args21_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 200, 100.0, &r),  2.1819577501255075240e+24, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 200, 100.0), ('2.1819577501255075240e+24', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args22_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 200, 400.0, &r),  3.728975529926573300e+119, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 200, 400.0), ('3.728975529926573300e+119', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args23_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 400, 10.0, &r),  12.473087623658878813, TEST_TOL0, GSL_SUCCESS)'
            self._test((100, 400, 10.0), ('12.473087623658878813', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args24_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 400, 100.0, &r),  9.071230376818550241e+11, TEST_TOL1, GSL_SUCCESS)'
            self._test((100, 400, 100.0), ('9.071230376818550241e+11', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args25_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 400, 150.0, &r),  7.160949515742170775e+18, TEST_TOL0, GSL_SUCCESS)'
            self._test((100, 400, 150.0), ('7.160949515742170775e+18', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args26_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 400, 200.0, &r),   2.7406690412731576823e+26, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 400, 200.0), ('2.7406690412731576823e+26', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args27_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 400, 300.0, &r),  6.175110613473276193e+43, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 400, 300.0), ('6.175110613473276193e+43', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args28_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 400, 400.0, &r),  1.1807417662711371440e+64, TEST_TOL3, GSL_SUCCESS)'
            self._test((100, 400, 400.0), ('1.1807417662711371440e+64', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args29_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 400, 600.0, &r),  2.4076076354888886030e+112, TEST_TOL3, GSL_SUCCESS)'
            self._test((100, 400, 600.0), ('2.4076076354888886030e+112', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args30_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 1, -1.0, &r),      0.11394854824644542810,   TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 1, -1.0), ('0.11394854824644542810', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args31_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 1, -10.0, &r),     0.0006715506365396127863, TEST_TOL1, GSL_SUCCESS)'
            self._test((10, 1, -10.0), ('0.0006715506365396127863', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args32_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 1, -100.0, &r),   -4.208138537480269868e-32, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 1, -100.0), ('-4.208138537480269868e-32', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args33_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 50, -1.0, &r),     0.820006196079380,        TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 50, -1.0), ('0.820006196079380', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args34_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, -10.0, &r),   0.38378859043466243,      TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 100, -10.0), ('0.38378859043466243', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args35_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, -100.0, &r),  0.0008460143401464189061, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 100, -100.0), ('0.0008460143401464189061', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args36_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, -500.0, &r),  1.1090822141973655929e-08, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 100, -500.0), ('1.1090822141973655929e-08', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args37_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (10, 100, -10000.0, &r), 5.173783508088272292e-21, TEST_TOL2, GSL_SUCCESS)'
            self._test((10, 100, -10000.0), ('5.173783508088272292e-21', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args38_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (50, 1, -90.0, &r),    -1.6624258547648311554e-21, TEST_TOL2, GSL_SUCCESS)'
            self._test((50, 1, -90.0), ('-1.6624258547648311554e-21', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args39_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (50, 1, -100.0, &r),    4.069661775122048204e-24, TEST_TOL2, GSL_SUCCESS)'
            self._test((50, 1, -100.0), ('4.069661775122048204e-24', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args40_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (50, 1, -110.0, &r),    1.0072444993946236025e-25, TEST_TOL2, GSL_SUCCESS)'
            self._test((50, 1, -110.0), ('1.0072444993946236025e-25', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args41_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 10, -100.0, &r), -2.7819353611733941962e-37, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 10, -100.0), ('-2.7819353611733941962e-37', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args42_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 1, -90.0, &r),  7.501705041159802854e-22, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 1, -90.0), ('7.501705041159802854e-22', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args43_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 1, -100.0, &r),  6.305128893152291187e-25, TEST_TOL3, GSL_SUCCESS)'
            self._test((100, 1, -100.0), ('6.305128893152291187e-25', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args44_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 1, -110.0, &r),  -7.007122115422439755e-26, TEST_TOL3, GSL_SUCCESS)'
            self._test((100, 1, -110.0), ('-7.007122115422439755e-26', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args45_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (100, 10, -100.0, &r),  -2.7819353611733941962e-37, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 10, -100.0), ('-2.7819353611733941962e-37', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args46_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (200, 50, -1.0, &r),  0.016087060191732290813, TEST_TOL1, GSL_SUCCESS)'
            self._test((200, 50, -1.0), ('0.016087060191732290813', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args47_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (200, 50, -300.0, &r),  -4.294975979706421471e-121, TEST_TOL2, GSL_SUCCESS)'
            self._test((200, 50, -300.0), ('-4.294975979706421471e-121', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args48_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (200, 100, -1.0, &r),  0.13397521083325179687, TEST_TOL0, GSL_SUCCESS)'
            self._test((200, 100, -1.0), ('0.13397521083325179687', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args49_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (200, 100, -10.0, &r),  5.835134393749807387e-10, TEST_TOL1, GSL_SUCCESS)'
            self._test((200, 100, -10.0), ('5.835134393749807387e-10', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args50_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (200, 100, -100.0, &r),  4.888460453078914804e-74, TEST_TOL2, GSL_SUCCESS)'
            self._test((200, 100, -100.0), ('4.888460453078914804e-74', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args51_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (200, 100, -500.0, &r),  -1.4478509059582015053e-195, TEST_TOL2, GSL_SUCCESS)'
            self._test((200, 100, -500.0), ('-1.4478509059582015053e-195', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args52_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-1, 1, 2.0, &r),  -1.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((-1, 1, 2.0), ('-1.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args53_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-1, -2, 2.0, &r),  2.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((-1, -2, 2.0), ('2.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args54_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-2, -3, 2.0, &r),  3.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((-2, -3, 2.0), ('3.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args55_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, 1, 1.0, &r),  0.4189459325396825397, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 1, 1.0), ('0.4189459325396825397', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args56_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, 1, 10.0, &r),  27.984126984126984127, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 1, 10.0), ('27.984126984126984127', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args57_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, 1, 100.0, &r),  9.051283795429571429e+12, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 1, 100.0), ('9.051283795429571429e+12', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args58_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-100, 20, 1.0, &r),  0.0020203016320697069566, TEST_TOL0, GSL_SUCCESS)'
            self._test((-100, 20, 1.0), ('0.0020203016320697069566', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args59_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -20, 1.0, &r),  1.6379141878548080173, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, -20, 1.0), ('1.6379141878548080173', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args60_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -20, 10.0, &r),  78.65202404521289970, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, -20, 10.0), ('78.65202404521289970', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args61_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -20, 100.0, &r),  4.416169713262624315e+08, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, -20, 100.0), ('4.416169713262624315e+08', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args62_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -100, 1.0, &r),  1.1046713999681950919, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, -100, 1.0), ('1.1046713999681950919', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args63_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -100, 10.0, &r),  2.6035952191039006838, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, -100, 10.0), ('2.6035952191039006838', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args64_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -100, 100.0, &r),  1151.6852040836932392, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, -100, 100.0), ('1151.6852040836932392', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args65_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-100, -200, 1.0, &r),  1.6476859702535324743, TEST_TOL0, GSL_SUCCESS)'
            self._test((-100, -200, 1.0), ('1.6476859702535324743', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args66_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-100, -200, 10.0, &r),  139.38026829540687270, TEST_TOL0, GSL_SUCCESS)'
            self._test((-100, -200, 10.0), ('139.38026829540687270', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args67_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-100, -200, 100.0, &r),  1.1669433576237933752e+19, TEST_TOL1, GSL_SUCCESS)'
            self._test((-100, -200, 100.0), ('1.1669433576237933752e+19', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args68_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -20, -1.0, &r),  0.6025549561148035735, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, -20, -1.0), ('0.6025549561148035735', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args69_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -20, -10.0, &r),  0.00357079636732993491, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10, -20, -10.0), ('0.00357079636732993491', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args70_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -20, -100.0, &r),  1.64284868563391159e-35, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10, -20, -100.0), ('1.64284868563391159e-35', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args71_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -100, -1.0, &r),  0.90442397250313899, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, -100, -1.0), ('0.90442397250313899', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args72_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -100, -10.0, &r),  0.35061515251367215, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10, -100, -10.0), ('0.35061515251367215', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args73_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-10, -100, -100.0, &r),  8.19512187960476424e-09, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10, -100, -100.0), ('8.19512187960476424e-09', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args74_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-100, -200, -1.0, &r),  0.6061497939628952629, TEST_TOL0, GSL_SUCCESS)'
            self._test((-100, -200, -1.0), ('0.6061497939628952629', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args75_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-100, -200, -10.0, &r),  0.0063278543908877674, TEST_TOL1, GSL_SUCCESS)'
            self._test((-100, -200, -10.0), ('0.0063278543908877674', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args76_1(self):
            '(s, gsl_sf_hyperg_1F1_int_e, (-100, -200, -100.0, &r),  4.34111795007336552e-25, TEST_TOL2, GSL_SUCCESS)'
            self._test((-100, -200, -100.0), ('4.34111795007336552e-25', 'TEST_TOL2'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_2F0_e
except AttributeError:
    print("Not including tests for hyperg_2F0_e")

if _t_func != None:
    class test_sf_automatic_hyperg_2F0_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_2F0_e, (0.01, 1.0, -0.02, &r), .99980388665511730901180717   , TEST_TOL0, GSL_SUCCESS)'
            self._test((0.01, 1.0, -0.02), ('.99980388665511730901180717', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_2F0_e, (0.1,  0.5, -0.02, &r), .99901595171179281891589794   , TEST_TOL0, GSL_SUCCESS)'
            self._test((0.1, 0.5, -0.02), ('.99901595171179281891589794', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_2F0_e, (1,   1, -0.02, &r), .98075549650574351826538049000    , TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, -0.02), ('.98075549650574351826538049000', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_2F0_e, (8,   8, -0.02, &r), .32990592849626965538692141   , TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 8, -0.02), ('.32990592849626965538692141', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_2F0_e, (50, 50, -0.02, &r), .2688995263772964415245902e-12 , TEST_TOL0, GSL_SUCCESS)'
            self._test((50, 50, -0.02), ('.2688995263772964415245902e-12', 'TEST_TOL0'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_2F1_conj_e
except AttributeError:
    print("Not including tests for hyperg_2F1_conj_e")

if _t_func != None:
    class test_sf_automatic_hyperg_2F1_conj_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_e, (1, 1, 1, 0.5, &r), 3.352857095662929028, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 1, 0.5), ('3.352857095662929028', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_e, (8, 8, 1, 0.5, &r), 1.7078067538891293983e+09, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 8, 1, 0.5), ('1.7078067538891293983e+09', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_e, (8, 8, 5, 0.5, &r), 285767.15696901140627, TEST_TOL1, GSL_SUCCESS)'
            self._test((8, 8, 5, 0.5), ('285767.15696901140627', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_e, (8, 8, 1, -0.5, &r), 0.007248196261471276276, TEST_TOL3, GSL_SUCCESS)'
            self._test((8, 8, 1, -0.5), ('0.007248196261471276276', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_e, (8, 8, 5, -0.5, &r), 0.00023301916814505902809, TEST_TOL3, GSL_SUCCESS)'
            self._test((8, 8, 5, -0.5), ('0.00023301916814505902809', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args5_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_e, (25, 25, 1, -0.5, &r), 5.1696944096e-06, TEST_SQRT_TOL0, GSL_SUCCESS)'
            self._test((25, 25, 1, -0.5), ('5.1696944096e-06', 'TEST_SQRT_TOL0'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_2F1_conj_renorm_e
except AttributeError:
    print("Not including tests for hyperg_2F1_conj_renorm_e")

if _t_func != None:
    class test_sf_automatic_hyperg_2F1_conj_renorm_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_renorm_e, (9, 9, -1.5, 0.99, &r), 5.912269095984229412e+49, TEST_TOL2, GSL_SUCCESS)'
            self._test((9, 9, -1.5, 0.99), ('5.912269095984229412e+49', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_renorm_e, (9, 9, -1.5, -0.99, &r), 0.10834020229476124874, TEST_TOL2, GSL_SUCCESS)'
            self._test((9, 9, -1.5, -0.99), ('0.10834020229476124874', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_renorm_e, (5, 5, -1, 0.5, &r), 1.4885106335357933625e+08, TEST_TOL2, GSL_SUCCESS)'
            self._test((5, 5, -1, 0.5), ('1.4885106335357933625e+08', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_renorm_e, (5, 5, -10, 0.5, &r), 7.968479361426355095e+21, TEST_TOL2, GSL_SUCCESS)'
            self._test((5, 5, -10, 0.5), ('7.968479361426355095e+21', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_2F1_conj_renorm_e, (5, 5, -100, 0.5, &r), 3.1113180227052313057e+208, TEST_TOL3, GSL_SUCCESS)'
            self._test((5, 5, -100, 0.5), ('3.1113180227052313057e+208', 'TEST_TOL3'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_2F1_e
except AttributeError:
    print("Not including tests for hyperg_2F1_e")

if _t_func != None:
    class test_sf_automatic_hyperg_2F1_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1, 1, 1, 0.5, &r), 2.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 1, 0.5), ('2.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, 8, 1, 0.5, &r), 12451584.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 8, 1, 0.5), ('12451584.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, -8, 1, 0.5, &r), 0.13671875, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, -8, 1, 0.5), ('0.13671875', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, -8.1, 1, 0.5, &r), 0.14147385378899930422, TEST_TOL4, GSL_SUCCESS)'
            self._test((8, -8.1, 1, 0.5), ('0.14147385378899930422', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, -8, 1, -0.5, &r), 4945.136718750000000, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, -8, 1, -0.5), ('4945.136718750000000', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args5_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, -8, -5.5, 0.5, &r),  -906.6363636363636364, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, -8, -5.5, 0.5), ('-906.6363636363636364', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args6_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, -8, -5.5, -0.5, &r), 24565.363636363636364, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, -8, -5.5, -0.5), ('24565.363636363636364', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args7_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, 8, 1, -0.5, &r), -0.006476312098196747669, TEST_TOL2, GSL_SUCCESS)'
            self._test((8, 8, 1, -0.5), ('-0.006476312098196747669', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args8_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, 8, 5, 0.5, &r), 4205.714285714285714, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 8, 5, 0.5), ('4205.714285714285714', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args9_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (8, 8, 5, -0.5, &r), 0.0028489656290296436616, TEST_TOL2, GSL_SUCCESS)'
            self._test((8, 8, 5, -0.5), ('0.0028489656290296436616', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args10_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, 1, 0.99, &r), 1.2363536673577259280e+38 , TEST_TOL2, GSL_SUCCESS)'
            self._test((9, 9, 1, 0.99), ('1.2363536673577259280e+38', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args11_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, -1.5, 0.99, &r), 3.796186436458346579e+46, TEST_TOL2, GSL_SUCCESS)'
            self._test((9, 9, -1.5, 0.99), ('3.796186436458346579e+46', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args12_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, -1.5, -0.99, &r), 0.14733409946001025146, TEST_TOL1, GSL_SUCCESS)'
            self._test((9, 9, -1.5, -0.99), ('0.14733409946001025146', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args13_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, -8.5, 0.99, &r), -1.1301780432998743440e+65, TEST_TOL2, GSL_SUCCESS)'
            self._test((9, 9, -8.5, 0.99), ('-1.1301780432998743440e+65', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args14_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, -8.5, -0.99, &r), -8.856462606575344483, TEST_TOL1, GSL_SUCCESS)'
            self._test((9, 9, -8.5, -0.99), ('-8.856462606575344483', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args15_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, -21.5, 0.99, &r), 2.0712920991876073253e+95, TEST_TOL3, GSL_SUCCESS)'
            self._test((9, 9, -21.5, 0.99), ('2.0712920991876073253e+95', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args16_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, -21.5, -0.99, &r), -74.30517015382249216, TEST_TOL2, GSL_SUCCESS)'
            self._test((9, 9, -21.5, -0.99), ('-74.30517015382249216', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args17_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, -100.5, 0.99, &r),  -3.186778061428268980e+262, TEST_TOL3, GSL_SUCCESS)'
            self._test((9, 9, -100.5, 0.99), ('-3.186778061428268980e+262', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args18_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (9, 9, -100.5, -0.99, &r),  2.4454358338375677520, TEST_TOL1, GSL_SUCCESS)'
            self._test((9, 9, -100.5, -0.99), ('2.4454358338375677520', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args19_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (25, 25, 1, -0.5, &r), -2.9995530823639545027e-06, TEST_SQRT_TOL0, GSL_SUCCESS)'
            self._test((25, 25, 1, -0.5), ('-2.9995530823639545027e-06', 'TEST_SQRT_TOL0'), GSL_SUCCESS)


        def test_args20_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, 1.0-1.0/64.0, &r), 3.17175539044729373926, TEST_TOL3, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '1.0-1.0/64.0'), ('3.17175539044729373926', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args21_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, 1.0-1.0/128.0, &r), 3.59937243502024563424, TEST_TOL2, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '1.0-1.0/128.0'), ('3.59937243502024563424', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args22_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, 1.0-1.0/256.0, &r), 4.03259299524392504369, TEST_TOL1, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '1.0-1.0/256.0'), ('4.03259299524392504369', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args23_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, 1.0-1.0/1024.0, &r), 4.90784159359675398250, TEST_TOL1, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '1.0-1.0/1024.0'), ('4.90784159359675398250', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args24_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, 1.0-1.0/65536.0, &r), 7.552266033399683914, TEST_TOL1, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '1.0-1.0/65536.0'), ('7.552266033399683914', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args25_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, 1.0-1.0/16777216.0, &r), 11.08235454026043830363, TEST_TOL1, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '1.0-1.0/16777216.0'), ('11.08235454026043830363', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args26_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, -1.0+1.0/1024.0, &r), 0.762910940909954974527, TEST_TOL0, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '-1.0+1.0/1024.0'), ('0.762910940909954974527', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args27_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, -1.0+1.0/65536.0, &r), 0.762762124908845424449, TEST_TOL0, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '-1.0+1.0/65536.0'), ('0.762762124908845424449', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args28_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 2.0, -1.0+1.0/1048576.0, &r), 0.762759911089064738044, TEST_TOL0, GSL_SUCCESS)'
            self._test((1.5, 0.5, 2.0, '-1.0+1.0/1048576.0'), ('0.762759911089064738044', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args29_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, 0.5, 3.0, 1.0, &r), 1.6976527263135502482014268 , TEST_TOL2, GSL_SUCCESS)'
            self._test((1.5, 0.5, 3.0, 1.0), ('1.6976527263135502482014268', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args30_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (1.5, -4.2, 3.0, 1.0, &r), .15583601560025710649555254 , TEST_TOL2, GSL_SUCCESS)'
            self._test((1.5, -4.2, 3.0, 1.0), ('.15583601560025710649555254', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args31_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (-7.4, 0.7, -1.5, 1.0, &r), -.34478866959246584996859 , TEST_TOL2, GSL_SUCCESS)'
            self._test((-7.4, 0.7, -1.5, 1.0), ('-.34478866959246584996859', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args32_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (0.1, -2.7, -1.5, 1.0, &r), 1.059766766063610122925 , TEST_TOL2, GSL_SUCCESS)'
            self._test((0.1, -2.7, -1.5, 1.0), ('1.059766766063610122925', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args33_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (0, -2, -4, 0.5, &r), 1.0 , TEST_TOL2, GSL_SUCCESS)'
            self._test((0, -2, -4, 0.5), ('1.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args34_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (-10.34, 2.05, 3.05, 0.1725, &r), 0.310473552213130010351006093079548, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10.34, 2.05, 3.05, 0.1725), ('0.310473552213130010351006093079548', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args35_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (-9.99999999999, 2.05, 3.05, 0.1725, &r),0.32141934630197487540298837643890, TEST_TOL2, GSL_SUCCESS)'
            self._test((-9.99999999999, 2.05, 3.05, 0.1725), ('0.32141934630197487540298837643890', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args36_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (11, -1, 11.0/2.0, 0.125 , &r), 0.75, TEST_TOL2, GSL_SUCCESS)'
            self._test((11, -1, '11.0/2.0', 0.125), ('0.75', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args37_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (-0.2, 8.8, 10.0, 0.8, &r), 0.77998971427681563, TEST_TOL1, GSL_SUCCESS)'
            self._test((-0.2, 8.8, 10.0, 0.8), ('0.77998971427681563', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args38_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (-0.2, 9.8, 11.0, 0.8, &r), 0.77574573497387267, TEST_TOL0, GSL_SUCCESS)'
            self._test((-0.2, 9.8, 11.0, 0.8), ('0.77574573497387267', 'TEST_TOL0'), GSL_SUCCESS)


        @pytest.mark.skip
        def test_args39_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (3.5, -0.5, 5.0, 0.9, &r), 0.5923981284370653465208973272, TEST_TOL2, GSL_SUCCESS)'
            self._test((3.5, -0.5, 5.0, 0.9), ('0.5923981284370653465208973272', 'TEST_TOL2'), GSL_SUCCESS)


        @pytest.mark.skip
        def test_args40_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (-1.0, -10.0, 1.0, 0.5, &r), 6.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((-1.0, -10.0, 1.0, 0.5), ('6.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args41_1(self):
            '(s, gsl_sf_hyperg_2F1_e, (3.23191, -4.0229, 8.02291, 0.5, &r), 0.4300243900348170646, TEST_TOL2, GSL_SUCCESS)'
            self._test((3.23191, -4.0229, 8.02291, 0.5), ('0.4300243900348170646', 'TEST_TOL2'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_2F1_renorm_e
except AttributeError:
    print("Not including tests for hyperg_2F1_renorm_e")

if _t_func != None:
    class test_sf_automatic_hyperg_2F1_renorm_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (1, 1, 1, 0.5, &r), 2.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 1, 0.5), ('2.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (8, 8, 1, 0.5, &r), 12451584.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 8, 1, 0.5), ('12451584.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (8, -8, 1, 0.5, &r), 0.13671875, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, -8, 1, 0.5), ('0.13671875', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (8, -8, 1, -0.5, &r), 4945.13671875, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, -8, 1, -0.5), ('4945.13671875', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (8, -8, -5.5, 0.5, &r), -83081.19167659493609, TEST_TOL2, GSL_SUCCESS)'
            self._test((8, -8, -5.5, 0.5), ('-83081.19167659493609', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args5_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (8, -8, -5.5, -0.5, &r), 2.2510895952730178518e+06, TEST_TOL2, GSL_SUCCESS)'
            self._test((8, -8, -5.5, -0.5), ('2.2510895952730178518e+06', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args6_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (8, 8, 5, 0.5, &r), 175.2380952380952381, TEST_TOL1, GSL_SUCCESS)'
            self._test((8, 8, 5, 0.5), ('175.2380952380952381', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args7_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (9, 9, -1.5, 0.99, &r), 1.6063266334913066551e+46, TEST_TOL2, GSL_SUCCESS)'
            self._test((9, 9, -1.5, 0.99), ('1.6063266334913066551e+46', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args8_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (9, 9, -1.5, -0.99, &r), 0.06234327316254516616, TEST_TOL2, GSL_SUCCESS)'
            self._test((9, 9, -1.5, -0.99), ('0.06234327316254516616', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args9_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (5, 5, -1, 0.5, &r), 4949760.0, TEST_TOL1, GSL_SUCCESS)'
            self._test((5, 5, -1, 0.5), ('4949760.0', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args10_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (5, 5, -10, 0.5, &r), 139408493229637632000.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((5, 5, -10, 0.5), ('139408493229637632000.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args11_1(self):
            '(s, gsl_sf_hyperg_2F1_renorm_e, (5, 5, -100, 0.5, &r), 3.0200107544594411315e+206, TEST_TOL3, GSL_SUCCESS)'
            self._test((5, 5, -100, 0.5), ('3.0200107544594411315e+206', 'TEST_TOL3'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_U_e
except AttributeError:
    print("Not including tests for hyperg_U_e")

if _t_func != None:
    class test_sf_automatic_hyperg_U_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 0.0001, 0.0001, &r), 1.0000576350699863577, TEST_TOL1, GSL_SUCCESS)'
            self._test((0.0001, 0.0001, 0.0001), ('1.0000576350699863577', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 0.0001, 1.0, &r), 0.9999403679233247536, TEST_TOL0, GSL_SUCCESS)'
            self._test((0.0001, 0.0001, 1.0), ('0.9999403679233247536', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 0.0001, 100.0, &r), 0.9995385992657260887, TEST_TOL0, GSL_SUCCESS)'
            self._test((0.0001, 0.0001, 100.0), ('0.9995385992657260887', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 1, 0.0001, &r), 1.0009210608660065989, TEST_TOL2, GSL_SUCCESS)'
            self._test((0.0001, 1, 0.0001), ('1.0009210608660065989', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 1.0, 1.0, &r), 0.9999999925484179084, TEST_TOL2, GSL_SUCCESS)'
            self._test((0.0001, 1.0, 1.0), ('0.9999999925484179084', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args5_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 10, 1, &r), 13.567851006281412726, TEST_TOL3, GSL_SUCCESS)'
            self._test((0.0001, 10, 1), ('13.567851006281412726', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args6_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 10, 10, &r), 0.9999244381454633265, TEST_TOL0, GSL_SUCCESS)'
            self._test((0.0001, 10, 10), ('0.9999244381454633265', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args7_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 100, 98, &r), 0.9998517867411840044, TEST_TOL2, GSL_SUCCESS)'
            self._test((0.0001, 100, 98), ('0.9998517867411840044', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args8_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 1000, 999, &r), 0.9997195294193261604, TEST_TOL2, GSL_SUCCESS)'
            self._test((0.0001, 1000, 999), ('0.9997195294193261604', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args9_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.0001, 1000, 1100, &r),  0.9995342990014584713, TEST_TOL1, GSL_SUCCESS)'
            self._test((0.0001, 1000, 1100), ('0.9995342990014584713', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args10_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.5, 1000, 800, &r), 9.103916020464797207e+08, TEST_TOL2, GSL_SUCCESS)'
            self._test((0.5, 1000, 800), ('9.103916020464797207e+08', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args11_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.5, 1000, 998, &r), 0.21970269691801966806, TEST_TOL2, GSL_SUCCESS)'
            self._test((0.5, 1000, 998), ('0.21970269691801966806', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args12_1(self):
            '(s, gsl_sf_hyperg_U_e, (0.5, 0.5, 1.0, &r), 0.7578721561413121060, TEST_TOL2, GSL_SUCCESS)'
            self._test((0.5, 0.5, 1.0), ('0.7578721561413121060', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args13_1(self):
            '(s, gsl_sf_hyperg_U_e, (1, 0.0001, 0.0001, &r), 0.9992361337764090785, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 0.0001, 0.0001), ('0.9992361337764090785', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args14_1(self):
            '(s, gsl_sf_hyperg_U_e, (1, 0.0001, 1, &r), 0.4036664068111504538, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, 0.0001, 1), ('0.4036664068111504538', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args15_1(self):
            '(s, gsl_sf_hyperg_U_e, (1, 0.0001, 100, &r), 0.009805780851264329587, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 0.0001, 100), ('0.009805780851264329587', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args16_1(self):
            '(s, gsl_sf_hyperg_U_e, (1, 1.2, 2.0, &r), 0.3835044780075602550, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 1.2, 2.0), ('0.3835044780075602550', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args17_1(self):
            '(s, gsl_sf_hyperg_U_e, (1, -0.0001, 1, &r), 0.4036388693605999482, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, -0.0001, 1), ('0.4036388693605999482', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args18_1(self):
            '(s, gsl_sf_hyperg_U_e, (8, 10.5, 1, &r),  27.981926466707438538, TEST_TOL1, GSL_SUCCESS)'
            self._test((8, 10.5, 1), ('27.981926466707438538', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args19_1(self):
            '(s, gsl_sf_hyperg_U_e, (8, 10.5, 10, &r),  2.4370135607662056809e-8, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 10.5, 10), ('2.4370135607662056809e-8', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args20_1(self):
            '(s, gsl_sf_hyperg_U_e, (8, 10.5, 100, &r),  1.1226567526311488330e-16, TEST_TOL2, GSL_SUCCESS)'
            self._test((8, 10.5, 100), ('1.1226567526311488330e-16', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args21_1(self):
            '(s, gsl_sf_hyperg_U_e, (10, -2.5, 10, &r),  6.734690720346560349e-14, TEST_TOL1, GSL_SUCCESS)'
            self._test((10, -2.5, 10), ('6.734690720346560349e-14', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args22_1(self):
            '(s, gsl_sf_hyperg_U_e, (10, 2.5, 10, &r),  6.787780794037971638e-13, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 2.5, 10), ('6.787780794037971638e-13', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args23_1(self):
            '(s, gsl_sf_hyperg_U_e, (10, 2.5, 50, &r),  2.4098720076596087125e-18, TEST_TOL0, GSL_SUCCESS)'
            self._test((10, 2.5, 50), ('2.4098720076596087125e-18', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args24_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 1.1, 1, &r),  -3.990841457734147e+6, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10.5, 1.1, 1), ('-3.990841457734147e+6', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args25_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 1.1, 10, &r),  1.307472052129343e+8, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 1.1, 10), ('1.307472052129343e+8', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args26_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 1.1, 50, &r),  3.661978424114088e+16, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10.5, 1.1, 50), ('3.661978424114088e+16', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args27_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 1.1, 90, &r),  8.09469542130868e+19, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 1.1, 90), ('8.09469542130868e+19', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args28_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 1.1, 99, &r),  2.546328328942063e+20, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 1.1, 99), ('2.546328328942063e+20', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args29_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 1.1, 100, &r),  2.870463201832814e+20, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 1.1, 100), ('2.870463201832814e+20', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args30_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 1.1, 200, &r),  8.05143453769373e+23, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10.5, 1.1, 200), ('8.05143453769373e+23', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args31_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 10.1, 0.1, &r),  -3.043016255306515e+20, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10.5, 10.1, 0.1), ('-3.043016255306515e+20', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args32_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 10.1, 1, &r),  -3.194745265896115e+12, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 10.1, 1), ('-3.194745265896115e+12', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args33_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 10.1, 4, &r),  -6.764203430361954e+07, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10.5, 10.1, 4), ('-6.764203430361954e+07', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args34_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 10.1, 10, &r),  -2.067399425480545e+09, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 10.1, 10), ('-2.067399425480545e+09', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args35_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 10.1, 50, &r),  4.661837330822824e+14, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 10.1, 50), ('4.661837330822824e+14', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args36_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 100.4, 10, &r),  -6.805460513724838e+66, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 100.4, 10), ('-6.805460513724838e+66', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args37_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 100.4, 50, &r),  -2.081052558162805e+18, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 100.4, 50), ('-2.081052558162805e+18', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args38_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 100.4, 80, &r),  2.034113191014443e+14, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10.5, 100.4, 80), ('2.034113191014443e+14', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args39_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 100.4, 100, &r),  6.85047268436107e+13, TEST_TOL1, GSL_SUCCESS)'
            self._test((-10.5, 100.4, 100), ('6.85047268436107e+13', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args40_1(self):
            '(s, gsl_sf_hyperg_U_e, (-10.5, 100.4, 200, &r),  1.430815706105649e+20, TEST_TOL2, GSL_SUCCESS)'
            self._test((-10.5, 100.4, 200), ('1.430815706105649e+20', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args41_1(self):
            '(s, gsl_sf_hyperg_U_e, (-19.5, 82.1, 10, &r),  5.464313196201917432e+60, TEST_TOL2, GSL_SUCCESS)'
            self._test((-19.5, 82.1, 10), ('5.464313196201917432e+60', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args42_1(self):
            '(s, gsl_sf_hyperg_U_e, (-50.5, 100.1, 10, &r),  -5.5740216266953e+126, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50.5, 100.1, 10), ('-5.5740216266953e+126', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args43_1(self):
            '(s, gsl_sf_hyperg_U_e, (-50.5, 100.1, 40, &r),  5.937463786613894e+91, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50.5, 100.1, 40), ('5.937463786613894e+91', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args44_1(self):
            '(s, gsl_sf_hyperg_U_e, (-50.5, 100.1, 50, &r),  -1.631898534447233e+89, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50.5, 100.1, 50), ('-1.631898534447233e+89', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args45_1(self):
            '(s, gsl_sf_hyperg_U_e, (-50.5, 100.1, 70, &r),  3.249026971618851e+84, TEST_TOL2, GSL_SUCCESS)'
            self._test((-50.5, 100.1, 70), ('3.249026971618851e+84', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args46_1(self):
            '(s, gsl_sf_hyperg_U_e, (-50.5, 100.1, 100, &r),  1.003401902126641e+85, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50.5, 100.1, 100), ('1.003401902126641e+85', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args47_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2.0, 4.0, 1.0, &r),  11.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((-2.0, 4.0, 1.0), ('11.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args48_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2.0, 0.5, 3.14, &r),  1.1896, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2.0, 0.5, 3.14), ('1.1896', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args49_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2.0, 0.5, 1.13, &r),  -1.3631, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2.0, 0.5, 1.13), ('-1.3631', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args50_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2.0, 0.5, 0.0, &r),  0.75, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2.0, 0.5, 0.0), ('0.75', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args51_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2.0, 0.5, 1e-20, &r),  0.75, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2.0, 0.5, 1e-20), ('0.75', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args52_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, 0, -0.1, &r), 1, TEST_TOL0, GSL_SUCCESS)'
            self._test((0, 0, -0.1), ('1', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args53_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, 0, -0.1, &r), -0.1, TEST_TOL0, GSL_SUCCESS)'
            self._test((-1, 0, -0.1), ('-0.1', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args54_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, 0, -0.1, &r), 0.21, TEST_TOL0, GSL_SUCCESS)'
            self._test((-2, 0, -0.1), ('0.21', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args55_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, 0, -0.1, &r), -0.661, TEST_TOL0, GSL_SUCCESS)'
            self._test((-3, 0, -0.1), ('-0.661', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args56_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, 0, -0.1, &r), 2.7721, TEST_TOL0, GSL_SUCCESS)'
            self._test((-4, 0, -0.1), ('2.7721', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args57_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, 0, -0.1, &r), -14.52201, TEST_TOL0, GSL_SUCCESS)'
            self._test((-5, 0, -0.1), ('-14.52201', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args58_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, 0, -0.1, &r), 91.230301, TEST_TOL0, GSL_SUCCESS)'
            self._test((-6, 0, -0.1), ('91.230301', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args59_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, 1, -0.1, &r), 1.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((0, 1, -0.1), ('1.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args60_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, 1, -0.1, &r), -1.1, TEST_TOL0, GSL_SUCCESS)'
            self._test((-1, 1, -0.1), ('-1.1', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args61_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, 1, -0.1, &r), 2.41, TEST_TOL1, GSL_SUCCESS)'
            self._test((-2, 1, -0.1), ('2.41', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args62_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, 1, -0.1, &r), -7.891, TEST_TOL2, GSL_SUCCESS)'
            self._test((-3, 1, -0.1), ('-7.891', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args63_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, 1, -0.1, &r), 34.3361, TEST_TOL2, GSL_SUCCESS)'
            self._test((-4, 1, -0.1), ('34.3361', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args64_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, 1, -0.1, &r), -186.20251, TEST_TOL2, GSL_SUCCESS)'
            self._test((-5, 1, -0.1), ('-186.20251', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args65_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, 1, -0.1, &r), 1208.445361, TEST_TOL2, GSL_SUCCESS)'
            self._test((-6, 1, -0.1), ('1208.445361', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args66_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 1, 2, -0.1, &r), -10.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 2, -0.1), ('-10.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args67_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, 2, -0.1, &r), 1.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((0, 2, -0.1), ('1.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args68_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, 2, -0.1, &r), -2.1, TEST_TOL2, GSL_SUCCESS)'
            self._test((-1, 2, -0.1), ('-2.1', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args69_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, 2, -0.1, &r), 6.61, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2, 2, -0.1), ('6.61', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args70_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, 2, -0.1, &r), -27.721, TEST_TOL2, GSL_SUCCESS)'
            self._test((-3, 2, -0.1), ('-27.721', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args71_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, 2, -0.1, &r), 145.2201, TEST_TOL2, GSL_SUCCESS)'
            self._test((-4, 2, -0.1), ('145.2201', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args72_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, 2, -0.1, &r), -912.30301, TEST_TOL2, GSL_SUCCESS)'
            self._test((-5, 2, -0.1), ('-912.30301', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args73_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, 2, -0.1, &r), 6682.263421, TEST_TOL2, GSL_SUCCESS)'
            self._test((-6, 2, -0.1), ('6682.263421', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args74_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 2, 3, -0.1, &r), 100.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((2, 3, -0.1), ('100.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args75_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 1, 3, -0.1, &r), 90.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, 3, -0.1), ('90.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args76_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, 3, -0.1, &r), 1.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((0, 3, -0.1), ('1.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args77_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, 3, -0.1, &r), -3.10, TEST_TOL2, GSL_SUCCESS)'
            self._test((-1, 3, -0.1), ('-3.10', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args78_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, 3, -0.1, &r), 12.81, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2, 3, -0.1), ('12.81', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args79_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, 3, -0.1, &r), -66.151, TEST_TOL2, GSL_SUCCESS)'
            self._test((-3, 3, -0.1), ('-66.151', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args80_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, 3, -0.1, &r), 409.8241, TEST_TOL2, GSL_SUCCESS)'
            self._test((-4, 3, -0.1), ('409.8241', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args81_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, 3, -0.1, &r), -2961.42351, TEST_TOL2, GSL_SUCCESS)'
            self._test((-5, 3, -0.1), ('-2961.42351', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args82_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, 3, -0.1, &r), 24450.804481, TEST_TOL2, GSL_SUCCESS)'
            self._test((-6, 3, -0.1), ('24450.804481', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args83_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 3, 4, -0.1, &r), -1000.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((3, 4, -0.1), ('-1000.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args84_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 2, 4, -0.1, &r), -1900.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((2, 4, -0.1), ('-1900.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args85_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 1, 4, -0.1, &r), -1810.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, 4, -0.1), ('-1810.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args86_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, 4, -0.1, &r), 1.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((0, 4, -0.1), ('1.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args87_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, 4, -0.1, &r), -4.10, TEST_TOL2, GSL_SUCCESS)'
            self._test((-1, 4, -0.1), ('-4.10', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args88_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, 4, -0.1, &r), 21.01, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2, 4, -0.1), ('21.01', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args89_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, 4, -0.1, &r), -129.181, TEST_TOL2, GSL_SUCCESS)'
            self._test((-3, 4, -0.1), ('-129.181', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args90_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, 4, -0.1, &r), 926.5481, TEST_TOL2, GSL_SUCCESS)'
            self._test((-4, 4, -0.1), ('926.5481', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args91_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, 4, -0.1, &r), -7594.16401, TEST_TOL2, GSL_SUCCESS)'
            self._test((-5, 4, -0.1), ('-7594.16401', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args92_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, 4, -0.1, &r), 70015.788541, TEST_TOL2, GSL_SUCCESS)'
            self._test((-6, 4, -0.1), ('70015.788541', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args93_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, -1, -0.1, &r), 1.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((0, -1, -0.1), ('1.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args94_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, -1, -0.1, &r), 0.9, TEST_TOL0, GSL_SUCCESS)'
            self._test((-1, -1, -0.1), ('0.9', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args95_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, -1, -0.1, &r), 0.01, TEST_TOL0, GSL_SUCCESS)'
            self._test((-2, -1, -0.1), ('0.01', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args96_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, -1, -0.1, &r), -0.031, TEST_TOL0, GSL_SUCCESS)'
            self._test((-3, -1, -0.1), ('-0.031', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args97_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, -1, -0.1, &r), 0.1281, TEST_TOL0, GSL_SUCCESS)'
            self._test((-4, -1, -0.1), ('0.1281', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args98_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, -1, -0.1, &r), -0.66151, TEST_TOL0, GSL_SUCCESS)'
            self._test((-5, -1, -0.1), ('-0.66151', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args99_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, -1, -0.1, &r), 4.098241, TEST_TOL0, GSL_SUCCESS)'
            self._test((-6, -1, -0.1), ('4.098241', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args100_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, -2, -0.1, &r), 1.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((0, -2, -0.1), ('1.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args101_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, -2, -0.1, &r), 1.9, TEST_TOL2, GSL_SUCCESS)'
            self._test((-1, -2, -0.1), ('1.9', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args102_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, -2, -0.1, &r), 1.81, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2, -2, -0.1), ('1.81', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args103_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, -2, -0.1, &r), -0.001, TEST_TOL0, GSL_SUCCESS)'
            self._test((-3, -2, -0.1), ('-0.001', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args104_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, -2, -0.1, &r), 0.0041, TEST_TOL0, GSL_SUCCESS)'
            self._test((-4, -2, -0.1), ('0.0041', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args105_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, -2, -0.1, &r), -0.02101, TEST_TOL0, GSL_SUCCESS)'
            self._test((-5, -2, -0.1), ('-0.02101', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args106_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, -2, -0.1, &r), 0.129181, TEST_TOL0, GSL_SUCCESS)'
            self._test((-6, -2, -0.1), ('0.129181', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args107_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, -3, -0.1, &r), 1.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((0, -3, -0.1), ('1.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args108_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, -3, -0.1, &r), 2.9, TEST_TOL2, GSL_SUCCESS)'
            self._test((-1, -3, -0.1), ('2.9', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args109_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, -3, -0.1, &r), 5.61, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2, -3, -0.1), ('5.61', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args110_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, -3, -0.1, &r), 5.429, TEST_TOL2, GSL_SUCCESS)'
            self._test((-3, -3, -0.1), ('5.429', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args111_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, -3, -0.1, &r), 0.0001, TEST_TOL0, GSL_SUCCESS)'
            self._test((-4, -3, -0.1), ('0.0001', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args112_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, -3, -0.1, &r), -0.00051, TEST_TOL0, GSL_SUCCESS)'
            self._test((-5, -3, -0.1), ('-0.00051', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args113_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, -3, -0.1, &r), 0.003121, TEST_TOL0, GSL_SUCCESS)'
            self._test((-6, -3, -0.1), ('0.003121', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args114_1(self):
            '(s, gsl_sf_hyperg_U_e, ( 0, -4, -0.1, &r), 1.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((0, -4, -0.1), ('1.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args115_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, -4, -0.1, &r), 3.9, TEST_TOL2, GSL_SUCCESS)'
            self._test((-1, -4, -0.1), ('3.9', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args116_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, -4, -0.1, &r), 11.41, TEST_TOL2, GSL_SUCCESS)'
            self._test((-2, -4, -0.1), ('11.41', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args117_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, -4, -0.1, &r), 22.259, TEST_TOL2, GSL_SUCCESS)'
            self._test((-3, -4, -0.1), ('22.259', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args118_1(self):
            '(s, gsl_sf_hyperg_U_e, (-4, -4, -0.1, &r), 21.7161, TEST_TOL2, GSL_SUCCESS)'
            self._test((-4, -4, -0.1), ('21.7161', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args119_1(self):
            '(s, gsl_sf_hyperg_U_e, (-5, -4, -0.1, &r), -1e-5, TEST_TOL0, GSL_SUCCESS)'
            self._test((-5, -4, -0.1), ('-1e-5', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args120_1(self):
            '(s, gsl_sf_hyperg_U_e, (-6, -4, -0.1, &r), 0.000061, TEST_TOL0, GSL_SUCCESS)'
            self._test((-6, -4, -0.1), ('0.000061', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args121_1(self):
            '(s, gsl_sf_hyperg_U_e, (-7, -4, -0.1, &r), -0.0004341, TEST_TOL0, GSL_SUCCESS)'
            self._test((-7, -4, -0.1), ('-0.0004341', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args122_1(self):
            '(s, gsl_sf_hyperg_U_e, (-3, 0.5, -0.5, &r), -9.5, TEST_TOL2, GSL_SUCCESS)'
            self._test((-3, 0.5, -0.5), ('-9.5', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args123_1(self):
            '(s, gsl_sf_hyperg_U_e, (-8, 0.5, -0.5, &r), 180495.0625, TEST_TOL2, GSL_SUCCESS)'
            self._test((-8, 0.5, -0.5), ('180495.0625', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args124_1(self):
            '(s, gsl_sf_hyperg_U_e, (-8, 1.5, -0.5, &r), 827341.0625, TEST_TOL2, GSL_SUCCESS)'
            self._test((-8, 1.5, -0.5), ('827341.0625', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args125_1(self):
            '(s, gsl_sf_hyperg_U_e, (-8, 1.5, -10, &r), 7.162987810253906e9, TEST_TOL2, GSL_SUCCESS)'
            self._test((-8, 1.5, -10), ('7.162987810253906e9', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args126_1(self):
            '(s, gsl_sf_hyperg_U_e, (3, 6, -0.5, &r), -296.0, TEST_TOL2, GSL_SUCCESS)'
            self._test((3, 6, -0.5), ('-296.0', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args127_1(self):
            '(s, gsl_sf_hyperg_U_e, (3, 7, -0.5, &r), 2824, TEST_TOL2, GSL_SUCCESS)'
            self._test((3, 7, -0.5), ('2824', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args128_1(self):
            '(s, gsl_sf_hyperg_U_e, (5, 12, -1.7, &r), -153.262676210016018065768591104, TEST_TOL2, GSL_SUCCESS)'
            self._test((5, 12, -1.7), ('-153.262676210016018065768591104', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args129_1(self):
            '(s, gsl_sf_hyperg_U_e, (0, 0, -0.5, &r), 1, TEST_TOL0, GSL_SUCCESS)'
            self._test((0, 0, -0.5), ('1', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args130_1(self):
            '(s, gsl_sf_hyperg_U_e, (0, 1, -0.5, &r), 1, TEST_TOL0, GSL_SUCCESS)'
            self._test((0, 1, -0.5), ('1', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args131_1(self):
            '(s, gsl_sf_hyperg_U_e, (0, 1, -0.001, &r), 1, TEST_TOL0, GSL_SUCCESS)'
            self._test((0, 1, -0.001), ('1', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args132_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, 0.99, -0.1, &r), -1.09, TEST_TOL2, GSL_SUCCESS)'
            self._test((-1, 0.99, -0.1), ('-1.09', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args133_1(self):
            '(s, gsl_sf_hyperg_U_e, (-1, 0, -0.5, &r), -0.5, TEST_TOL0, GSL_SUCCESS)'
            self._test((-1, 0, -0.5), ('-0.5', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args134_1(self):
            '(s, gsl_sf_hyperg_U_e, (-2, 0, -0.5, &r), 1.25, TEST_TOL0, GSL_SUCCESS)'
            self._test((-2, 0, -0.5), ('1.25', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args135_1(self):
            '(s, gsl_sf_hyperg_U_e, (-7, 0, -0.1, &r), -668.2263421, TEST_TOL0, GSL_SUCCESS)'
            self._test((-7, 0, -0.1), ('-668.2263421', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args136_1(self):
            '(s, gsl_sf_hyperg_U_e, (4.11, 0.11, 6.4, &r), 6.422378238765078623739153038e-5, TEST_TOL2, GSL_SUCCESS)'
            self._test((4.11, 0.11, 6.4), ('6.422378238765078623739153038e-5', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args137_1(self):
            '(s, gsl_sf_hyperg_U_e, (5, 4, 6.4, &r), 3.2586223825343211136628535e-05, TEST_TOL2, GSL_SUCCESS)'
            self._test((5, 4, 6.4), ('3.2586223825343211136628535e-05', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args138_1(self):
            '(s, gsl_sf_hyperg_U_e, (2.2,1.2 , 8.7, &r), 5.7250017539318661177749625e-03, TEST_TOL2, GSL_SUCCESS)'
            self._test((2.2, 1.2, 8.7), ('5.7250017539318661177749625e-03', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args139_1(self):
            '(s, gsl_sf_hyperg_U_e, (2, -6.4, 1, &r),1.2141502795806162484648638e-02, TEST_TOL2, GSL_SUCCESS)'
            self._test((2, -6.4, 1), ('1.2141502795806162484648638e-02', 'TEST_TOL2'), GSL_SUCCESS)

_t_func = None
try:
    _t_func = sf.hyperg_U_int_e
except AttributeError:
    print("Not including tests for hyperg_U_int_e")

if _t_func != None:
    class test_sf_automatic_hyperg_U_int_e(_test_sf_automatic):
        _func = _t_func

        def test_args0_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 1, 0.0001, &r),  8.634088070212725330, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 0.0001), ('8.634088070212725330', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args1_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 1, 0.01, &r),  4.078511443456425847, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 0.01), ('4.078511443456425847', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args2_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 1, 0.5, &r),  0.9229106324837304688, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 0.5), ('0.9229106324837304688', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args3_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 1, 2.0, &r),  0.3613286168882225847, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 2.0), ('0.3613286168882225847', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args4_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 1, 100, &r),  0.009901942286733018406, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 100), ('0.009901942286733018406', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args5_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 1, 1000, &r),  0.0009990019940238807150, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1, 1000), ('0.0009990019940238807150', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args6_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 8, 0.01, &r),  7.272361203006010000e+16, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 8, 0.01), ('7.272361203006010000e+16', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args7_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 8, 1, &r),  1957.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 8, 1), ('1957.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args8_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 8, 5, &r),  1.042496, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, 8, 5), ('1.042496', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args9_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 8, 8, &r),  0.3207168579101562500, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 8, 8), ('0.3207168579101562500', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args10_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 8, 50, &r),  0.022660399001600000000, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 8, 50), ('0.022660399001600000000', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args11_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 8, 100, &r),  0.010631236727200000000, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 8, 100), ('0.010631236727200000000', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args12_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 8, 1000, &r),  0.0010060301203607207200, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 8, 1000), ('0.0010060301203607207200', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args13_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 20, 1, &r),  1.7403456103284421000e+16, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 20, 1), ('1.7403456103284421000e+16', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args14_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 20, 20, &r),  0.22597813610531052969, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 20, 20), ('0.22597813610531052969', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args15_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 50, 1, &r),  3.374452117521520758e+61, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 50, 1), ('3.374452117521520758e+61', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args16_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 50, 50, &r),  0.15394136814987651785, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 50, 50), ('0.15394136814987651785', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args17_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 100, 0.1, &r),  1.0418325171990852858e+253, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, 100, 0.1), ('1.0418325171990852858e+253', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args18_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 100, 1, &r),  2.5624945006073464385e+154, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, 100, 1), ('2.5624945006073464385e+154', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args19_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 100, 50, &r),  3.0978624160896431391e+07, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, 100, 50), ('3.0978624160896431391e+07', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args20_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 100, 100, &r),  0.11323192555773717475, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 100, 100), ('0.11323192555773717475', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args21_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 100, 200, &r),  0.009715680951406713589, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 100, 200), ('0.009715680951406713589', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args22_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 100, 1000, &r),  0.0011085142546061528661, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 100, 1000), ('0.0011085142546061528661', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args23_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, 1000, 2000, &r),  0.0009970168547036318206, TEST_TOL0, GSL_SUCCESS)'
            self._test((1, 1000, 2000), ('0.0009970168547036318206', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args24_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -1, 1, &r),  0.29817368116159703717, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, -1, 1), ('0.29817368116159703717', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args25_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -1, 10, &r),  0.07816669698940409380, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, -1, 10), ('0.07816669698940409380', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args26_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -10, 1, &r),  0.08271753756946041959, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, -10, 1), ('0.08271753756946041959', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args27_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -10, 5, &r),  0.06127757419425055261, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -10, 5), ('0.06127757419425055261', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args28_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -10, 10, &r),  0.04656199948873187212, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -10, 10), ('0.04656199948873187212', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args29_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -10, 20, &r),  0.031606421847946077709, TEST_TOL1, GSL_SUCCESS)'
            self._test((1, -10, 20), ('0.031606421847946077709', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args30_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -100, 0.01, &r),  0.009900000099999796950, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -100, 0.01), ('0.009900000099999796950', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args31_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -100, 1, &r),  0.009802970197050404429, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -100, 1), ('0.009802970197050404429', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args32_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -100, 10, &r),  0.009001648897173103447, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -100, 10), ('0.009001648897173103447', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args33_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -100, 20, &r),  0.008253126487166557546, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -100, 20), ('0.008253126487166557546', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args34_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -100, 50, &r),  0.006607993916432051008, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -100, 50), ('0.006607993916432051008', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args35_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -100, 90, &r),  0.005222713769726871937, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -100, 90), ('0.005222713769726871937', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args36_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -100, 110, &r),  0.004727658137692606210, TEST_TOL2, GSL_SUCCESS)'
            self._test((1, -100, 110), ('0.004727658137692606210', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args37_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (1, -1000, 1010, &r),  0.0004971408839859245170, TEST_TOL4, GSL_SUCCESS)'
            self._test((1, -1000, 1010), ('0.0004971408839859245170', 'TEST_TOL4'), GSL_SUCCESS)


        def test_args38_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (8, 1, 0.001, &r),  0.0007505359326875706975, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 1, 0.001), ('0.0007505359326875706975', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args39_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (8, 1, 0.5, &r),  6.449509938973479986e-06, TEST_TOL3, GSL_SUCCESS)'
            self._test((8, 1, 0.5), ('6.449509938973479986e-06', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args40_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (8, 1, 8, &r),  6.190694573035761284e-10, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 1, 8), ('6.190694573035761284e-10', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args41_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (8, 1, 20, &r),  3.647213845460374016e-12, TEST_TOL0, GSL_SUCCESS)'
            self._test((8, 1, 20), ('3.647213845460374016e-12', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args42_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (8, 8, 1, &r),  0.12289755012652317578, TEST_TOL1, GSL_SUCCESS)'
            self._test((8, 8, 1), ('0.12289755012652317578', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args43_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (8, 8, 10, &r),  5.687710359507564272e-09, TEST_TOL1, GSL_SUCCESS)'
            self._test((8, 8, 10), ('5.687710359507564272e-09', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args44_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (8, 8, 20, &r),  2.8175404594901039724e-11, TEST_TOL1, GSL_SUCCESS)'
            self._test((8, 8, 20), ('2.8175404594901039724e-11', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args45_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (100, 100, 0.01, &r),  1.0099979491941914867e+196, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 100, 0.01), ('1.0099979491941914867e+196', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args46_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (100, 100, 0.1, &r),  1.0090713562719862833e+97, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 100, 0.1), ('1.0090713562719862833e+97', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args47_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (100, 100, 1, &r),  0.009998990209084729106, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 100, 1), ('0.009998990209084729106', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args48_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (100, 100, 20, &r),  1.3239363905866130603e-131, TEST_TOL2, GSL_SUCCESS)'
            self._test((100, 100, 20), ('1.3239363905866130603e-131', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args49_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 1, 0.01, &r),  3.274012540759009536e+06, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 1, 0.01), ('3.274012540759009536e+06', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args50_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 1, 1, &r),  1.5202710000000000000e+06, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 1, 1), ('1.5202710000000000000e+06', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args51_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 1, 10, &r),  1.0154880000000000000e+08, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 1, 10), ('1.0154880000000000000e+08', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args52_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 1, 100, &r),  3.284529863685482880e+19, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 1, 100), ('3.284529863685482880e+19', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args53_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 10, 1, &r),  1.1043089864100000000e+11, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 10, 1), ('1.1043089864100000000e+11', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args54_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 100, 1, &r),  1.3991152402448957897e+20, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 100, 1), ('1.3991152402448957897e+20', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args55_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 100, 10, &r),  5.364469916567136000e+19, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 100, 10), ('5.364469916567136000e+19', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args56_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 100, 100, &r),  3.909797568000000000e+12, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 100, 100), ('3.909797568000000000e+12', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args57_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-10, 100, 500, &r),  8.082625576697984130e+25, TEST_TOL0, GSL_SUCCESS)'
            self._test((-10, 100, 500), ('8.082625576697984130e+25', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args58_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, 1, 0.01, &r),  1.6973422555823855798e+64, TEST_TOL2, GSL_SUCCESS)'
            self._test((-50, 1, 0.01), ('1.6973422555823855798e+64', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args59_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, 1, 1, &r),  7.086160198304780325e+63, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50, 1, 1), ('7.086160198304780325e+63', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args60_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, 1, 10, &r),  5.332862895528712200e+65, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50, 1, 10), ('5.332862895528712200e+65', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args61_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, 10, 1, &r),  -7.106713471565790573e+71, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50, 10, 1), ('-7.106713471565790573e+71', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args62_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, 100, 1, &r),  2.4661377199407186476e+104, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50, 100, 1), ('2.4661377199407186476e+104', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args63_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, 10, 10, &r),  5.687538583671241287e+68, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50, 10, 10), ('5.687538583671241287e+68', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args64_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, 100, 10, &r),  1.7880761664553373445e+102, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50, 100, 10), ('1.7880761664553373445e+102', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args65_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-90, 1, 0.01, &r),  4.185245354032917715e+137, TEST_TOL2, GSL_SUCCESS)'
            self._test((-90, 1, 0.01), ('4.185245354032917715e+137', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args66_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-90, 1, 0.1, &r),  2.4234043408007841358e+137, TEST_TOL3, GSL_SUCCESS)'
            self._test((-90, 1, 0.1), ('2.4234043408007841358e+137', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args67_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-90, 1, 10, &r),  -1.8987677149221888807e+139, TEST_TOL1, GSL_SUCCESS)'
            self._test((-90, 1, 10), ('-1.8987677149221888807e+139', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args68_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-90, 10, 10, &r),  -5.682999988842066677e+143, TEST_TOL1, GSL_SUCCESS)'
            self._test((-90, 10, 10), ('-5.682999988842066677e+143', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args69_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-90, 100, 10, &r),  2.3410029853990624280e+189, TEST_TOL2, GSL_SUCCESS)'
            self._test((-90, 100, 10), ('2.3410029853990624280e+189', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args70_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-90, 1000, 10, &r),  1.9799451517572225316e+271, TEST_TOL3, GSL_SUCCESS)'
            self._test((-90, 1000, 10), ('1.9799451517572225316e+271', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args71_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, -1, 10, &r),  -9.083195466262584149e+64, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50, -1, 10), ('-9.083195466262584149e+64', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args72_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, -10, 10, &r),  -1.4418257327071634407e+62, TEST_TOL1, GSL_SUCCESS)'
            self._test((-50, -10, 10), ('-1.4418257327071634407e+62', 'TEST_TOL1'), GSL_SUCCESS)


        def test_args73_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, -100, 0.01, &r),  3.0838993811468983931e+93, TEST_TOL2, GSL_SUCCESS)'
            self._test((-50, -100, 0.01), ('3.0838993811468983931e+93', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args74_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-50, -100, 10, &r),  4.014552630378340665e+95, TEST_TOL2, GSL_SUCCESS)'
            self._test((-50, -100, 10), ('4.014552630378340665e+95', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args75_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-100, -100, 10, &r),  2.0556466922347982030e+162, TEST_TOL2, GSL_SUCCESS)'
            self._test((-100, -100, 10), ('2.0556466922347982030e+162', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args76_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-100, -200, 10, &r),  1.1778399522973555582e+219, TEST_TOL2, GSL_SUCCESS)'
            self._test((-100, -200, 10), ('1.1778399522973555582e+219', 'TEST_TOL2'), GSL_SUCCESS)


        def test_args77_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (-100, -200, 100, &r),  9.861313408898201873e+235, TEST_TOL3, GSL_SUCCESS)'
            self._test((-100, -200, 100), ('9.861313408898201873e+235', 'TEST_TOL3'), GSL_SUCCESS)


        def test_args78_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (3, 6, -0.5, &r), -296.0, TEST_TOL0, GSL_SUCCESS)'
            self._test((3, 6, -0.5), ('-296.0', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args79_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (3, 7, -0.5, &r), 2824, TEST_TOL0, GSL_SUCCESS)'
            self._test((3, 7, -0.5), ('2824', 'TEST_TOL0'), GSL_SUCCESS)


        def test_args80_1(self):
            '(s, gsl_sf_hyperg_U_int_e, (5, 12, -1.7, &r), -153.262676210016018065768591104, TEST_TOL2, GSL_SUCCESS)'
            self._test((5, 12, -1.7), ('-153.262676210016018065768591104', 'TEST_TOL2'), GSL_SUCCESS)


if __name__ == '__main__':
    unittest.main()
