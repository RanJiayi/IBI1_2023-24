#create a class in terms of name, major and scores
class Students:
	#create a function to output the information
	def __init__(self,name,major,score_1,score_2,score_3):
		self.name=name
		self.major=major
		self.score_1=score_1
		self.score_2=score_2
		self.score_3=score_3
	def Output_information(self):
		print(self.name,self.major,self.score_1,self.score_2,self.score_3)
#collect the student's information
name=input("Student's name:")
major=input("Mmajor(BMI/BMS):")
score_1=input("Score for code portfolio:")
score_2=input("Score for group project:")
score_3=input("Exam score:")
#output by class
Students_1=Students(name,major,score_1,score_2,score_3)
Students_1.Output_information()


