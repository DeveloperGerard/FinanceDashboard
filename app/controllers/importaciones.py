"""
    Importacion de controlladores
"""

from ..controllers.account_controller import AccountController
from ..controllers.income_controller import IncomeController
from ..controllers.loan_controller import LoanController
from ..controllers.loanpayment_controller import LoanPaymentController
from ..controllers.service_controller import ServiceController
from ..controllers.servicepayment_controller import ServicePaymentController
from ..controllers.user_controller import UserController

AccountController = AccountController
IncomeController = IncomeController 
LoanController = LoanController
LoanPaymentController = LoanPaymentController
ServiceController = ServiceController
ServicePaymentController = ServicePaymentController
UserController = UserController