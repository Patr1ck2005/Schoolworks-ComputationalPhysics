package util.chat;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYItemRenderer;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.DefaultXYDataset;

public class Scatter extends Chart {

    public Scatter(double[] x, double[]... y) {
        super(x, y);
    }

    public Scatter(double[][]... data) {
        super(data);
    }

    @Override
    public void draw() {
        var x = getX();
        var y = getY();
        var n = y.length;
        var keys = getKeys();
        var colors = getColors();
        var sizes = getSizes();
        DefaultXYDataset dataset = new DefaultXYDataset();
        for (int i = 0; i < n; i++) {
            dataset.addSeries(keys[i], new double[][]{x[i], y[i]});
        }
        JFreeChart chart = ChartFactory.createScatterPlot(getTitle(), getXLabel(), getYLabel(), dataset,
                PlotOrientation.VERTICAL, isSetLegend(), true, false);

        XYPlot plot = (XYPlot) chart.getPlot();
        XYItemRenderer renderer = plot.getRenderer();
        if (renderer instanceof XYLineAndShapeRenderer lineAndShapeRenderer) {
            for (int i = 0; i < getN(); i++) {
                lineAndShapeRenderer.setSeriesShape(i, new java.awt.geom.Ellipse2D.Double(-sizes[i] / 2, -sizes[i] / 2, sizes[i], sizes[i]));
                if (isSetColors()) {
                    lineAndShapeRenderer.setSeriesPaint(i, colors[i]);
                }
            }
        }

        display(chart);
    }
}
