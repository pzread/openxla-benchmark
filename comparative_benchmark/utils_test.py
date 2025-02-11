#!/usr/bin/env python3
#
# Copyright 2023 The OpenXLA Authors
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import numpy as np
import unittest

import utils


class UtilsTest(unittest.TestCase):

  def test_compare_tensors(self):
    verdicts = utils.compare_tensors(
        outputs=(np.array([0]), np.array([0.1, 0.1]), np.array([10])),
        expects=(np.array([-1]), np.array([0.1, 0.2]), np.array([11])),
        absolute_tolerance=0.2,
        relative_tolerance=0.1,
    )

    self.assertEqual(
        verdicts,
        [
            (False, 1),
            (True, 0.1),
            # It's equal because abs(10 - 11) <= 0.2 + 0.1 * 11
            (True, 1),
        ])


if __name__ == "__main__":
  unittest.main()
