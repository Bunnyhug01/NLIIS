import sys
sys.path.append(r'.\main\components')

from django.shortcuts import render, redirect
from django.http import *
from .models import Word, Text
from .forms import TextForm, WordForm

from textPreprocessing import textPreprocessing

from tags import Tag
from wordProcessing import WordProcessing
from affixes import Affix
from processedWord import ProcessedWord
from syntaxTree import SyntaxTree
from semanticTree import SemanticTree
from semanticTree import getSynonymsString
from chat import AnimalsChat

def process(request):
	tag = Tag()
	wordProcessing = WordProcessing()
	affix = Affix()

	processedWords = []
	text = ''
	error = ''
	if request.method == 'POST':
		form = TextForm(request.POST)
		
		if "Clear" in request.POST:
			return redirect(process)

		if form.is_valid():
			form.save()

			if "File" in request.FILES:
				file = request.FILES['File'].readlines()
				for element in file:
					text = '{}'.format(element.strip()).replace("b\'", '').replace("\'", '')
			else:
				text = form.data['body']

			text = textPreprocessing(text)
			text = tag.addPosTag(text)
			text = wordProcessing.lemmatizeText(text)
			text = list(set(text))
			text.sort()

			for word in text:
				processedWords.append(ProcessedWord(word, tag.getPosTag(word)[0][1], affix.getPrefixes(word, affix.generalPrefixes)
					+ affix.getPrefixes(word, affix.negativePrefixes), affix.getSuffixes(word, affix.nounSuffixes)
					+ affix.getSuffixes(word, affix.adjectiveSuffixes)
					+ affix.getSuffixes(word, affix.verbSuffixes)
					+ affix.getSuffixes(word, affix.adverbSuffixes)))
				
			for word in processedWords:
				if not Word.objects.filter(body = word.lemma).exists():
					Word.objects.get_or_create(body=word.lemma, pos=word.pos, prefixes=word.correctPrefixes, suffixes = word.correctSuffixes)

		else:
			error = 'Form was wrong!'

	form = TextForm()
	context = {
		'form':	form,
		'error': error
	}
	return render(request, 'main/processing.html', {'context' : context, 'processedWords' : processedWords})

def generation(request):
	tag = Tag()
	wordProcessing = WordProcessing()
	affix = Affix()

	generatedWords = []

	prefixRadio = 'noPrefix'
	suffixRadio = 'noSuffix'

	prefixParam = {
		'noPrefix' : ' ',
		'generalPrefix' : affix.generalPrefixes,
		'negativePrefix' : affix.negativePrefixes
	}

	suffixParam = {
		'noSuffix' : ' ',
		'Noun' : affix.nounSuffixes,
		'Adjective' : affix.adjectiveSuffixes,
		'Verb' : affix.verbSuffixes,
		'Adverb' : affix.adverbSuffixes
	}

	error = ''
	if request.method == 'POST':
		form = WordForm(request.POST)

		if 'Prefix' in request.POST:
			prefixRadio = request.POST['Prefix']
		
		if 'Suffix' in request.POST:
			suffixRadio = request.POST['Suffix']
		
		if "Clear" in request.POST:
			return redirect(generation)

		if form.is_valid():

			word = form.data['body']
			word = textPreprocessing(word)
			word = tag.addPosTag(word)
			word = wordProcessing.lemmatizeText(word)

			if len(word) == 0:
				error = 'Please enter a word'
			else:
				generatedWords = wordProcessing.generatePossibleWords(word.pop(0), prefixParam[prefixRadio], suffixParam[suffixRadio])
				generatedWords = [word.strip() for word in generatedWords]
		else:
			error = 'Form was wrong!'

	form = WordForm()
	context = {
		'form':	form,
		'error': error
	}
	return render(request, 'main/generation.html', {'context' : context, 'generatedWords' : generatedWords})


def help(request):
	return render(request, 'main/help.html')


def savedWords(request):
	words = Word.objects.all()

	wordTypes = {
		'Noun' : 'N',
		'Adjective' : 'J',
		'Verb' : 'V',
		'Adverb' : 'R'
	}

	error = ''
	if request.method == 'POST':
		form = WordForm(request.POST)
		
		if "Clear" in request.POST:
			return redirect(savedWords)
		
		if "FilterButton" and "Filter" in request.POST:
			filterRadio = request.POST['Filter']

			wordType = wordTypes[filterRadio]
			words = Word.objects.filter(pos__startswith=wordType)
		
		if form.is_valid():
			word = form.data['body']

			if "Delete" in request.POST:
				if word == '':
					words.delete()
				else:
					Word.objects.get(body = word).delete()

			if "Find" in request.POST:
				words = Word.objects.filter(body__startswith = word)
		else:
			error = 'Form was wrong!'

	form = WordForm()
	context = {
		'form':	form,
		'error': error
	}
	return render(request, 'main/savedWords.html', {'context' : context, 'words': words})


def syntaxAnalysis(request):
	syntaxTree = SyntaxTree()

	tree = None
	text = ''
	error = ''
	if request.method == 'POST':
		form = TextForm(request.POST)
		
		if "Clear" in request.POST:
			return redirect(syntaxAnalysis)

		if form.is_valid():
			form.save()

			if "File" in request.FILES:
				file = request.FILES['File'].readlines()
				for element in file:
					text = '{}'.format(element.strip()).replace("b\'", '').replace("\'", '')
			else:
				text = form.data['body']
			
			tree = syntaxTree.generateTree(text)
			tree = syntaxTree.drawTree(tree)

			Text.objects.get_or_create(body=text, tree=tree)

		else:
			error = 'Form was wrong!'

	form = TextForm()
	context = {
		'form':	form,
		'error': error
	}
	return render(request, 'main/syntaxAnalysis.html', {'context' : context, 'tree' : tree})


def semanticAnalysis(request):
	semanticTree = SemanticTree()

	tree = None
	text = ''
	error = ''
	if request.method == 'POST':
		form = TextForm(request.POST)
		
		if "Clear" in request.POST:
			return redirect(semanticAnalysis)

		if form.is_valid():
			form.save()

			if "File" in request.FILES:
				file = request.FILES['File'].readlines()
				for element in file:
					text = '{}'.format(element.strip()).replace("b\'", '').replace("\'", '')
			else:
				text = form.data['body']
			
			tree = semanticTree.generateTree(text)
			tree = semanticTree.drawTree(tree)

			Text.objects.get_or_create(body=text, semanticTree=tree)

		else:
			error = 'Form was wrong!'

	form = TextForm()
	context = {
		'form':	form,
		'error': error
	}
	return render(request, 'main/semanticAnalysis.html', {'context' : context, 'tree' : tree})


def chat(request):
	return render(request, 'main/chat.html', {})

def chat_answer(request):
	message = request.GET.get('message').lower()
	
	animalsChat = AnimalsChat()

	answer = 'Command is not recognized. Please enter "help" for commands.'
	
	if message in getSynonymsString('help'):
		answer = '''Get all animals: animals;
					Find animals by feature: find predator;
					Get all features: features;
					Also you can use some synonyms of command names.'''
		
	elif message in getSynonymsString('animals'):
		answer = animalsChat.getAnimals()

	elif message in getSynonymsString('features'):
		answer = animalsChat.getFeatures()

	elif message.split(' ')[0] in getSynonymsString('find'):
		features =  animalsChat.getFeatures()
		feature = message.split(' ')[-1]

		if feature in features:
			answer = animalsChat.getAnimalsByFeature(feature)
		else:
			answer = f'There is not feature "{feature}"'

	return JsonResponse({
		'answer' : answer,
	})