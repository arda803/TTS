# TTS
You can test your word knowledge with this app!
# 🎤 Doğru Konuş — Kurulum Rehberi

Bu projeyi çalıştırmak için bilgisayarınızda **Python 3.11 veya üzeri** bulunmalıdır.

## 1. Projeyi İndirin

Projeyi bilgisayarınıza indirin veya GitHub üzerinden klonlayın.

Terminali proje klasöründe açın:

```bash
cd "proje-klasörünün-konumu"
```

## 2. Gerekli Kütüphaneleri Yükleyin

Terminale aşağıdaki komutu yazın:

```bash
pip install sounddevice scipy SpeechRecognition googletrans==4.0.2
```

Kütüphanelerin doğru yüklendiğini kontrol etmek için:

```bash
pip show sounddevice
pip show scipy
pip show SpeechRecognition
pip show googletrans
```

## 3. Programı Çalıştırın

Proje klasöründe terminali açtıktan sonra:

```bash
python main.py
```

Program açıldığında önce kullanmak istediğiniz dili seçin:

```text
Dil seçin (tr, en, fr, es, ru, de, it, pt):
```

Örneğin:

```text
en
```

Daha sonra zorluk seviyesini seçin:

```text
Zorluk seviyesini seçin (kolay, orta, zor):
```

Örneğin:

```text
kolay
```

## 4. Mikrofon İzni

Program konuşmanızı algılamak için mikrofonunuzu kullanır.

İlk çalıştırmada Windows mikrofon izni isterse **İzin Ver** seçeneğini kullanın.

Mikrofonunuzun çalıştığından emin olun.

## 5. Desteklenen Diller

Program aşağıdaki dilleri destekler:

| Kod | Dil |
|---|---|
| `tr` | Türkçe |
| `en` | İngilizce |
| `fr` | Fransızca |
| `es` | İspanyolca |
| `ru` | Rusça |
| `de` | Almanca |
| `it` | İtalyanca |
| `pt` | Portekizce |

## 6. Sorun Giderme

### `ModuleNotFoundError` hatası

Örneğin:

```text
ModuleNotFoundError: No module named 'sounddevice'
```

gibi bir hata alırsanız gerekli kütüphaneyi tekrar yükleyin:

```bash
pip install sounddevice scipy SpeechRecognition googletrans==4.0.2
```

### Mikrofon çalışmıyorsa

Windows'ta:

**Ayarlar → Gizlilik ve güvenlik → Mikrofon**

bölümünden Python'un mikrofon erişiminin açık olduğundan emin olun.

### Googletrans ile ilgili hata

Googletrans'ın doğru sürümünün kurulu olduğundan emin olun:

```bash
pip install --upgrade googletrans==4.0.2
```

Kurulu sürümü kontrol etmek için:

```bash
pip show googletrans
```

Sürümün `4.0.2` olduğunu kontrol edin.

## 🚀 Hazırsınız!

Kurulum tamamlandıktan sonra:

```bash
python main.py
```

komutuyla **Doğru Konuş** oyununu başlatabilirsiniz. 🎤
