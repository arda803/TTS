import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import random
from googletrans import Translator

number = random.randint(1, 10)

words = {
    "kolay": ["kedi", "köpek", "elma", "süt", "güneş", "araba", "ev", "masa", "kitap", "çanta"],
    "orta": ["muz", "okul", "arkadaş", "pencere", "sarı", "telefon", "bilgisayar", "çorap", "çorba", "çocuk"],
    "zor": ["teknoloji", "üniversite", "bilgi", "telaffuz", "hayal gücü", "deneyim", "yaratıcılık", "sorumluluk", "özgürlük", "farkındalık", "çevre", "toplum", "kültür", "sanat", "edebiyat", "psikoloji", "felsefe", "bilim", "matematik", "astronomi", "biyoloji", "kimya", "fizik", "tarih", "coğrafya", "ekonomi", "siyaset", "hukuk", "sağlık", "spor", "müzik", "dans", "tiyatro", "sinema", "fotoğrafçılık", "yazılım", "donanım", "robotik", "yapay zeka", "uzay araştırmaları", "iklim değişikliği", "sürdürülebilirlik", "enerji kaynakları", "tarım", "gıda güvenliği", "su kaynakları", "ormanlar", "denizler", "hava durumu", "jeoloji", "arazi kullanımı", "ulaşım", "turizm"]
}

duration = 5
sample_rate = 44100

language = input("Dil seçin (tr, en, fr, es, ru, de, it, pt): ").lower()

if language not in ["tr", "en", "fr", "es", "ru", "de", "it", "pt"]:
    print("Girdiğiniz dil bulunmamakta.")
else:
    option = input("Zorluk seviyesini seçin (kolay, orta, zor): ").lower()

    if option not in words:
        print("Girdiğiniz zorluk seviyesi bulunmamakta.")
    else:
        print(option.capitalize(), "zorluk seviyesi seçildi!")
        selected_words = random.sample(words[option], number)
        translator = Translator()

        for word in selected_words:
            print("\n🇹🇷 Türkçe kelime:", word)
            print("Bu kelimenin seçtiğiniz dildeki karşılığını söyleyin!")

            try:
                translated = translator.translate(word, src="tr", dest=language)
                correct_answer = translated.text.lower().strip()
            except Exception as e:
                print("❌ Çeviri yapılamadı:", e)
                break

            print("🎤 Konuşmaya başlayın...")

            recording = sd.rec(
                int(duration * sample_rate),
                samplerate=sample_rate,
                channels=1,
                dtype="int16"
            )

            sd.wait()
            wav.write("output.wav", sample_rate, recording)

            print("⏹️ Kayıt tamamlandı!")

            recognizer = sr.Recognizer()

            with sr.AudioFile("output.wav") as source:
                audio = recognizer.record(source)

            try:
                text = recognizer.recognize_google(
                    audio,
                    language=language
                ).lower().strip()

                print("🗣️ Söylediğiniz:", text)

                if text == correct_answer:
                    print("✅ Doğru!")
                else:
                    print("❌ Yanlış!")
                    print("Doğru cevap:", correct_answer)

            except sr.UnknownValueError:
                print("❌ Konuşma tanınamadı.")

            except sr.RequestError as e:
                print(f"❌ Hizmet hatası: {e}")