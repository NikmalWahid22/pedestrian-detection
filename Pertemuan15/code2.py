import cv2
import imutils

# Menginisialisasi detektor orang HOG
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('vid.mp4')

while cap.isOpened():
    # Membaca streaming video
    ret, image = cap.read()
    
    if ret:
        # Mengubah ukuran gambar
        image = imutils.resize(image, width=min(400, image.shape[1]))
        
        # Mendeteksi semua wilayah dalam Gambar yang memiliki pejalan kaki di dalamnya
        (regions, _) = hog.detectMultiScale(
            image, 
            winStride=(4, 4), 
            padding=(4, 4), 
            scale=1.05
        )
        
        # Menggambar wilayah di Gambar
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
        # Menampilkan Gambar keluaran
        cv2.imshow("Image", image)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()