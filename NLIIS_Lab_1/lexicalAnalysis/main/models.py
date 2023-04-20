from django.db import models

# Create your models here.

class Word(models.Model):
	body = models.CharField(max_length=50, blank=True, null=True)
	pos = models.CharField(max_length=50, null=True)
	prefixes = models.CharField(max_length=100, null=True)
	suffixes = models.CharField(max_length=100, null=True)


	def __str__(self):
		return self.body[:50]


	class Meta:
		verbose_name = 'Word'
		verbose_name_plural = 'Words'


class Text(models.Model):
	body = models.TextField('Text', blank=True, null=True)
	lemmas = models.ForeignKey(Word, on_delete=models.CASCADE, null=True)
	tree = models.TextField('Tree', null=True)
	semanticTree = models.TextField('Semantic Tree', null=True)
	
	def __str__(self):
		return self.body[:50]


	class Meta:
		verbose_name = 'Text'
		verbose_name_plural = 'Texts'