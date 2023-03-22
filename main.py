import speech_recognition as sr

def online_av():
#criando um reconhecedor:
    reconhecimento = sr.Recognizer()
#Abrindo microfone e capturando audio:
    with sr.Microphone() as source:
        while True:
            audio = reconhecimento.listen(source) #define o microfone como fonte de audio
            print(reconhecimento.recognize_google(audio, language='pt'))
online_av()
'''Código utilizado online, por isso lentidão'''