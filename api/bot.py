import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Langchain implementation
template = """Assistant is a large language model trained by OpenAI.

{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "human_input"], 
    template=template
)

chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationalBufferWindowMemory(k=2),
)

# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    print(message)
    
    output = chatgpt_chain.predict(human_input=message['text'])   
    say(output)

# This is the entry point for Vercel
def handler(request):
    if request.method == 'POST':
        SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    return {
        'statusCode': 200,
        'body': 'Bot is running'
    }
