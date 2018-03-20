# Chat Bot :AAG
import cleverbot

with open('key.tar') as fp:     #File name with key in it.        
    key = fp.read()         
   
cb = cleverbot.Cleverbot(key, timeout=60)
print('Talk To CleverBot')
try:
    while(True):
        text = input()
        reply = cb.say(text)
        print(reply)
except cleverbot.CleverbotError as error:
    print(error)
finally:
    cb.close()
print('GoodBye Have a nice day')
