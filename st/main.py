from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item


# if __name__ == "__main__":
#     student = student('иванов','Иван','иванович','34',{'химия': 5,'математика':4})
#     studentRegistry = StudentRegistry()
#     studentRegistry.addStudents(student)
#     student.printLong()

main_menu = Menu()

file_menu = main_menu.addItems('Список студентов',test)
file_menu = main_menu.addItems('Добавить студента',test)
file_menu = main_menu.addSubMenu('Редактировать студента')

file_menu.addItems('Изменить фамилию', test)
file_menu.addItems('Изменить имя', test)
file_menu.addItems('Изменить отчество', test)
file_menu.addItems('Изменить группу', test)
file_menu.addItems('Добавить оценку', test)
file_menu.addItems('Изменить оценку', test)
file_menu.addItems('Удалить оценку', test)

file_menu = main_menu.addItems('Удалить студента',test)

file_menu = main_menu.addItems('Показать отличников',test)
file_menu = main_menu.addItems('Показать неуспевающих',test)


main_menu.run()