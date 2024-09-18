# barkod
Barkod ve Data Matrix Okuma ile Enlil İşlemleri

Bu proje, kameradan barkod ve Data Matrix kodlarını okuyarak, Data Matrix kodları için bir GUI arayüzü sunar ve barkod okunduğunda Enlil sistemi ile entegre çalışır. Enlil işlemleri için `ocr-isimoku.pyw` dosyasını kullanır.

## Özellikler

- **Barkod Tespiti**: Barkod tespit edildiğinde "Enlil işlemi" başlatılır.
- **Data Matrix Tespiti**: Data Matrix tespit edildiğinde Tkinter GUI'si açılarak, kullanıcıdan pozitif/negatif seçeneği istenir ve gerektiğinde yeni kodlar kaydedilir.
- **Kapat Tuşu**: GUI üzerinde bulunan "Kapat" tuşu, arayüzü gizler ancak kamera okuması devam eder.
- **Kopyala Tuşu**: Sonuçlar clipboard'a kopyalanır ve tuşun ismi "Kopyalandı" olarak değişir.

## Gereksinimler

Aşağıdaki kütüphanelerin kurulması gerekmektedir:

```bash
pip install opencv-python pyzbar zxing-cpp pyperclip winsound tkinter
```

### Kütüphane Açıklamaları:
- **OpenCV**: Kameradan görüntü alıp işlemek için kullanılır.
- **Pyzbar**: Barkodları ve Data Matrix kodlarını çözümlemek için kullanılır.
- **zxing-cpp**: Data Matrix ve barkodları okumak için alternatif bir kütüphane.
- **Pyperclip**: Sonuçları clipboard'a kopyalamak için kullanılır.
- **Winsound**: Sesli bildirimler için kullanılır.
- **Tkinter**: Data Matrix tespit edildiğinde GUI arayüzü oluşturmak için kullanılır.

## Projenin Kurulumu

1. Bu projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/metinciris/barkodtopatoloji.git
cd barkodtopatoloji
```

2. Gerekli Python kütüphanelerini kurun:

```bash
pip install opencv-python pyzbar zxing-cpp pyperclip winsound tkinter
```

3. Enlil işlemi için `ocr-isimoku.pyw` dosyasını kullanın. İlgili dosyayı [buradan](https://github.com/metinciris/barkodtopatoloji/blob/main/ocr-isimoku.pyw) indirebilirsiniz.

4. Ana Python dosyasını çalıştırın:

```bash
python main.py
```

## Projenin Çalışma Prensibi

- **Barkod Okuma**: Barkodda "/" karakteri varsa, Enlil işlemi başlatılır.
- **Data Matrix Okuma**: Data Matrix tespit edilirse Tkinter GUI'si açılır ve kod tanımı yapılmamışsa kaydedilir, tanımlanmışsa pozitif/negatif seçeneği sunulur.
- **Kamera**: Kamera görüntüleri sürekli işlenir ve `Kapat` tuşuna basılmadıkça işlemler devam eder.

## Katkı Yapmak

1. Bu repoyu forklayın.
2. Yeni bir branch oluşturun: `git checkout -b feature-branch`
3. Değişikliklerinizi yapın ve commit'leyin: `git commit -m 'Add new feature'`
4. Branch'inizi push'layın: `git push origin feature-branch`
5. Pull request açın.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
```

