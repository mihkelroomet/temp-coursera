import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

big = {'fontsize': 50}

n = 10

x1 = np.random.normal(-2.5, 1, 1000)
x2 = np.random.gamma(2, 1.5, 1000)
x3 = np.random.exponential(2, 1000)+7
x4 = np.random.uniform(14,20, 1000)

fig = plt.figure(figsize=(12,5))
gspec = gridspec.GridSpec(250, 114)

axes = [
    plt.subplot(gspec[47:79, 23:49]),
    plt.subplot(gspec[102:190, 5:38]),
    plt.subplot(gspec[7:165, 63:103]),
    plt.subplot(gspec[201:229, 83:108])
]

def update(i):
    if i+1 == n:
        a.event_source.stop()
    for a in axes:
        a.cla()
    
    axes[0].hist(x1[:(i+1)*100], normed=True, bins=20, alpha=0.3, color='red')
    axes[0].axis([-6, 1, 0, 0.5])
    axes[1].hist(x2[:(i+1)*100], normed=True, bins=20, alpha=0.9, color='#9ef2ff')
    axes[1].axis([0, 15, 0, 0.5])
    axes[2].hist(x3[:(i+1)*100], normed=True, bins=20, alpha=0.9, color='#afffab')
    axes[2].axis([7, 23, 0, 0.5])
    axes[3].hist(x4[:(i+1)*100], normed=True, bins=20, alpha=0.3, color='purple')
    axes[3].axis([14, 20, 0, 0.5])

    for a in axes:
        a.axis('off')

    axes[0].text(-5, 0.5, 'Normal\nn={}'.format((i+1)*100))
    axes[1].text(4, 0.2, 'Gamma\nn={}'.format((i+1)*100))
    axes[2].text(9, 0.3, 'Exponential\nn={}'.format((i+1)*100))
    axes[3].text(15, -0.2, 'Uniform\nn={}'.format((i+1)*100))

    plt.title('Distribooshahnss', loc='right', **big)

a = animation.FuncAnimation(fig, update, interval=1000)

plt.show()