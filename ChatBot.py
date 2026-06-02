from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history=[
  SystemMessage(content="You are a helpful AI assistant")
]

while True:
  user_name=input("YOU: ")
  chat_history.append(HumanMessage(content=user_name))
  if user_name=="exit":
    break
  result=model.invoke(chat_history)
  chat_history.append(AIMessage(content=result.content))
  print("MAX_AI: ",result.content)


print(chat_history)
