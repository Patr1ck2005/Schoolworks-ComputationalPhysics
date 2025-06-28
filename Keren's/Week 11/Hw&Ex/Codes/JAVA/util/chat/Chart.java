package util.chat;

import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;

import javax.swing.*;
import java.awt.*;

public abstract class Chart {
    private final double[][] x;
    private final double[][] y;
    private final int n;
    private String figureTitle = "Figure";
    private int[] figureSize = {1000, 750};
    private String title = "Figure";
    private String xLabel = "x";
    private String yLabel = "y";
    private boolean setLegend = false;
    private String[] keys;
    private boolean setColors = false;
    private Color[] colors;
    private double[] sizes;
    private float[] widths;

    public Chart(double[] x, double[]... y) {
        n = y.length;
        this.x = new double[n][];
        this.y = y;
        keys = new String[n];
        sizes = new double[n];
        widths = new float[n];
        for (int i = 0; i < n; i++) {
            this.x[i] = x;
            keys[i] = "series" + (i + 1);
            sizes[i] = 2.0;
            widths[i] = 2.0f;
        }
    }

    public Chart(double[][]... data) {
        n = data.length;
        x = new double[n][];
        y = new double[n][];
        keys = new String[n];
        sizes = new double[n];
        widths = new float[n];
        for (int i = 0; i < n; i++) {
            x[i] = data[i][0];
            y[i] = data[i][1];
            keys[i] = "series" + (i + 1);
            sizes[i] = 2.0;
            widths[i] = 2.0f;
        }
    }

    public double[][] getX() {
        return x;
    }

    public double[][] getY() {
        return y;
    }

    public int getN() {
        return n;
    }

    public void setFigureTitle(String figureTitle) {
        this.figureTitle = figureTitle;
    }

    public void setFigureSize(int... figureSize) {
        this.figureSize = figureSize;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getXLabel() {
        return xLabel;
    }

    public void setXLabel(String xLabel) {
        this.xLabel = xLabel;
    }

    public String getYLabel() {
        return yLabel;
    }

    public void setYLabel(String yLabel) {
        this.yLabel = yLabel;
    }

    public boolean isSetLegend() {
        return setLegend;
    }

    public String[] getKeys() {
        return keys;
    }

    public void setKeys(String... keys) {
        if (keys.length != n) {
            throw new IllegalArgumentException("The number of keys does not match the number of series");
        }
        setLegend = true;
        this.keys = keys;
    }

    public boolean isSetColors() {
        return setColors;
    }

    public Color[] getColors() {
        return colors;
    }

    public void setColors(Color... colors) {
        if (colors.length != n) {
            throw new IllegalArgumentException("The number of colors does not match the number of series");
        }
        setColors = true;
        this.colors = colors;
    }

    public double[] getSizes() {
        return sizes;
    }

    public void setSizes(double... sizes) {
        if (sizes.length != n) {
            throw new IllegalArgumentException("The number of sizes does not match the number of series");
        }
        this.sizes = sizes;
    }

    public float[] getWidths() {
        return widths;
    }

    public void setWidths(float... widths) {
        if (widths.length != n) {
            throw new IllegalArgumentException("The number of widths does not match the number of series");
        }
        this.widths = widths;
    }

    public void draw() {
    }

    public void display(JFreeChart chart) {
        JFrame frame = new JFrame(figureTitle);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new Dimension(figureSize[0], figureSize[1]));
        frame.add(chartPanel, BorderLayout.CENTER);
        frame.pack();
        frame.setVisible(true);
    }
}
