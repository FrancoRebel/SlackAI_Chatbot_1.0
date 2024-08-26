import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory

# Initializes your app with your bot token
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
def message_handler(message, say):
    print(message)
    
    output = chatgpt_chain.predict(human_input=message['text'])
    say(output)

# Entry point for Vercel
def handler(request):
    # The handler function does not need to start the SocketModeHandler directly,
    # because SocketModeHandler should already be running with your Vercel deployment.
    return {
        'statusCode': 200,
        'body': 'Bot is running'
    }

# Start your bot using Socket Mode
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
