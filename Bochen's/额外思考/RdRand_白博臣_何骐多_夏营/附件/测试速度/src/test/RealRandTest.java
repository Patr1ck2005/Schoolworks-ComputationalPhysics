package test;

import util.RealRand;
import util.Vector;
import util.chat.Scatter;

import java.util.Random;

class RealRandTest {
    public static void main(String[] args) {
        var rand = new RealRand();
        int n = 100000;
        var r = new double[n];
        var y = Vector.value(Vector.line(0, 1, n));
        long startTime = System.nanoTime();
        for (int i = 0; i < n; i++) {
            r[i] = rand.nextDouble();
        }
        long endTime = System.nanoTime();
        long duration = endTime - startTime;
        System.out.println("真随机");
        System.out.println("运行时间：" + duration + "纳秒");
        System.out.println("随机数生成时间： " + (double)duration / n + "纳秒/个");
        System.out.println();
        var scatter = new Scatter(r, y);
        scatter.setTitle("True Random");
        scatter.draw();

        var rand0 = new Random();
        var r0 = new double[n];
        long startTime0 = System.nanoTime();
        for (int i = 0; i < n; i++) {
            r0[i] = rand0.nextDouble();
        }
        long endTime0 = System.nanoTime();
        long duration0 = endTime0 - startTime0;
        System.out.println("伪随机");
        System.out.println("运行时间：" + duration0 + "纳秒");
        System.out.println("随机数生成时间： " + (double)duration0 / n + "纳秒/个");
        var scatter0 = new Scatter(r0, y);
        scatter0.setTitle("Pseudo Random");
        scatter0.draw();
    }
}
