import unittest
from company_prog.employee import Employee
from company_prog.car import Car


class TestEmployee(unittest.TestCase, Employee, Car):
    testId = 0

    @classmethod
    def setUpClass(cls) -> None:
        print('start testing Employee Class.')

    @classmethod
    def tearDownClass(cls) -> None:
        print('end testing Employee Class.')

    def setUp(self) -> None:
        self.emp_1 = Employee("memo", 2000, 'suffering', 111, 'Mercedes',
                              'memo@gmail.com', int(2e4), 999, '-100%')
        self.emp_2 = Employee("catKoot", 3000, 'still awesome', 111, 'toyota',
                              'catKoot@gmail.com', int(2e5), 999, '-100%')

        TestEmployee.testId += 1
        print(f'start test {TestEmployee.testId}')

    def tearDown(self) -> None:
        print('tearDown test.')

    def test_work(self):
        print('test_work')

        self.assertEqual(self.sleep(8), 'happy')
        self.assertEqual(self.sleep(10), 'tired')
        self.assertEqual(self.sleep(6), 'lazy')

    def test_refuel(self):
        print('test_refuel')

        self.assertEqual(Car.fuel_rate + 200, self.refuel(200))


if __name__ == "__main__":
    unittest.main()



#  name, money, mood, id, car, email, salary, distance_to_work, health_rate