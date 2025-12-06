#include <gpiod.hpp>
#include <iostream>
#include <unistd.h>

const std::string CHIP_NAME = "gpiochip4";
const int IN1_PIN = 14; 
const int IN2_PIN = 15; 

int main() {
    try {
        gpiod::chip chip(CHIP_NAME);
        gpiod::line line_in1 = chip.get_line(IN1_PIN);
        gpiod::line line_in2 = chip.get_line(IN2_PIN);

        // 出力として要求 (初期値 LOW)
        line_in1.request({"test-motor", gpiod::line_request::DIRECTION_OUTPUT, 0}, 0);
        line_in2.request({"test-motor", gpiod::line_request::DIRECTION_OUTPUT, 0}, 0);
        std::cout << "GPIO lines acquired. Starting test." << std::endl;

        // 順方向 (extend_motor に相当)
        std::cout << "Forward (IN1=1, IN2=0)" << std::endl;
        line_in1.set_value(1);
        line_in2.set_value(0);
        sleep(2);

        // 逆方向 (shrink_motor に相当)
        std::cout << "Backward (IN1=0, IN2=1)" << std::endl;
        line_in1.set_value(0);
        line_in2.set_value(1);
        sleep(2);

        // 停止 (stop_motor に相当)
        std::cout << "Stop (IN1=0, IN2=0)" << std::endl;
        line_in1.set_value(0);
        line_in2.set_value(0);
        sleep(1);

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    std::cout << "Test finished." << std::endl;
    return 0;
}
