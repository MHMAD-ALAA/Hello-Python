from company_prog.employee import Employee
from company_prog.main import empDict
# from datetime import datetime


class Office(object):
    def __init__(self, name, employees):
        self.id = None
        self.salary = None
        self.name: str = name
        self.employees: list = employees

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        required_emp: list = []
        for k in empDict.keys():
            if empDict[k] == emp_id:
                required_emp.append(k)

        return required_emp

    def hire(self):
        """if you send to this fucntion an Employee object that
        mean you already create and added this Employee with the constructor
        while creating it!"""
        pass

    def fire(self, emp_id):
        for key, val in empDict.items():
            if val == emp_id:
                del empDict[key]
                Employee.employeesNum -= 1
                break

    def deduct(self, emp_id, deduction):
        if self.id == emp_id:
            self.salary -= deduction

    def reward(self, emp_id, reward):
        if self.id == emp_id:
            self.salary += reward

    def check_lateness(self, emp_id, move_hour):
        # time_now = datetime.now().strftime("%H")
        # time_now = int(time_now)
        if move_hour - 9 > 0:
            Office.deduct(self, emp_id, 10)
        else:
            Office.reward(self, emp_id, 10)

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        req_velocity = distance / abs(move_hour - target_hour)
        if req_velocity < velocity:
            return "late employee"
        else:
            return "employee not late"

    @classmethod
    def change_emp_num(cls, num):
        Employee.employeesNum = num
