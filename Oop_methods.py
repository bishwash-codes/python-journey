class employee:
    num_emp = 0
    bonus = 1.05
    gender = "male"
    sum = 0

    def __init__(self, name, age, pay, position):
        self.name = name
        self.age = age
        self.pay = pay
        self.position = position
        employee.num_emp += 1
        employee.sum += pay

    def raise_amt(self):
        self.pay = int(employee.bonus * self.pay)

    @classmethod
    def total_emp(cls):
        return f"{cls.num_emp}"

    @classmethod
    def total_salary(cls):
        return cls.sum

    @staticmethod
    def available_position(position):
        available_pos = ["analyst", "web dev", "QA", "Data scientist"]
        return position in available_pos


emp_1 = employee("santosh", 18, 120000, "analyst")
emp_2 = employee("nirvan", 17, 679000, "web dev")
emp_3 = employee("adarsh", 19, 230000, "QA")

print(emp_2.pay)
emp_2.raise_amt()
print(f"the increased salary is  {emp_2.pay}")

print(f"total employee are {employee.total_emp()}")

print(employee.total_salary())

print(employee.available_position("QA"))
