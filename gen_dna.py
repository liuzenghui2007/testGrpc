import numpy as np
import matplotlib.pyplot as plt

# 定义信号参数
SAMPLE_RATE = 5000  # Hz
DURATION = 0.1  # seconds
TOTAL_SAMPLES = SAMPLE_RATE * DURATION

# 电流水平
CURRENT_LEVELS = {
    'open': (0.2, 0.3),
    'transit': (0.1, 0.2),
    'block': (0, 0.1)
}

# 事件持续时间
EVENT_DURATIONS = {
    'transit': (3, 10),  # seconds
    'block': (1, 5),     # seconds
    'open': (0.2, 5)     # seconds
}

# 噪声水平
NOISE_LEVELS = {
    'open': 0.005,
    'transit': 0.01,
    'block': 0.005
}

def generate_signal(samples):
    signal = np.zeros(samples)
    time = 0
    while time < samples:
        event_type = np.random.choice(['transit', 'block', 'open'])
        duration = int(np.random.uniform(*EVENT_DURATIONS[event_type]) * SAMPLE_RATE)
        current_level = np.random.uniform(*CURRENT_LEVELS[event_type])
        
        if time + duration > samples:
            duration = samples - time
        
        # 为每个事件添加相应水平的噪声
        noise = np.random.normal(loc=0, scale=NOISE_LEVELS[event_type], size=duration)
        signal[time:time+duration] = current_level + noise
        
        time += duration
    
    return signal

if __name__ == '__main__':
    # 这里的代码只有在直接运行 gen_dna.py 时才会执行
    # 生成信号
    signal = generate_signal(TOTAL_SAMPLES)

    # 绘制信号
    plt.figure(figsize=(14, 7))
    plt.plot(signal, label='Noisy Signal')
    plt.fill_between(range(TOTAL_SAMPLES), CURRENT_LEVELS['open'][0], CURRENT_LEVELS['open'][1], color='green', alpha=0.2, label='Open Level')
    plt.fill_between(range(TOTAL_SAMPLES), CURRENT_LEVELS['transit'][0], CURRENT_LEVELS['transit'][1], color='blue', alpha=0.2, label='Transit Level')
    plt.fill_between(range(TOTAL_SAMPLES), CURRENT_LEVELS['block'][0], CURRENT_LEVELS['block'][1], color='red', alpha=0.2, label='Block Level')
    plt.legend()
    plt.xlabel('Sample Index')
    plt.ylabel('Current Level (pA)')
    plt.title('Simulated Nanopore Sequencing Signal with Noise')
    plt.grid(True)
    plt.show()