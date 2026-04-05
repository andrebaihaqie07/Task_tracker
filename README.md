import datetime
print("--------------------- Welcome In Your task---------------------------")


class TaskTracker:

    def __init__(self):
        self.items = [{'ID': '1', 'activity': 'Membaca', 'Description': 'tolong beri pemberitahuan 5 menit ',
                       'Status': 'To-do', 'CreatedAt': '2026-04-05 07:30', 'UpdateAt': ''},
                      {'ID': '2', 'activity': 'Berlari', 'Description': 'Andre mengajak lari jam 7 ',
                       'Status': 'To-do', 'CreatedAt': '2026-04-05 07:45', 'UpdateAt': ''},
                      {'ID': '3', 'activity': 'Belajar', 'Description': 'besok ada ulangan',
                       'Status': 'In-progress', 'CreatedAt': '2026-04-05 07:50', 'UpdateAt': ''},
                      {'ID': '4', 'activity': 'Tidur', 'Description': 'Mohon istirahat besom ada ulangan',
                       'Status': 'In-progress', 'CreatedAt': '2026-04-05 08:00', 'UpdateAt': ''},
                      {'ID': '5', 'activity': 'Sekolah', 'Description': 'Sekolah jam 7:00',
                       'Status': 'Done', 'CreatedAt': '2026-04-05 08:00', 'UpdateAt': ''},
                      {'ID': '6', 'activity': 'Les', 'Description': 'Les sekolah jam 3',
                       'Status': 'Done', 'CreatedAt': '2026-04-05 08:01', 'UpdateAt': ''}
                      ]
        self.id = 1 + len(self.items)
        self.time = datetime.datetime.now()

    def show_tasks(self, tasks, title):
        print(f"\n{'='*140}")
        print(f"{title:^140}")
        print(f"{'='*140}")
        print(f"{'ID':<5}{'Activity':<15}{'Description':<50}{'Status':<15}{'CreatedAt':<20}{'UpdateAt':<20}")
        print(f"{'-'*140}")

        if not tasks:
            print("No data found.")
        else:
            for task in tasks:
                print(
                    f"{task['ID']:<5}{task['activity']:<15}{task['Description']:<50}{task['Status']:<15}{task['CreatedAt']:<20}{task['UpdateAt']:<20}")

        print(f"{'='*140}\n")

    def add_activity(self):
        while True:
            activity = input('what activity want you do?: ')
            if activity == 'keluar':
                break
            if not activity.isalpha():
                print(F'Activity should not empty and must be letter')
                continue
            description = input('Add description?:')
            if description == 'keluar':
                break
            while not description.replace(" ", "").isalpha():
                print(f'description must be letter')
                description = input('Add description?:')
                if description == 'keluar':
                    break
            if description == 'keluar':
                break
            status = input('What a status?:')
            if status == 'keluar':
                break
            while status not in ['To-do', 'In-progress', 'Done']:
                print(f'Status must be To-do, In-progress, or Done')
                status = input('what a status?:')
                if status == 'keluar':
                    break
            if status == 'keluar':
                break
            time_create = self.time.strftime('%Y-%m-%d %H:%M')
            task = {'ID': self.id, 'activity': activity, 'Description': description,
                    'Status': status, 'CreatedAt': time_create, 'UpdateAt': ''}
            self.items.append(task)
            self.id += 1

    def delete(self):
        while True:
            print(
                f"\nDaftar saat ini: {[task['activity'] for task in self.items]}")
            delete_activity = input("What activity you want delete?:")
            if delete_activity == 'keluar':
                break
            sebelum = len(self.items)
            self.items = [
                task for task in self.items if task['activity'] != delete_activity]

            if len(self.items) < sebelum:
                print(f"Activity '{delete_activity}' successfully deleted!")

            else:
                print(
                    f"Activity '{delete_activity}' not found. Please try again.")

    def mark_activity(self):
        while True:
            print(
                f"\nDaftar saat ini: {[task['activity'] for task in self.items]}")
            update_mark = input('what activity do you want mark?: ')
            if update_mark == 'keluar':
                break

            found = False
            for new_mark in self.items:
                if new_mark['activity'] == update_mark:
                    found = True
                    while True:
                        pembaruan_mark = input(
                            'Mark status (To-do, In-progress, Done): ')

                        if pembaruan_mark in ['To-do', 'In-progress', 'Done']:
                            new_mark['Status'] = pembaruan_mark
                            new_mark['UpdateAt'] = self.time.strftime(
                                ('%Y-%m-%d %H:%M'))
                            print('Update succesfully')
                            return
                        else:
                            print('Status must be To-do, In-progress, or Done')

            if not found:
                print('Activity not found')

    def update(self):
        while True:
            print(
                f"\nDaftar saat ini: {[task['activity'] for task in self.items]}")
            update_activity = input('what activity do you want update?')
            if update_activity == 'keluar':
                break
            for new_update in self.items:
                if new_update['activity'] == update_activity:
                    while True:
                        pembaruan = input('input activity you want update?: ')
                        if pembaruan.isalpha() and not pembaruan.isdigit():
                            new_update['activity'] = pembaruan
                            new_update['UpdateAt'] = self.time.strftime(
                                ('%Y-%m-%d %H:%M'))
                            print("Update Succesfully")
                            return
                        else:
                            print('Input must be letter')

            else:
                print('Input must be letter')

    def list_done(self):
        done_tasks = [task for task in self.items if task['Status'] == 'Done']
        self.show_tasks(done_tasks, "DONE TASKS")

    def list_to_do(self):
        todo_tasks = [task for task in self.items if task['Status'] == 'To-do']
        self.show_tasks(todo_tasks, "TO-DO TASKS")

    def list_in_progress(self):
        progress_tasks = [
            task for task in self.items if task['Status'] == 'In-progress']
        self.show_tasks(progress_tasks, "IN-PROGRESS TASKS")

    def list_all(self):
        self.show_tasks(self.items, "ALL TASKS")


test = TaskTracker()
print("-----------The feature---------------------- \n1.add_activity\n2.delete\n3.mark_activity\n4.update\n5.list_done\n6.list_to_do\n7.list_in_progress\n8.list_all")
while True:
    y = input(
        'what do you want to do?\n to exit type "keluar"\nPlease Type Feature:\n '
    ).lower()

    if y == 'keluar':
        break
    elif y == 'update':
        test.update()
    elif y == 'mark_activity':
        test.mark_activity()
    elif y == 'delete':
        test.delete()
    elif y == 'add_activity':
        test.add_activity()
    elif y == 'list_done':
        print(test.list_done())
    elif y == 'list_to_do':
        print(test.list_to_do())
    elif y == 'list_in_progress':
        print(test.list_in_progress())
    elif y == 'list_all':
        print(test.list_all())
    else:
        print("Feature not found")
