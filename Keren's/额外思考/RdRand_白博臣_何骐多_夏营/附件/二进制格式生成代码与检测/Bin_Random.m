% 创建目标文件夹
folderName = 'target\data4';
if ~exist(folderName, 'dir')
    mkdir(folderName);
end

% 设置参数
numSamples = 1000;      % 文件数量
numBits = 1000000;      % 每个样本中的位数
bytesPerFile = ceil(numBits / 8); % 每个文件的字节数（125,000字节）

% 检查文件大小限制
maxFileSize = 131072; % 128KB
if bytesPerFile > maxFileSize
    error('单个文件的大小超过128KB的限制');
end

% 生成和保存随机数
for i = 1:numSamples
    % 生成随机位数组
    randomBits = randi([0, 1], 1, numBits, 'uint8');
    
    % 初始化字节数组
    randomBytes = uint8(zeros(1, bytesPerFile));
    
    % 将位数组转换为字节数组
    for j = 1:numBits
        byteIndex = ceil(j / 8);
        bitIndex = mod(j-1, 8) + 1;
        randomBytes(byteIndex) = bitor(randomBytes(byteIndex), bitshift(randomBits(j), 8-bitIndex));
    end
    
    % 保存为二进制文件
    fileName = fullfile(folderName, sprintf('random_%04d.bin', i));
    fid = fopen(fileName, 'w');
    fwrite(fid, randomBytes, 'uint8');
    fclose(fid);
end

disp('随机数生成并保存完成');
