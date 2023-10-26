import RPi.GPIO as GPIO
import time

class Car:
    def __init__(self) -> None:
        # Lista de pines que deseas habilitar
        GPIO.setmode(GPIO.BCM)
        pines = [17, 18]  # Ejemplo de pines GPIO
        pwm_gpio = 12
        frequence = 50
        GPIO.setup(pwm_gpio, GPIO.OUT)
        self.pwm = GPIO.PWM(pwm_gpio, frequence)

        # Configura los pines como salida
        for pin in pines:
            GPIO.setup(pin, GPIO.OUT)


        self.pwm.start(self.angle_to_percent(0))

    def forward(self) -> None:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)

    def backward(self) -> None:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

    def stop(self) -> None:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

    def direction(self, direction: str) -> None:
        self.pwm.ChangeDutyCycle(self.angle_to_percent(int(direction)))

    @staticmethod
    def angle_to_percent (angle) :
        if angle > 180 or angle < 0 :
            return False

        start = 4
        end = 12.5
        ratio = (end - start)/180 #Calcul ratio from angle to percent

        angle_as_percent = angle * ratio

        return start + angle_as_percent

    def __del__(self) -> None:
        GPIO.cleanup()
