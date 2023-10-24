import cv2

# Inicializar la captura de video desde la cámara (normalmente 0 es la cámara predeterminada).
cap = cv2.VideoCapture(1)

# Verificar si la cámara se abrió correctamente.
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Capturar un fotograma de video.
    ret, frame = cap.read()

    # Verificar si la captura fue exitosa.
    if not ret:
        print("Error: No se pudo capturar un fotograma.")
        break

    # Mostrar el fotograma en una ventana.
    cv2.imshow("Video", frame)

    # Si se presiona la tecla 'q', salir del bucle.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana.
cap.release()
cv2.destroyAllWindows()






