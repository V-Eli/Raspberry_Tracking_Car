import RPi.GPIO as GPIO
import time

class Car:
    def __init__(self) -> None:
        # Lista de pines que deseas habilitar
        pines = [17, 18]  # Ejemplo de pines GPIO

        # Configura los pines como salida
        for pin in pines:
            GPIO.setup(pin, GPIO.OUT)

    def forward(self) -> None:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)

    def backward(self) -> None:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

    def stop(self) -> None:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

    def __del__(self) -> None:
        GPIO.cleanup()
