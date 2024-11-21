from nltk.chat.util import Chat,reflections
reflections
print("hey guys I'm a rule based chatbot")
pairs=[
    ['gm',['good morning']],
    ['afternoon',['good afternoon']],
    ['good evening',['good evening']],
    ['I need help',['hey how can i help you']],
    ['who is the PM of India' ,['hello  the pm of india is NArendra MODI ji' ]],
    ['when did India get independence',['india got its  independence on 15th AUG 1947' ]],
    ['how many countries are there in the world',['there are 195 countries in the world']],
    ['need to know the best channel to learn dsa' ,['well u have 2 to 3 but go for (1)code with harry,(2)jenny']],
    ['why do we need chatbot',['Chatbots are important for businesses because they can help with customer service, operational efficiency, and cost savings']],
    ['exit',['thank u do visit again with doubts']]
]
chat=Chat(pairs,reflections)
chat.converse()