package util;

import java.util.AbstractCollection;
import java.util.Arrays;
import java.util.Iterator;

/**
 * A matrix class representing a two-dimensional array of double values.
 */
public class Matrix extends AbstractCollection<Double> {
    private final double[][] x;
    private final int column;
    private final int row;

    /**
     * Constructs a Matrix object from a 2D array of double values.
     *
     * @param x The 2D array representing the matrix.
     */
    public Matrix(double[][] x) {
        this.x = x.clone();
        this.column = x.length;
        this.row = x[0].length;
    }

    /**
     * Creates a new Matrix object filled with zeros.
     *
     * @param column The number of columns.
     * @param row    The number of rows.
     * @return A Matrix object filled with zeros.
     */
    public static Matrix zeros(int column, int row) {
        double[][] x = new double[column][row];
        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                x[i][j] = 0.0;
            }
        }
        return new Matrix(x);
    }

    /**
     * Creates a new Matrix object with diagonal elements set to one and the rest to zero.
     *
     * @param column The number of columns.
     * @param row    The number of rows.
     * @return A Matrix object with diagonal elements set to one.
     */
    public static Matrix ones(int column, int row) {
        double[][] x = new double[column][row];
        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                x[i][j] = (i == j) ? 1.0 : 0.0;
            }
        }
        return new Matrix(x);
    }

    /**
     * Creates a new Matrix object with the diagonal elements set according to the provided array.
     *
     * @param v The array containing the diagonal elements.
     * @return A Matrix object with the diagonal elements set according to the provided array.
     */
    public static Matrix diag(double[] v) {
        double[][] x = new double[v.length][v.length];
        for (int i = 0; i < v.length; i++) {
            for (int j = 0; j < v.length; j++) {
                x[i][j] = (i == j) ? v[i] : 0.0;
            }
        }
        return new Matrix(x);
    }

    /**
     * Retrieves the underlying 2D array of the Matrix.
     *
     * @return The 2D array representing the Matrix.
     */
    public double[][] getX() {
        return x.clone();
    }

    /**
     * Retrieves the number of rows in the Matrix.
     *
     * @return The number of rows.
     */
    public int getColumn() {
        return column;
    }

    /**
     * Retrieves the number of columns in the Matrix.
     *
     * @return The number of columns.
     */
    public int getRow() {
        return row;
    }

    /**
     * Retrieves the value at the specified row and column in the Matrix.
     *
     * @param column The column index.
     * @param row    The row index.
     * @return The value at the specified position.
     */
    public double get(int column, int row) {
        return x[column][row];
    }

    /**
     * Sets the value at the specified row and column in the Matrix.
     *
     * @param column The column index.
     * @param row    The row index.
     * @param value  The value to set.
     */
    public void set(int column, int row, double value) {
        x[column][row] = value;
    }

    /**
     * Checks whether this Matrix is equal to another Matrix.
     *
     * @param other The Matrix to compare.
     * @return True if the matrices are equal, false otherwise.
     */
    public boolean equals(Matrix other) {
        return Arrays.deepEquals(x, other.x);
    }

    @Override
    public Iterator<Double> iterator() {
        return new MatrixIterator();
    }

    @Override
    public int size() {
        return column * row;
    }


    /**
     * Get the sting of the elements in matrix
     *
     * @return string of the elements in matrix
     */
    public String display() {
        StringBuilder s = new StringBuilder();
        int n = 0;
        for (double e : this) {
            s.append(e);
            n++;
            if (n < row) {
                s.append("\t");
            } else {
                s.append("\n");
                n = 0;
            }
        }
        return s.toString();
    }

    /**
     * Transposes this Matrix, swapping rows and columns.
     *
     * @return The transposed Matrix.
     */
    public Matrix transpose() {
        var x = new double[row][column];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                x[i][j] = this.x[j][i];
            }
        }
        return new Matrix(x);
    }

    /**
     * Adds another Matrix to this Matrix element-wise.
     *
     * @param other The Matrix to add.
     * @return The resulting Matrix after addition.
     * @throws IllegalArgumentException if the sizes of the matrices do not match.
     */
    public Matrix addMatrix(Matrix other) {
        if (column != other.column || row != other.row) {
            throw new IllegalArgumentException("Matrix size does not match");
        }
        var x = new double[column][row];
        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                x[i][j] = this.x[i][j] + other.x[i][j];
            }
        }
        return new Matrix(x);

    }

    /**
     * Multiplies this Matrix by a scalar value.
     *
     * @param k The scalar value to multiply by.
     * @return The resulting Matrix after multiplication.
     */
    public Matrix multiplyNumber(double k) {
        var x = new double[column][row];
        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                x[i][j] = this.x[i][j] * k;
            }
        }
        return new Matrix(x);
    }

    /**
     * Multiplies this Matrix by another Matrix.
     *
     * @param other The Matrix to multiply by.
     * @return The resulting Matrix after multiplication.
     * @throws IllegalArgumentException if the matrices cannot be multiplied due to incompatible sizes.
     */
    public Matrix multiplyMatrix(Matrix other) {
        if (row != other.column) {
            throw new IllegalArgumentException("Matrix size does not match");
        } else {
            var x = new double[column][other.row];
            for (int i = 0; i < column; i++) {
                for (int j = 0; j < other.row; j++) {
                    for (int k = 0; k < row; k++) {
                        x[i][j] += this.x[i][k] * other.x[k][j];
                    }
                }
            }
            return new Matrix(x);
        }
    }

    /**
     * Calculates the power of Matrix of index n.
     *
     * @param n the index of power.
     * @return the power.
     */
    public Matrix power(int n) {
        if (column != row) {
            throw new IllegalArgumentException("Matrix is not square");
        }
        var matrix = this;
        for (int i = 0; i < n - 1; i++) {
            matrix = matrix.multiplyMatrix(this);
        }
        return matrix;

    }

    /**
     * Calculates the determinant of this square Matrix.
     *
     * @return The determinant value.
     * @throws IllegalArgumentException if the Matrix is not square.
     */
    public double determinant() {
        if (column != row) {
            throw new IllegalArgumentException("Matrix is not square");
        } else if (column == 1) {
            return x[0][0];
        } else if (column == 2) {
            return x[0][0] * x[1][1] - x[0][1] * x[1][0];
        }

        double determinant = 0;
        for (int i = 0; i < row; i++) {
            determinant += x[0][i] * cofactor(0, i) * (i % 2 == 0 ? 1 : -1);
        }
        return determinant;

    }

    /**
     * Calculates the inverse of this Matrix.
     *
     * @return The inverse Matrix.
     * @throws IllegalArgumentException if the Matrix is not invertible (determinant is zero).
     */
    public Matrix inverse() {
        if (determinant() == 0) {
            throw new IllegalArgumentException("Determinant is zero");
        }

        double[][] x = new double[column][row];
        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                x[i][j] = cofactor(j, i) * ((i + j) % 2 == 0 ? 1 : -1) / determinant();
            }
        }
        return new Matrix(x);

    }

    /**
     * Calculates the cofactor of a specific element in the Matrix.
     *
     * @param rowToRemove The row index to remove.
     * @param colToRemove The column index to remove.
     * @return The cofactor value.
     */
    private double cofactor(int rowToRemove, int colToRemove) {
        double[][] cofactorMatrix = new double[column - 1][row - 1];
        int rowIndex = 0;
        for (int i = 0; i < column; i++) {
            if (i == rowToRemove) {
                continue;
            }
            int colIndex = 0;
            for (int j = 0; j < row; j++) {
                if (j == colToRemove) {
                    continue;
                }
                cofactorMatrix[rowIndex][colIndex++] = x[i][j];
            }
            rowIndex++;
        }
        return new Matrix(cofactorMatrix).determinant();
    }

    /**
     * An iterator implementation for iterating over the elements of the Matrix.
     */
    private class MatrixIterator implements Iterator<Double> {
        private int rowIndex = 0;
        private int colIndex = 0;

        @Override
        public boolean hasNext() {
            return rowIndex < column && colIndex < row;
        }

        @Override
        public Double next() {
            if (!hasNext()) {
                throw new IndexOutOfBoundsException("No more elements in the matrix");
            }
            double element = x[rowIndex][colIndex++];
            if (colIndex == row) {
                colIndex = 0;
                rowIndex++;
            }
            return element;
        }
    }
}
