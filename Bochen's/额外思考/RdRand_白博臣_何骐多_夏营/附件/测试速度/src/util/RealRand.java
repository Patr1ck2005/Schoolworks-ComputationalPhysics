package util;

import com.github.javachaos.jrdrand.RdRand;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class RealRand extends RdRand {

    public static final BigDecimal maxLongBigDecimal = new BigDecimal(Long.MAX_VALUE);

    public double nextDouble(double min, double max) {
        return new BigDecimal(min).add(nextRandFromN1ToP1().add(new BigDecimal(1)).divide(new BigDecimal(2), 17, RoundingMode.HALF_UP).multiply(new BigDecimal(max - min))).doubleValue();
    }

    public double nextDouble(double max) {
        return nextRandFromN1ToP1().add(new BigDecimal(1)).divide(new BigDecimal(2), 17, RoundingMode.HALF_UP).multiply(new BigDecimal(max)).doubleValue();
    }

    public double nextDouble() {
        return nextRandFromN1ToP1().add(new BigDecimal(1)).divide(new BigDecimal(2), 17, RoundingMode.HALF_UP).doubleValue();
    }

    private BigDecimal nextRandFromN1ToP1() {
        BigDecimal rand = new BigDecimal(this.rand());
        return rand.divide(maxLongBigDecimal, 18, RoundingMode.HALF_UP);
    }

    @Override
    public long rand() {
        return super.rand();
    }

    @Override
    public long seed() {
        return super.seed();
    }
}

