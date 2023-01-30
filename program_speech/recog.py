from vosk import Model, KaldiRecognizer
import pyaudio
import serial 

model = Model("model")
recognizer = KaldiRecognizer(model,16000)
ser = serial.Serial('/dev/ttyACM0',9600)

mic = pyaudio.PyAudio()
stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
stream.start_stream()

while True:
    
    data = stream.read(4096)
    # print (data)
    # if len(data) == 0:
    #     break
    # print(data)
    # audio = recognizer.listen(source)
    if recognizer.AcceptWaveform(data):
        hasil = recognizer.Result()
        split_text = hasil.split(":")
        value =  split_text[1].strip().replace('"','').replace('}','').replace('\n','')
        print("Hasil ", value) 
        if (value == "sit down"):
            ser.write(b'0')
        elif (value == "stand up"):
            ser.write(b'1')
        elif (value == "hello"):
            ser.write(b'2')
        elif (value == "dancing"):
            ser.write(b'3')
        elif (value == "clap"):
            ser.write(b'4')
        # Type  {
        # "text" : ""
        # }
        # print(recognizer.Result())
        # text = recognizer.Result()
        # print(text)
        # print(text[14:-3])
        
        
