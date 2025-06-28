package util.chat;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.awt.*;

public class Plot extends Chart {

    public Plot(double[] x, double[]... y) {
        super(x, y);
    }

    public Plot(double[][]... data) {
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
        var widths = getWidths();

        XYSeriesCollection dataset = new XYSeriesCollection();
        XYSeries[] series = new XYSeries[n];
        for (int i = 0; i < n; i++) {
            series[i] = new XYSeries(keys[i]);
            for (int j = 0; j < y[i].length; j++) {
                series[i].add(x[i][j], y[i][j]);
            }
            dataset.addSeries(series[i]);
        }

        JFreeChart chart = ChartFactory.createXYLineChart(getTitle(), getXLabel(), getYLabel(), dataset,
                PlotOrientation.VERTICAL, isSetLegend(), true, false);

        XYPlot plot = chart.getXYPlot();
        plot.setDomainPannable(true);
        plot.setRangePannable(true);

        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();
        plot.setRenderer(renderer);

        if (renderer instanceof XYLineAndShapeRenderer lineAndShapeRenderer) {
            for (int i = 0; i < n; i++) {
                lineAndShapeRenderer.setSeriesStroke(i, new BasicStroke(widths[i]));
                lineAndShapeRenderer.setSeriesShape(i, new java.awt.geom.Ellipse2D.Double(-sizes[i] / 2, -sizes[i] / 2, sizes[i], sizes[i]));
                if (isSetColors()) {
                    lineAndShapeRenderer.setSeriesPaint(i, colors[i]);
                }
            }
        }

        display(chart);
    }
}
