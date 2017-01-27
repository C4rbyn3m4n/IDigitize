import requests

teachersHTML = "https://raw.githubusercontent.com/C4rbyn3m4n/IDigitize/master/TeacherTutorInfo/Teachers.txt";
tutorsHTML = "https://raw.githubusercontent.com/C4rbyn3m4n/IDigitize/master/TeacherTutorInfo/Tutors.txt";

tutorsData = requests.get(tutorsHTML).text

for line in tutorsData:
    print(line)
