{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "432b7c3a-d973-4370-8c75-dfe6636a5c09",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from slack_bolt import App\n",
    "from slack_bolt.adapter.socket_mode import SocketModeHandler\n",
    "from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate\n",
    "from langchain.chains.conversation.memory import ConversationalBufferWindowMemory\n",
    "\n",
    "# Initializes your app with your bot token and socket mode handler\n",
    "app = App(token=os.environ.get(\"SLACK_BOT_TOKEN\"))\n",
    "\n",
    "#Langchain implementation\n",
    "template = \"\"\"Assistant is a large language model trained by OpenAI.\n",
    "\n",
    "    Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.\n",
    "\n",
    "    Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.\n",
    "\n",
    "    Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.\n",
    "\n",
    "    {history}\n",
    "    Human: {human_input}\n",
    "    Assistant:\"\"\"\n",
    "\n",
    "prompt = PromptTemplate(\n",
    "    input_variables=[\"history\", \"human_input\"], \n",
    "    template=template\n",
    ")\n",
    "\n",
    "\n",
    "chatgpt_chain = LLMChain(\n",
    "    llm=OpenAI(temperature=0), \n",
    "    prompt=prompt, \n",
    "    verbose=True, \n",
    "    memory=ConversationalBufferWindowMemory(k=2),\n",
    ")\n",
    "\n",
    "#Message handler for Slack\n",
    "@app.message(\".*\")\n",
    "def message_handler(message, say, logger):\n",
    "    print(message)\n",
    "    \n",
    "    output = chatgpt_chain.predict(human_input = message['text'])   \n",
    "    say(output)\n",
    "\n",
    "\n",
    "\n",
    "# Start your app\n",
    "if __name__ == \"__main__\":\n",
    "    SocketModeHandler(app, os.environ[\"SLACK_APP_TOKEN\"]).start()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
