from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer



bot = ChatBot('chatbot', readonly=False, logic_adapters=[
	{
		'import_path': 'chatterbot.logic.BestMatch',
		# 'default_response' : 'Sorry! I dont know what that means!',
		# 'maximum_similarity_threshold' : 0.95

	}
	])

list_to_train = [
	
	"hi",
	"hi there!",
	"what's your name?",
	"I'm just a chatbot :)",
	"what's your favorite food?",
	"I like Pitzza!",
	"what's your favorite sport?",
	"football!",
	"Do you have children?!",
	"No!",

]


chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)


# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)


chatterbotCorpusTrainer.train('chatterbot.corpus.english') # You can change this sactieon for your own/fav language. "english" ---> "any language you want to train"


def index(request):
	return render(request, 'blog/index.html')


def specific(request):
	return HttpResponse("This is the specific url")


def getResponse(request):
	userMessage = request.GET.get('userMessage')
	chatResponse = str(bot.get_response(userMessage))
	return HttpResponse(chatResponse)