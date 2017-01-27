import requests

classAndTacher = []
info = []


teachersHTML = "https://raw.githubusercontent.com/C4rbyn3m4n/IDigitize/master/TeacherTutorInfo/Teachers.txt";
tutorsHTML = "https://raw.githubusercontent.com/C4rbyn3m4n/IDigitize/master/TeacherTutorInfo/Tutors.txt";

teacherData = requests.get(teachersHTML).text
lines = teacherData.split('\n')

for line in lines:
    if ""==line:
        classAndTacher.append(info)
        info = []
    else:
        info.append(line)


print(classAndTacher)
