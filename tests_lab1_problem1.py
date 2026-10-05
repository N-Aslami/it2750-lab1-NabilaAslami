######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest

test_file = "lab1_problem1"
test_inputs = []

def test(monkeypatch, capsys):
    global test_file
    global test_inputs
    try:
        exists = os.path.exists(test_file + '.py')
        assert exists == True
        source = __import__(test_file)
    except:
        sys.exit()
    if len(test_inputs) > 0:
        inputs = iter(test_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n

    tc = unittest.TestCase()

    # Test: Ensure 4 lines of output
    assert len(output) == 4
    
    # Test: Ensure Line 1 reads as in the template
    assert output[0] == "Welcome to Tri-C IT 2750!"

    # Test: Ensure Line 2 reads as instructed
    assert output[1] == "This is Problem 1 of Lab 1"

    # Test: Ensure student entered a name on Line 3
    tc.assertRegex(output[2], '^.+$')

    # Test: Ensure student entered a valid Tri-C email address on Line 4
    tc.assertRegex(output[3].lower(), '^.+tri-c.edu$')

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################