import unittest

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fsm.fsm import FSM

class TestFSM(unittest.TestCase):
    """Set up the MOD 3 FSM for testing"""
    def setUp(self):
        states = {
            's0': {'0': 's0', '1': 's1'},
            's1': {'0': 's2', '1': 's0'},
            's2': {'0': 's1', '1': 's2'}
        }
        start_state = 's0'
        accepting_states = {'s0'}
        self.fsm = FSM(start_state, states, accepting_states)


    '''Test the final state of the FSM after running on the input'''
    def test_finalstate(self):
        self.fsm.run('1110')
        self.assertEqual(self.fsm.state, 's2')
        self.fsm.reset()
        self.fsm.run('110')
        self.assertEqual(self.fsm.state, 's0')
        self.fsm.reset()
        self.fsm.run('111111') # 63
        self.assertEqual(self.fsm.state, 's0')
    
    """Test the functionality of reset function"""
    def test_reset(self):
        self.fsm.run('1110')
        self.assertEqual(self.fsm.state, 's2')
        self.fsm.reset()
        self.assertEqual(self.fsm.state, 's0')

    """Test the response to invalid input in transition function"""
    def test_invalid_transition(self):
        with self.assertRaises(ValueError):
            self.fsm.transition('2')  # Assuming '2' is not a valid input symbol

    """some unique cases"""
    def test_edge_cases(self):
        self.fsm.reset()
        self.assertEqual(self.fsm.run(''), self.fsm.start_state)  # Empty input should not change state
        self.fsm.reset()
        self.assertEqual(self.fsm.run('00110101'), 's2') # 53 leading zeros
        self.fsm.reset()

if __name__ == '__main__':
    unittest.main()
