import unittest
from scripts.generated_validation_code import validate_data
import pandas as pd

class TestDataValidation(unittest.TestCase):

    def setUp(self):
        # Set up sample historic violations
        self.historic_violations = {
            '1234567890': 3,  # Customer 1234567890 has 3 previous violations
            '0987654321': 1   # Customer 0987654321 has 1 previous violation
        }

    def test_validate_data_no_errors(self):
        row_data = {
            'Customer_ID': '1234567890',
            'Transaction_Date': '2025-03-23',
            'Amount': 100,
            'Transaction_Type': 'Credit',
        }

        errors, remediation_actions, risk_score = validate_data(row_data, self.historic_violations)

        # We expect no errors in this case
        self.assertEqual(errors, [])
        self.assertEqual(risk_score, 1)  # Assuming a risk score of 1 for this case

    def test_validate_data_with_errors(self):
        row_data = {
            'Customer_ID': '1234567890',
            'Transaction_Date': 'invalid-date',  # Invalid date
            'Amount': -100,  # Invalid amount
            'Transaction_Type': 'Credit',
        }

        errors, remediation_actions, risk_score = validate_data(row_data, self.historic_violations)

        # We expect errors for invalid date and amount
        self.assertIn("Invalid date format", errors)
        self.assertIn("Amount cannot be negative", errors)
        self.assertGreater(risk_score, 1)  # Risk score should be higher due to errors

    def test_missing_customer_id(self):
        row_data = {
            'Transaction_Date': '2025-03-23',
            'Amount': 100,
            'Transaction_Type': 'Credit',
        }

        errors, remediation_actions, risk_score = validate_data(row_data, self.historic_violations)

        # We expect errors due to missing Customer_ID
        self.assertIn("Missing Customer ID", errors)
        self.assertEqual(risk_score, 1)

if __name__ == '__main__':
    unittest.main()
