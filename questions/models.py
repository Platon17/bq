#=AleX= 
from django.db import models
from django.utils import timezone

class Question(models.Model):
    title		= models.CharField(max_length=31)
    text 		= models.CharField(max_length=255)
    added_ad 	= models.DateTimeField('added date',default=timezone.now)
    rating 		= models.IntegerField(default=0)
    author 		= models.ForeignKey(User, on_delete=models.PROTECT)
    likes 		= models.ManyToManyField(User, related_name='likes_set')
	def added(self):
		self.added_at = timezone.now()
		self.save()
		
    def __str__(self): 
		return self.text

class Answer(models.Model):
    Question 	= models.ForeignKey(Question, on_delete=models.CASCADE)
    text 		= models.CharField(max_length=255)
    correct 	= models.BooleanField(default=False)
    added_at 	= models.DateTimeField('added date',default=timezone.now)
    author 		= models.ForeignKey(User, on_delete=models.PROTECT)

	
	def added(self):
		self.added_at = timezone.now()
		self.save()

	# if correct - Right, else - Wrong	
    def __str__(self):
        if self.correct:
            value = "Right!"
        else:
            value = "Wrong"
        return "{} - ({}) [{}]".format(self.text, value, self.Question.text)

