

---

## Proje Kapsam Dosyası: AI Görsel İşleme Merkezi

**1. Proje Adı:**  
AI Görsel İşleme Merkezi

**2. Proje Amacı:**  
Bu proje, Stability AI API'sini kullanarak kullanıcıların metin açıklamalarından görseller üretmelerine ve mevcut görseller üzerinde varyasyonlar oluşturmalarına olanak tanıyan interaktif bir web uygulaması geliştirmeyi amaçlamaktadır. Uygulama, Streamlit kütüphanesi ile kullanıcı dostu bir arayüz sunacaktır.

**3. Ana Özellikler:**

- **Metinden Görsel Oluşturma:**
  
  - Kullanıcının girdiği metin açıklamasına (prompt) göre görsel üretme.
  
  - Üretilecek görselin genişlik ve yükseklik ayarlarını belirleyebilme.
  
  - Oluşturulan görseli arayüzde sergileme.

- **Görsel Varyasyonu Oluşturma:**
  
  - Kullanıcının bir temel görsel yüklemesine izin verme.
  
  - Yüklenen görsele ve isteğe bağlı bir metin açıklamasına (prompt) dayanarak yeni görsel varyasyonları oluşturma.
  
  - Oluşturulan varyasyon görselini arayüzde sergileme.

- **API Entegrasyonu:**
  
  - Stability AI API'si (v1.0, stable-diffusion-xl-1024-v1-0 motoru) ile güvenli ve etkili iletişim.
  
  - API çağrıları için merkezi bir helper fonksiyonu.

- **Kullanıcı Arayüzü:**
  
  - Streamlit kullanılarak oluşturulmuş, anlaşılır ve kolay kullanımlı bir web arayüzü.
  
  - Genişletilebilir bölümler (expander) ile farklı özellikleri gruplama.
  
  - Görsel yükleme, metin girişi ve sayısal giriş alanları.
  
  - İşlem sırasında kullanıcıyı bilgilendirmek için yükleme göstergeleri (spinner).
  
  - Hata mesajlarını kullanıcıya gösterme.

**4. Kullanılan Teknolojiler:**

- **Programlama Dili:** Python

- **Web Framework:** Streamlit

- **API İstemcisi:** Requests

- **Görsel İşleme:** Pillow (PIL)

- **Ortam Değişkenleri Yönetimi:** python-dotenv

- **Veri Formatları:** JSON, Base64 (görseller için)

- **Harici API:** Stability AI API

**5. Hedef Kitle:**

- Yapay zeka ile görsel üretimi ve düzenlemesi yapmak isteyen tasarımcılar.

- İçerik üreticileri.

- Geliştiriciler ve AI meraklıları.

**6. Kısıtlamalar ve Varsayımlar:**

- Kullanıcının geçerli bir Stability AI API anahtarına sahip olması gerekmektedir.

- Uygulamanın çalışması için aktif bir internet bağlantısı zorunludur.

- API kullanım limitleri Stability AI tarafından belirlenen koşullara tabidir.

- Şu anki sürümde inpainting ve outpainting fonksiyonları kodda tanımlanmış olsa da, kullanıcı arayüzünde bu özellikler için bir bölüm bulunmamaktadır. (Gelecekte eklenebilir.)

---

## Nasıl Çalıştırılır?

Bu Streamlit uygulamasını çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

**1. Ön Koşullar:**

- Python 3.7 veya daha üstü bir sürümün yüklü olması.

- pip paket yöneticisinin kurulu olması.

**2. Proje Dosyalarının Hazırlanması:**

- Verilen kodu streamlitimage.py (veya istediğiniz başka bir .py uzantılı dosya adı) olarak kaydedin.

- Aynı dizinde .env adında bir dosya oluşturun.

**3. Gerekli Kütüphanelerin Kurulumu:**  
Terminali veya komut istemcisini açın ve proje dizinine gidin. Ardından aşağıdaki komutları çalıştırarak gerekli Python kütüphanelerini yükleyin:

      `pip install streamlit requests Pillow python-dotenv`

**4. API Anahtarının Ayarlanması:**

- Stability AI platformundan bir API anahtarı edinin.

- Proje dizininde oluşturduğunuz .env dosyasını açın ve içine aşağıdaki satırı ekleyin. YOUR_STABILITY_AI_API_KEY kısmını kendi API anahtarınızla değiştirin:
  
        `STABILITY_API_KEY="YOUR_STABILITY_AI_API_KEY"`



**5. Uygulamanın Çalıştırılması:**  
Terminalde veya komut istemcisinde, streamlitimage.py dosyasının bulunduğu dizindeyken aşağıdaki komutu çalıştırın:

      `streamlit run streamlitimage.py`



Bu komut çalıştırıldıktan sonra, Streamlit uygulaması varsayılan web tarayıcınızda otomatik olarak açılacaktır. Genellikle http://localhost:8501 adresinden erişilebilir.

**6. Kullanım:**

- Açılan web sayfasında "Metinden Görsel Oluştur" bölümünden istediğiniz açıklamayı girip, boyutları ayarlayarak yeni görseller üretebilirsiniz.

- "Görsel Varyasyonu" bölümünden bir görsel yükleyip, isteğe bağlı bir açıklama ile bu görselin farklı varyasyonlarını oluşturabilirsiniz.

Artık AI Görsel İşleme Merkezi'ni kullanmaya başlayabilirsiniz!
