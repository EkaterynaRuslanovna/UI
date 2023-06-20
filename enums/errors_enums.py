from enum import Enum

"""
Assertion errors.
"""


class ErrorMassages(Enum):

    ELEMENT_IS_NOT_VISIBLE = "Element {} is not visible"
    ELEMENT_IS_VISIBLE = "Element {} is visible"
    ELEMENT_IS_NOT_CLICKABLE = "Element {} is not clickable"
    CURRENT_BALANCE_IS_NOT_EQL = "Current balance {0} is not eql {1}"
    FAILED_TO_ADD_CUSTOMER = "Failed to add customer"
    FAILED_TO_OPEN_ACCOUNT = "Failed to open an account"
