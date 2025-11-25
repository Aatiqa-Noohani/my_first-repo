from abc import ABC, abstractmethod

# ------------------------------
# Abstract Base Class
# ------------------------------
class EmployeeBase(ABC):
    @abstractmethod
    def show_info(self):
        pass
