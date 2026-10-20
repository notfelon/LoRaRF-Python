from LoRaRF import SX126x, LoRaSpi, LoRaGpio
import time

spi = LoRaSpi(1, 0)  # Вы используете SPI1, cs_id обычно 0

# Параметры LoRaGpio: (gpiochip, line_number)
# Используйте номера линий, которые вы нашли ранее через gpioinfo
cs = LoRaGpio(0, 324)      # ваш PK3 (CS)
reset = LoRaGpio(0, 320)   # ваш reset
busy = LoRaGpio(0, 323)    # ваш busy
irq = LoRaGpio(0,321)
tx_en = LoRaGpio(0,326)
# Затем передайте их в SX126x
LoRa = SX126x(spi, cs, reset, busy, irq, tx_en)

LoRa.begin()
# Настройка параметров
LoRa.setFrequency(868000000)          # 868 МГц
LoRa.setTxPower(22, LoRa.TX_POWER_SX1262)
LoRa.setLoRaModulation(9, 250000, 5)  # SF9, BW250 кГц, CR 4/5
LoRa.setLoRaPacket(LoRa.HEADER_EXPLICIT, 12, 0, True)

print("Start sending...")
while True:
    LoRa.beginPacket()
    message = "HeLoRa World!\0"
    messageList = list(message)
    for i in range(len(messageList)) : messageList[i] = ord(messageList[i])
    LoRa.write(messageList,1)
    LoRa.endPacket()
    print("Sent: hello lora")
    time.sleep(5)
