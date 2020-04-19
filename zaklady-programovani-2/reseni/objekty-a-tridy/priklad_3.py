class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Poté zbývá {self.remainingHolidayDays} dní."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    vypis = f"{self.name} pracuje na pozici {self.position}. "
    if self.probation:
      vypis += "Je ve zkušební době."
    return vypis
  def __init__(self, name, position, probation):
    self.name = name
    self.position = position
    self.probation = probation
    self.remainingHolidayDays = 25

class Manager(Employee):
  def addEmployee(self, employee):
    self.employeeList.append(employee)
  def getEmployees(self):
    print("Vypisuji podřízené:")
    for employee in self.employeeList:
      print(employee.name)
  def __init__(self, name, position, probation):
    super().__init__(name, position, probation)
    self.employeeList = []
