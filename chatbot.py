from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
bot = ChatBot('Omar')

# logic_adapters=[
  #      'chatterbot.logic.MathematicalEvaluation',
  #      'chatterbot.logic.TimeLogicAdapter',
#   ],
trainer = ListTrainer(bot)

trainer.train([
    "مرحبا!",
    "ممكن نتعرف؟",
    "اكيد!",
    "شو اسمك",
    "اسمي زكريا"

])


while True:

    # Get a response to the input text 'I would like to book a flight.'
    response = bot.get_response(input("You: "))
    print("Bot: ", response)
