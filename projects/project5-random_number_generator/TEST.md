以下是对脚本中各项随机性检验的详细介绍，以及如何根据各自的检验值来判断随机数质量。

---

## 1. Monobit Test（比特频率检验）  
**目的**：检验整个序列中“0”和“1”的出现频率是否接近各占一半。  
**方法**：将比特流转换为 ±1（0→−1，1→+1），计算所有值之和 S，然后标准化为观察统计量  
\[
S_{\mathrm{obs}} = \frac{|S|}{\sqrt{n}}
\]  
再通过正态分布计算 p-value：  
\[
p = 2\bigl(1 - \Phi(S_{\mathrm{obs}})\bigr)
\]  
**判定标准**：  
- 若 \(p > 0.01\)（或更保守地，\(p > 0.05\)），则接受“0/1 频率均衡”假设，说明无明显偏差。  
- 若 p 极小（如 <0.001），说明“1”或“0”一方明显过多，存在严重偏差。

---

## 2. Block Frequency Test（块频率检验）  
**目的**：检验长序列在较短区块内也保持“0/1”平衡，避免全局均衡但局部倾斜。  
**方法**：  
1. 按固定大小 \(M\)（如 128）将比特串分成 \(N=\lfloor n/M\rfloor\) 个块。  
2. 计算每个块中“1”的比例 \(p_i\)。  
3. 构造卡方统计量  
\[
\chi^2 = 4M\sum_{i=1}^N(p_i-0.5)^2
\]  
4. 依据自由度 \(df=N\) 计算 p-value：  
\[
p = \Pr(\chi^2_{df} \ge \chi^2)
\]  
**判定标准**：  
- \(p > 0.01\)（或 >0.05）：每个块内“0/1”比例正常，无局部失衡。  
- 若 p 很低，则存在某些块过度偏向“0”或“1”。

---

## 3. Runs Test（游程检验）  
**目的**：检验比特流中“0-1”切换的次数是否符合随机预期，避免过长或过短的连续段（游程）。  
**方法**：  
1. 计算平均概率 \(\pi=\frac{\#1}{n}\)，若 \(|\pi-0.5|\) 太大则直接判为不通过。  
2. 计算游程总数 \(V_n\)（每次比特不同即计一次）。  
3. 将 \(V_n\) 与期望 \(2n\pi(1-\pi)\) 做正态近似，得出 p-value。  
**判定标准**：  
- \(p > 0.01\)：游程分布正常，切换频率符合随机预期。  
- 若 p 很低，则可能存在游程过多（频繁切换）或过少（长段不切换）。

---

## 4. Autocorrelation Test（自相关检验）  
**目的**：检查滞后 \(lag\) 下，序列比特之间是否存在线性相关。  
**方法**：  
1. 计算比特序列与自身滞后 \(lag\) 后的皮尔逊相关系数 \(\rho\)。  
2. 基于大样本正态近似，计算统计量并得出 p-value。  
**判定标准**：  
- 若 \(|\rho|\) 接近 0 且 \(p > 0.01\)，说明没有显著自相关。  
- 若 \(\rho\) 显著偏离 0（p 很小），则序列存在线性依赖，不足够“随机”。

---

## 5. Spectral Test（离散傅里叶谱检验）  
**目的**：检测序列中周期性模式和频谱峰值，避免隐藏的循环或结构。  
**方法**：  
1. 将比特映射为 ±1，做快速傅里叶变换（FFT），得到幅值谱 \(S_k\)。  
2. 统计小于阈值 \(T=\sqrt{\ln(1/0.05)\times N}\) 的谱成分数量 count。  
3. 与理论期望 \(\approx0.95\times(N/2)\) 比较，计算 Z-score 再求 p-value。  
**判定标准**：  
- \(p > 0.01\)：频谱峰值分布正常，无显著周期性。  
- 否则可能有隐藏的重复模式或周期噪声。

---

## 6. Approximate Entropy Test（近似熵检验）  
**目的**：衡量比特序列在重叠子串层级上的重复度，检测高阶依赖或结构。  
**方法**：  
1. 对长度 m 和 m+1 的所有重叠子串统计出现频率，计算近似熵  
\(\mathrm{ApEn} = \phi(m) - \phi(m+1)\)。  
2. 将 ApEn 与理想的 \(\ln(2)\) 差距通过卡方检验得出 p-value。  
**判定标准**：  
- \(p > 0.01\) 且 ApEn 接近 \(\ln(2)\approx0.693\)：高熵、无显著模式。  
- 若 p 很小或 ApEn 明显偏低，序列有环境依赖或可预测性。

---

## 如何综合判断质量高低  
- **通过所有 p-value 检验**：每项测试若 \(p > 0.01\)（或更严格的 0.05），则无显著偏差。  
- **多角度无弱项**：单一测试通过不足以证明完全随机，但若六项检验均通过，则随机数性质已非常可靠。  
- **留意统计显著性边界**：  
  - p 过于接近 1 反而可能“过于完美”——真实随机不应完全一致。  
  - p 在 0.1–0.9 范围内较理想；极端接近上下界（如 <0.001 或 >0.999）都值得复查数据或测试方法。

---

**小贴士**：在不同参数（如 `BLOCK_SIZE`、`APEN_M`、`RUN_LAG`）下多次测试，并结合专业工具（Dieharder、TestU01）做更深入分析，可进一步验证系统的健壮性与安全性。