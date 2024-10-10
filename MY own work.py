class HomeMaintenance:
    def __init__(self):
        self.maint_stack = []  
        self.service_queue = []      
        self.technicians = []       

    def add_maintenance_task(self, task):
        self.maint_stack.append(task)
        print(f"Task '{task}' added to maintenance task.")


    def undo_last_task(self):
        if self.maint_stack:
            task = self.maint_stack.pop()
            print(f"Task '{task}' undone.")
        else:
             print("No tasks to undo.")


    def schedule_service(self, service):
        self.service_queue.append(service)
        print(f"Service '{service}' scheduled.")

    
    def complete_service(self):
        if self.service_queue:
            service = self.service_queue.pop(0)
            print(f"Service '{service}' completed.")
        else:
            print("No services to complete.")


    def add_technician(self, tech):
        self.technicians.append(tech)
        print(f"Technician '{tech}' added to the list.")


    def list_technicians(self):
        if self.technicians:
            print("Available technicians:")
            for tech in self.technicians:
                print(f"- {tech}")
        else:
            print("No technicians available.")

home_maint = HomeMaintenance()


home_maint.add_technician("onesphore")
home_maint.add_technician("onesmo")
home_maint.add_technician("uwera")
home_maint.add_technician("belyse")
home_maint.add_technician("kellen")
home_maint.add_technician("eric")
home_maint.add_technician("enock")

home_maint.list_technicians()


home_maint.add_maintenance_task("fix the house")
home_maint.add_maintenance_task("Clean gutters")
home_maint.add_maintenance_task("fix the roof")
home_maint.add_maintenance_task("changing the colors")
home_maint.add_maintenance_task("fix the elctorics")
home_maint.add_maintenance_task("fix the cars")
home_maint.add_maintenance_task("fix the graden ")
home_maint.add_maintenance_task("fix the door's")

home_maint.undo_last_task()

home_maint.schedule_service("HVAC maintenance")
home_maint.schedule_service("Pest control")

home_maint.complete_service()
home_maint.complete_service()
