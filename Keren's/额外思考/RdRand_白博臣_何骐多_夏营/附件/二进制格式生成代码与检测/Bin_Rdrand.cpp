#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <limits>
#include <string>
#include <filesystem> // 使用C++17的文件系统库来创建目录

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

bool create_directory_if_not_exists(const std::string& dir) {
	std::filesystem::path p(dir);
	if (!std::filesystem::exists(p)) {
		std::filesystem::create_directories(p);
		return true;
	}
	return false;
}

void generate_random_sample(const std::string& filename) {
	if (!has_rdrand()) {
		throw std::runtime_error("RdRand not supported on this CPU.");
	}
	
	std::ofstream outfile(filename, std::ios::binary);
	if (!outfile.is_open()) {
		std::cerr << "Failed to open file for writing: " << filename << std::endl;
		return;
	}
	
	for (int i = 0; i < 1000000 / (sizeof(uint32_t) * 8); ++i) {
		uint32_t random = rdrand();
		outfile.write(reinterpret_cast<char*>(&random), sizeof(random));
	}
	
	outfile.close();
}

int main() {
	if (!has_rdrand()) {
		std::cout << "RdRand not supported on this CPU." << std::endl;
		return 1;
	}
	
	std::string target_dir = "target\\data";
	if (!create_directory_if_not_exists(target_dir)) {
		std::cerr << "Failed to create directory: " << target_dir << std::endl;
		return 1;
	}
	
	for (int i = 0; i < 1000; ++i) {
		std::string filename = target_dir + "\\" + "sample_" + std::to_string(i) + ".bin";
		generate_random_sample(filename);
	}
	
	return 0;
}
