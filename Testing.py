*******************
UNIT TESTING

are used to verify that small isolated parts of a program are correct. Unit tests are generally written alongside
the code to test the behavior of individual pieces or units like functions or methods. Unit tests help assure
the developer that each piece of code does what its meant to do. An important characteristic of a unit test
 is isolation. Unit test should only test the unit of code they target, the function or method thats being tested.

przyklad REARRANGE NAMES

import re
def rearrange_name(name):
    result=re.search(r"([\w.]*), ([\w.]*)$", name)
    return "{} {}".format(result[2], result[1])

Zeby uniknac errorow z test_empty dopisujemy do defa

    if result is None:
        return name

    --->

import re
def rearrange_name(name):
    result=re.search(r"([\w.]*), ([\w.]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

HOW DO WE TEST IT?

w interpreterze unixowym

1 - python3
2 - from rearrange import rearrange_name
3 - rearrange_name("Lovelace, Ada")

4- tworzymy nowy plik rearrange_test.py
    #!/usr/bin/env python3
    from rearrange import rearrange_name
    import unittest

    class TestRearrange(unitest.TestCase):
        def test_basic(self):
            testcase = "Lovelace, Ada"
            expected = "Ada Lovelace"
            self.assertEqual(rearrange_name(testcase), expected)
        def test_empty(self):
            testcase = ""
            expected = ""
            self.assertEqual(rearrange_name(testcase), expected)

    unittest.main()

5 - w int unix: chmod +x rearrange_test.py
6 - ./rearrange_test.py

(dla samego test_basic)
 =====> Ran 1 test in 0.000s   OK


(przy wpisanych test_basic i test_empty)
=====>  Ran 2 tests in 0.000s   FAILED (errors=1)


**************
EDGE CASES

Edge cases are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges
of input we imagine our programs will typically work with.

**************
WHITE BOX TESTING

White-box testing also sometimes called clear-box or transparent testing relies on the test creators knowledge of
the software being tested to construct the test cases. With a white-box test, the test creator knows how the code
works and can write test cases that use the understanding to make sure that everything is performing the way
its expected to.

***************
BLACK BOX TESTING

in black - box testing, the software being tested is treated like an opaque box.
In other words, the tester doesnt know the internals of how the software works.
Black-box tests are written with an awareness of what the program
is supposed to do, its requirements or specifications, but not how it does it.


*********************
ASSERTEQUAL vs ASSERTRAISES method DOUCZ SIE :P

https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement

https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python