
from model import classifier

result = classifier("I need your lips now—suck my cock")
print(result)

if result[0]['score']<.49:
    print("Not toxic")
else:
    print("Toxic")