import unittest

# Given the following dictionary of employees, print out the data in the following format:

# Employee: {name}, Age: {age}, and Salary: {salary}


def employeePrinter(employeeDict: dict[dict]) -> str:

    output = ""

    for employee in employeeDict:
        employeeName = employeeDict[employee]["name"]
        employeeAge = employeeDict[employee]["age"]
        employeeSalary = employeeDict[employee]["salary"]
        output += f"Employee: { employeeName}, Age: {employeeAge}, and Salary: {employeeSalary}\n"

    return output


class employeePrinterTest(unittest.TestCase):
    def test_01(self):

        sample_dict = {
            "emp1": {"name": "Steve", "salary": 7500, "age": 32},
            "emp2": {"name": "Noel", "salary": 6500, "age": 25},
            "emp3": {"name": "Arjun", "salary": 8000, "age": 40},
            "emp4": {"name": "Vithusan", "salary": 500, "age": 18},
        }
        self.assertEqual(
            employeePrinter(sample_dict),
            "Employee: Steve, Age: 32, and Salary: 7500\nEmployee: Noel, Age: 25, and Salary: 6500\nEmployee: Arjun, Age: 40, and Salary: 8000\nEmployee: Vithusan, Age: 18, and Salary: 500\n",
        )

    def test_02(self):

        sample_dict = {
            "emp1": {"name": "Steve", "salary": 7500, "age": 32},
            "emp2": {"name": "Noel", "salary": 6500, "age": 25},
        }
        self.assertEqual(
            employeePrinter(sample_dict),
            "Employee: Steve, Age: 32, and Salary: 7500\nEmployee: Noel, Age: 25, and Salary: 6500\n",
        )


if __name__ == "__main__":
    unittest.main()
