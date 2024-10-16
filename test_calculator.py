import unittest
import calculator

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calculator.add(470, 700), 1170)
    self.assertEqual(calculator.add(-1, 2), 1)
    self.assertEqual(calculator.add(-5, -2), -7)

  def test_subtraction(self):
    self.assertEqual(calculator.subtr(10, 5), 5)
    self.assertEqual(calculator.subtr(-1, 1), -2)
    self.assertEqual(calculator.subtr(-1, -1), 0)
  
  def test_multiplication(self):
    self.assertEqual(calculator.multiply(10, 0), 0)
    self.assertEqual(calculator.multiply(5, 5), 25)
    self.assertEqual(calculator.multiply(-4, 4), -16)
  
  def test_divide(self):
      self.assertEqual(calculator.divide(10, 2), 5)
      self.assertEqual(calculator.divide(5, 0), None)  # This tests for division by zero
      self.assertEqual(calculator.divide(-10, 2), -5)
    
 


if __name__ == '__main__':
  unittest.main()