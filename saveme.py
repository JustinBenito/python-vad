import os
from pydub import AudioSegment
import requests

files=os.listdir('samples')
files.sort()

start=0
end=3

print(files)
while(start!=end+1):
    sound=AudioSegment.from_file("blanche.wav")
    for j in files:
        if int(j[:1])==start:
            print(j)
            sound1 = AudioSegment.from_file("samples/{file}".format(file=j), format="wav")
            sound+=sound1
    output = sound.export("merged/{}.wav".format(start))
    start+=1
    print("-----")



s_start=0
s_skip=2
s_end=3

while(s_start!=s_end):
    final=AudioSegment.from_file("blanche.wav")
    for i in range(s_start, s_skip):
        print(i)
        sound1 = AudioSegment.from_file("merged/{file}.wav".format(file=i))
        final+=sound1
    print("----")
    output = final.export("final/{}.wav".format(s_start))
    s_start+=1
    s_skip+=1




url = "http://10.9.244.20:8000/decode"

payload = {'vtt': 'true',
'language': 'english'}
files=[
  ('file',('0.wav',open('final/0.wav','rb'),'audio/wav'))
]
headers = {}

try:
    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    print(response.text)
except Exception as e:
    print(e)


