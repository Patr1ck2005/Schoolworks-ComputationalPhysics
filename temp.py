import numpy as np
import matplotlib.pyplot as plt

def rotation_matrix(theta):
    """返回平面旋转矩阵 R(theta)."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s],
                     [s,  c]])

def ellip_basis(psi, chi):
    """
    构造一对正交椭圆偏振琼斯基矢量 e1, e2。
    psi: 偏振面方向角（rad）
    chi: 椭圆度角（rad）
    返回 J: 2x2 的酉矩阵，将水平/垂直基映射到{e1,e2}.
    """
    c_ch, s_ch = np.cos(chi), np.sin(chi)
    c_ps, s_ps = np.cos(psi), np.sin(psi)
    e1 = np.array([ c_ch*c_ps - 1j*s_ch*s_ps,
                    c_ch*s_ps + 1j*s_ch*c_ps ])
    e2 = np.array([-1j*c_ch*s_ps + s_ch*c_ps,
                    -1j*c_ch*c_ps - s_ch*s_ps ])
    print(sum(e1*e2))
    e1 /= np.linalg.norm(e1)
    e2 /= np.linalg.norm(e2)
    return np.column_stack([e1, e2])

def scattering_in_ellip_basis(theta, psi, chi):
    """
    计算在给定 theta, psi, chi 下的散射矩阵 S''.
    theta: 平面旋转角（rad）
    psi: 椭圆偏振主轴方向（rad）
    chi: 椭圆度角（rad）
    返回 2x2 复矩阵 S_dd.
    """
    S = np.array([[1.0, 0.0],
                  [0.0, 0.0]])
    R = rotation_matrix(theta)
    S_prime = R @ S @ R.T
    J = ellip_basis(psi, chi)
    return J.conj().T @ S_prime @ J

# 设置参数
psi = np.deg2rad(0)  # 椭圆主轴方向
chi = np.deg2rad(45)  # 椭圆度角
theta_vals = np.linspace(0, 2*np.pi, 500)

# 预分配数组
S11 = np.zeros_like(theta_vals, dtype=complex)
S12 = np.zeros_like(theta_vals, dtype=complex)
S21 = np.zeros_like(theta_vals, dtype=complex)
S22 = np.zeros_like(theta_vals, dtype=complex)

# 计算
for i, th in enumerate(theta_vals):
    S_dd = scattering_in_ellip_basis(th, psi, chi)
    S11[i], S12[i], S21[i], S22[i] = S_dd[0,0], S_dd[0,1], S_dd[1,0], S_dd[1,1]

# 绘图：幅值
for label, data in [('S11', S11), ('S12', S12), ('S21', S21), ('S22', S22)]:
    plt.figure()
    plt.plot(theta_vals, np.abs(data))
    plt.xlabel('θ (rad)')
    plt.ylabel(f'|{label}|')
    plt.title(f'abs |{label}(θ)|')
    plt.tight_layout()

# 绘图：相位
for label, data in [('S11', S11), ('S12', S12), ('S21', S21), ('S22', S22)]:
    plt.figure()
    plt.plot(theta_vals, np.angle(data))
    plt.xlabel('θ (rad)')
    plt.ylabel(f'∠{label} (rad)')
    plt.title(f'arg ∠{label}(θ)')
    plt.tight_layout()

plt.show()
