#include <stdio.h>
#include <float.h>
#include <quadmath.h>

int main() {
    // Calculate float epsilon
    float f = 1.0f;
    while (1.0f + f != 1.0f) {
        f /= 2.0f;
    }
    printf("Float epsilon: %.50e\n", f);

    // Calculate double epsilon
    double d = 1.0;
    while (1.0 + d != 1.0) {
        d /= 2.0;
    }
    printf("Double epsilon: %.50e\n", d);

    // Calculate quadruple precision epsilon
    __float128 epsilon = 1.0Q;
    
    while (1.0Q + epsilon != 1.0Q) {
        epsilon /= 2.0Q;
    }

    char buf[1024];
    quadmath_snprintf(buf, sizeof(buf), "%50.50Qe", epsilon);
    
    printf("Quadruple epsilon: %s\n", buf);

    return 0;
}

