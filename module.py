from moduleElement import *

class Module(object):
    dates = []
    elements = []
    module_count = 0

    def __init__(self, ects, title, semester, grade=None):
        self.__ects = ects
        self.__title = title
        self.__semester = semester
        self.__grade = grade
        Module.module_count += 1

    def get_important_dates_overview(self):
        for element in self.dates:
            print(element)

    def set_grade(self, grade):
        self.__grade = grade

    def add_module_element(self, class1, date):
        object = class1(date)
        object.add_important_date(date)
        self.elements.append(object)

    def add_important_date(self, date):
        self.dates.append(date)

    def get_title(self):
        return self.__title

    def get_grade(self):
        return self.__grade

#########################################################################

class Course(Module):

    def __str__(self):
        return "Course:", Module.__title
        ######## CODE MISSING HERE

#########################################################################

class Seminar(Module):

    def __init__(self,ects,title,semester,topic, grade=None):
        Module.__init__(self,ects, title, semester, grade=None)
        Seminar.topic = topic
    
    def __str__(self):
        return Seminar.topic


    def get_topic(self):
        return Seminar.topic

#########################################################################

class Thesis(Module):

    def __init__(self,ects,title,semester,topic,research_group, grade=None):
        Module.__init__(self, ects, title, semester, grade=None)
        Thesis.topic = topic
        Thesis.research_group = research_group

    def __str__(self):
        return Thesis.topic, Thesis.research_group

    def get_topic(self):
        return Thesis.topic

    def get_research_group(self):
        return Thesis.research_group

#########################################################################

### test cases ###

info1 = Course(6,"Info 1",1)
info1.add_module_element(Midterm,"31.10.2017")
info1.add_module_element(FinalExam,"20.12.2017")
info1.get_important_dates_overview()
# expected output:
# Important dates for Info 1:
#	Midterm on 31.10.2017
#	Final Exam on 20.12.2017
print(info1)
# expected output:
# Course: Info 1

math1 = Course(6, "Mathematik I", 1)
math1.add_module_element(Midterm,"18.12.2017")
math1.get_important_dates_overview()
# Important dates for Mathematik I:
#	Midterm on 18.12.2017


# print(Module.module_count)
# expected output: 2

thesis = Thesis(18,"Bachelor Thesis",6,"A promising research topic on Software Engineering","SEAL")
# print(thesis)
# expected output:
# Bachelor Thesison the topic: A promising research topic on Software Engineering in the Research Group SEAL


sem = Seminar(3,"Seminar in Software Engineering",4,"A Seminar topic")
# print(sem)
# print(thesis)
# expected output:
# Seminar in Software Engineering under the topic: A Seminar topic

info1.set_grade(6)
