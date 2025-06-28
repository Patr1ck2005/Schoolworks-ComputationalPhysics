package util;

public class Vector {
    private final int dimension;
    private final double[] vector;

    public Vector(double... vector) {
        this.dimension = vector.length;
        this.vector = vector;
    }

    public static double[] value(Vector vector) {
        return vector.getVector();
    }

    public static Vector line(double x1, double x2, int dimension) {
        double[] vector = new double[dimension];
        for (int i = 0; i < dimension; i++) {
            vector[i] = x1 + (x2 - x1) * i / (dimension - 1);
        }
        return new Vector(vector);
    }

    public double[] getVector() {
        return vector;
    }

    public double get(int dimension) {
        return vector[dimension];
    }

    public Vector add(Vector other) {
        double[] result = new double[dimension];
        if (dimension != other.dimension) {
            throw new IllegalArgumentException("Vector dimensions do not match");
        }
        for (int i = 0; i < dimension; i++) {
            result[i] = vector[i] + other.vector[i];
        }
        return new Vector(result);
    }

    public double dot(Vector other) {
        if (dimension != other.dimension) {
            throw new IllegalArgumentException("Vector dimensions do not match");
        }
        double sum = 0;
        for (int i = 0; i < dimension; i++) {
            sum += vector[i] * other.vector[i];
        }
        return sum;
    }
}
