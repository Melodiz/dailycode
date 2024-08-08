class DeliveryScheduler:
    def __init__(self, employees):
        self.employees = employees
        self.current_time = 0
        self.tips = 0

    def schedule_deliveries(self):
        self.current_time = 0
        self.tips = 0
        self.employees.sort(key=lambda x: x[0])
        for ai, bi in self.employees:
            if self.current_time + bi <= ai:
                self.tips += ai - (self.current_time + bi)
            else:
                self.tips -= (self.current_time + bi) - ai
            self.current_time += bi

    def update_employee(self, index, new_ai, new_bi):
        self.employees[index] = (new_ai, new_bi)
        self.schedule_deliveries()

    def get_tips(self):
        return self.tips

# Reading input
n, q = map(int, input().split())
min_num = max_num = 0
employees = []

for i in range(n):
    ai, bi = map(int, input().split())
    employees.append((ai, bi))

scheduler = DeliveryScheduler(employees)
scheduler.schedule_deliveries()
max_num = scheduler.get_tips()

updates = []
for i in range(q):
    index, new_ai, new_bi = map(int, input().split())
    updates.append((index, new_ai, new_bi))

for index, new_ai, new_bi in updates:
    scheduler.update_employee(index, new_ai, new_bi)
min_num = scheduler.get_tips()

print(max_num)
print(min_num)