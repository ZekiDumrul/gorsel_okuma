import cv2

# Resim dosyasýnýn yolu (masaüstündeki resim)
resim_yolu = r"C:\Users\Zeki\Desktop\resim\manzara.webp"  

# Resmi oku
resim = cv2.imread(resim_yolu)

if resim is None:
    print("Resim bulunamadi")
else:
    # Resmi göster
    cv2.imshow("Image", resim)

    # Resmi kaydet
    cv2.imwrite("copied_image.png", resim)
    print("Image kaydedildi: copied_image.png")

    # Pencereyi kapatmak için tuþa bas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
