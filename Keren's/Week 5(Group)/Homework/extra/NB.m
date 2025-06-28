clc; clear; close all; 
N = 20000; 
epsilon = 1e-3;
root1 = 1;
root2 = -1 / 2 + sqrt(3)/2i;
root3 = -1 / 2 - sqrt(3)/2i;
x = linspace(-2, 2, N);
y = linspace(-2, 2, N);
[xgrid, ygrid] = meshgrid(x, y);
X = xgrid + 1i*ygrid;

% 使用parfor循环并在循环内部利用GPU加速的函数
A = zeros(N);
tic; % 开始计时
parfor i = 1:N
    % 将数据移动到GPU
    X_gpu = gpuArray(X(i, :));
    
    % 在每次迭代中，利用GPU加速计算结果
    A_gpu = arrayfun(@solve, X_gpu);
    
    % 将计算结果从GPU移回CPU
    A(i, :) = gather(A_gpu); 

end

% 对计算结果进行处理
A(abs(A - root1) < epsilon) = 0;
A(abs(A - root2) < epsilon) = 1;
A(abs(A - root3) < epsilon) = 2;


% 绘制图像
% fig = figure('color',[1 1 1],'position',[400,100,500*1.5,416*1.5], 'Visible','off');
% contourf(x, y, A, 'LineStyle', 'none');
% clim([0, 2])
% colormap("cool")
% colorbar;
% saveas(fig, 'plot.png');

toc;

% writematrix(A, "result.txt")
