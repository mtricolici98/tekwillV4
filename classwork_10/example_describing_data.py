cursul_python = {
    'titlu': 'Python Fundamentals',
    'mentor': {
        'nume': "Marius Tricolici",
        'specializare': "Python"
    },
    "lectii": [
        {
            "titlul": "Introducere Python",
            "durata": "2h"
        },
        {
            "titlul": "Variable in Python",
            "durata": "2h30m"
        }
    ]
}

print(cursul_python['titlu'])
print(cursul_python['mentor']['nume'])
# print(cursul_python['mentor']['varsta'])

for index, lesson in enumerate(cursul_python['lectii']):
    print(f"Lesson {index + 1} is called: {lesson['titlul']}")
