import requests

teachersHTML = "https://raw.githubusercontent.com/C4rbyn3m4n/IDigitize/master/TeacherTutorInfo/Teachers.txt";
tutorsHTML = "https://raw.githubusercontent.com/C4rbyn3m4n/IDigitize/master/TeacherTutorInfo/Tutors.txt";

teacherData= requests.get(teachersHTML).text
print (teacherData)