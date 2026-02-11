import cv2 #import module opencv
import mediapipe
capture = cv2.VideoCapture(0) #video capture pada device kamera NO.1
mediapipehand = mediapipe.solutions.hands #inisialisasi deteksi tangan
tangan = mediapipehand.Hands() #variable tangan untuk menyimpan konfigurasi

while True:
    success, img = capture.read() #menyimpan screenshot kamera ke img
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #mengubah warna img ke RGB
    result = tangan.process(imgRGB) #melakukan pemrosesan dari citra imgRGB
    if result.multi_hand_landmarks:
        print("tangan") #ketikan tangan terdeteksi menampilkan "tangan" pada terminal
    else:
        print("tidak ada") #ketikan tangan terdeteksi menampilka "tidak ada" pada terminal
    cv2.imshow("img", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
capture.release() #tutup webcam dan jendela tampilan saat 1 ditekan
cv2.destroyAllWindows()