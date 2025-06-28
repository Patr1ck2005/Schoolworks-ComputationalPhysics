package enterance;

import util.Matrix;

public class MatrixCal1 {
    public static void main(String[] args) {
        var t1 = new Matrix(new double[][]{
                {0.40, 0.15, 0.15, 0.35},
                {0.00, 0.20, 0.20, 0.10},
                {0.10, 0.15, 0.15, 0.05},
                {0.50, 0.50, 0.50, 0.50}
        });
        var t2 = new Matrix(new double[][]{
                {0.50, 0.15, 0.15, 0.35},
                {0.00, 0.20, 0.20, 0.10},
                {0.00, 0.15, 0.15, 0.05},
                {0.50, 0.50, 0.50, 0.50}
        });
        var l = new Matrix(new double[][]{{1}, {0}, {0}, {0}});
        var l1 = t1.power(2).multiplyMatrix(l);
        var l2 = t2.power(2).multiplyMatrix(l);
        System.out.println("The probability that the grandson of a man from Harvard went to Harvard in case 1: " + l1.get(0, 0));
        System.out.println("The probability that the grandson of a man from Harvard went to Harvard in case 2: " + l2.get(0, 0));
    }
}
