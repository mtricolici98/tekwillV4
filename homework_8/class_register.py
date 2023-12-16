names = input("Lista de nume separata prin virgula: ")  # Marius, Ion, Vasile
list_of_names = names.split(',')

list_of_marks = []

for name in list_of_names:
    mark = input(f"Nota pentru {name}: ")
    list_of_marks.append(int(mark))

for indece_nota in range(len(list_of_marks)):
    list_of_marks[indece_nota] = int(list_of_marks[indece_nota])

for index in range(len(list_of_marks)):  # range(pana_la), range(de_la, pana_la), range(de_la, pana_la, pasul=1)
    numele = list_of_names[index]
    nota = list_of_marks[index]
    print(f"{numele} are nota {nota} ")

marks_sum = 0
for mark in list_of_marks:
    marks_sum += int(mark)

print(f"Suma notelor: {marks_sum}")
print(f"Media notelor: {marks_sum / len(list_of_marks)}")
