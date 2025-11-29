from gpiozero import OutputDevice
import time

# ピン番号の定義 (BCMモード = GPIO番号で指定)
IN1_PIN = 14  # GPIO 14
IN2_PIN = 15  # GPIO 15

# setup() の代わりに、ここでオブジェクトを作成します
# これでピンが自動的に出力モードに設定されます
in1 = OutputDevice(IN1_PIN)
in2 = OutputDevice(IN2_PIN)

def motor_control():
    """モーター制御のシーケンス"""
    
    # 正転
    print("正転 (Forward)")
    in1.on()   # RPi.GPIOの High
    in2.off()  # RPi.GPIOの Low
    time.sleep(2)

    # ブレーキ
    print("ブレーキ (Brake)")
    in1.on()
    in2.on()
    time.sleep(2)

    # 逆転
    print("逆転 (Backward)")
    in1.off()
    in2.on()
    time.sleep(2)

    # 停止（惰性）
    print("停止 (Coast)")
    in1.off()
    in2.off()
    time.sleep(2)

def main():
    """メイン処理"""
    try:
        while True:  # Arduinoのloop()に相当
            motor_control()
            
    except KeyboardInterrupt:
        # Ctrl+C でプログラムを終了したとき
        print("\nプログラムを終了します。")
        
    finally:
        # RPi.GPIO.cleanup() の代わりに、デバイスを閉じる
        # （実際には try ブロックの外に出た時点で自動でクリーンアップされますが
        #  明示的に書いておくと確実です）
        in1.close()
        in2.close()
        print("GPIOクリーンアップ完了")

# このスクリプトが直接実行された場合にmain()関数を呼び出す
if __name__ == "__main__":
    main()
