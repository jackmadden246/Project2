class LanguageStudent:
    def __init__(self):
        self.languages = []


    def add_language(self,language):
        self.languages.append(language)


class LanguageTeacher(LanguageStudent):
    def __init__(self):
        super().__init__()


    def teach(self, student, language):
        if language in self.languages:
            student.add_language(language)
            return True
        else:
            return False


teacher = LanguageTeacher()
teacher.add_language('English')
teacher.add_language('French')
student = LanguageStudent()
teacher.teach(student, 'French')
teacher.teach(student, 'English')
print(student.languages)
