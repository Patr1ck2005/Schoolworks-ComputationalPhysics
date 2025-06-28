#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <limits> // 包含此头文件以使用numeric_limitsa

bool has_rdrand() {
	uint32_t ecx, edx;
	__asm__ volatile ("cpuid" : "=c"(ecx), "=d"(edx) : "0"(1) : "ebx", "eax");
	return ecx & (1 << 30);
}

uint32_t rdrand() {
	uint32_t result;
	__asm__ volatile ("rdrand %0" : "=r"(result) : : "cc");
	return result;
}

double generate_random_double() {
	if (!has_rdrand()) {
		throw std::runtime_error("RdRand not supported on this CPU.");
	}
	
	// 使用unsigned long long的numeric_limits::max()代替uint64_t
	uint64_t random = (uint32_t)rdrand() | (((uint64_t)rdrand()) << 32);
	return static_cast<double>(random) / std::numeric_limits<unsigned long long>::max();
}

int main() {
	if (!has_rdrand()) {
		std::cout << "RdRand not supported on this CPU." << std::endl;
		return 1;
	}
	
	std::ofstream outfile("random_numbers.txt");
	if (!outfile.is_open()) {
		std::cerr << "Failed to open file for writing." << std::endl;
		return 1;
	}
	
	for (int i = 0; i < 10000; ++i) {
		double rnd = generate_random_double();
		outfile << rnd << std::endl;  // 输出到文件
	}
	
	outfile.close();  // 关闭文件流
	return 0;
}
