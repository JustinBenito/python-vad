import auditok
import os

prev=0

def chunkme(file,num):
    path='hls-incoming-add-input-files-here/{file}'.format(file=file)
    audio_region = auditok.split(
    path,
    min_dur=0.2,     
    max_dur=3,       
    max_silence=0.01, 
    energy_threshold=60 
    )
    for i, r in enumerate(audio_region):
        filename = r.save("samples/{num}{i}.wav".format(i=i, r=r,num=num-1))
        print("region saved as: {i}".format(i=filename))
    os.remove(path)

while(True):
    if len(os.listdir('hls-incoming-add-input-files-here'))>0:
        prev=prev+1
        chunks=os.listdir("hls-incoming-add-input-files-here")
        file=chunks[0]

        chunkme(file,prev)
    




# audio_array= ['obs-0.ts', 'obs-1.ts']

# while(audio_array!=[]):
    # audio_region = auditok.split(
    # audio_array[0],
    # min_dur=0.2,     
    # max_dur=3,       
    # max_silence=0.01, 
    # energy_threshold=60 
    # )

    # for i, r in enumerate(audio_region):

    #     print("Region {i}: {r.meta.start:.3f}s -- {r.meta.end:.3f}s".format(i=i, r=r))

    #     filename = r.save("region_{i}:{r.meta.start:.3f}-{r.meta.end:.3f}.wav".format(i=i, r=r))
    #     print("region saved as: {}".format(filename))

    # audio_array.pop(0)