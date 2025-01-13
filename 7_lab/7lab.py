class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"Имя работника: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self):
        return f"Менеджер {self.name} управляет проектами в {self.department} отделе."


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник {self.name} проводит техническое обслуживание {self.specialization}."


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        info = f"Участники команды:\n"
        for emp in self.team:
            info += emp.get_info() + "\n"
        return info


if name == "__main__":
    employee = Employee("Андрей", 1)
    technician = Technician("Арутр", 2, "Связи")
    manager = Manager("Кирилл", 3, "IT")
    tech_manager = TechManager("Евгений", 4, "Инженер", "Системы")

    print(employee.get_info())
    print(technician.get_info())
    print(technician.perform_maintenance())
    print(manager.get_info())
    print(manager.manage_project())

    tech_manager.add_employee(employee)
    tech_manager.add_employee(technician)
    tech_manager.add_employee(manager)

    print(tech_manager.get_info())
    print(tech_manager.manage_project())
    print(tech_manager.perform_maintenance())
    print(tech_manager.get_team_info())