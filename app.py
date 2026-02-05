import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.signal import correlate
def simulate_single(I=1.5, noise=2.0, T=500, dt=1, seed=1, V_rest=-65, tau=20):
    np.random.seed(seed)
    steps = int(T / dt)
    V = np.ones(steps) * V_rest
    for t in range(1, steps):
        dV = (-(V[t-1] - V_rest) + I) / tau
        V[t] = V[t-1] + dV * dt + noise * np.random.randn() * 0.2
    return V
    np.random.seed(seed)
    steps = int(T / dt)
    V = np.ones(steps) * V_rest
    for t in range(1, steps):
        dV = (-(V[t-1] - V_rest) + I) / tau
        V[t] = V[t-1] + dV * dt + noise * np.random.randn() * 0.2
    return V
st.set_page_config(page_title="Canlı Nöron Simülasyonu", layout="centered")

st.title("🧠 Canlı LIF Nöron Ağı Simülasyonu")
st.write("Parametreleri değiştirerek nöron davranışını canlı gözlemleyebilirsin.")

# -----------------------
# PARAMETRELER
# -----------------------
N = st.slider("Nöron sayısı", 10, 200, 50)
I = st.slider("Uyarım akımı (I)", 0.0, 5.0, 1.5)
tau = st.slider("Zaman sabiti (tau)", 5.0, 30.0, 10.0)
threshold = st.slider("Eşik voltaj", -55.0, -40.0, -50.0)
noise = st.slider("Gürültü (noise)", 0.0, 5.0, 1.0)

T = 200
dt = 1

# -----------------------
# SİMÜLASYON
# -----------------------
V = -65 * np.ones((N, T))
spikes = np.zeros((N, T))

for t in range(1, T):
    dV = (-(V[:, t-1] + 65) + I) / tau
    V[:, t] = V[:, t-1] + dV*dt + np.random.normal(0, noise, N)
    
    fired = V[:, t] > threshold
    spikes[fired, t] = 1
    V[fired, t] = -65

# -----------------------
# GRAFİK
# -----------------------
fig, ax = plt.subplots(figsize=(8,4))

for i in range(min(N, 20)):
    ax.plot(V[i], lw=0.7)

ax.axhline(threshold, color='r', linestyle='--', label="Eşik")
ax.set_xlabel("Zaman")
ax.set_ylabel("Membran potansiyeli (mV)")
ax.set_title("Seçilmiş Nöronların Voltaj Davranışı")
ax.legend()

st.pyplot(fig)

# -----------------------
# AÇIKLAMA
# -----------------------
st.markdown("""
### 🔬 Bu neyi gösteriyor?

Her çizgi bir nöronu temsil eder.  
- Akım artarsa → daha sık ateşleme olur  
- Gürültü artarsa → düzensizlik artar  
- Eşik düşerse → sistem aşırı uyarılır (epilepsi benzeri)

Bu sistem:
🧠 Beyindeki kolektif davranışı  
⚡ Hassas parametreleri  
🎯 Müdahale etkisini  
incelemek için kullanılabilir.
""")
import time

st.header("Canlı Gün 1 — Tek Nöron")

I = st.slider("I (giriş akımı)", 0.0, 5.0, 1.5)
noise = st.slider("noise", 0.0, 5.0, 2.0)
speed = st.slider("Hız (ms)", 10, 200, 50)

if st.button("Canlı çalıştır"):
    V = simulate_single(I=I, noise=noise, T=T, dt=dt, seed=seed,
                        V_rest=default_Vrest, tau=default_tau)
    t = np.arange(0, T, dt)

    placeholder = st.empty()
    fig, ax = plt.subplots(figsize=(9,3))

    for i in range(1, len(t)):
        ax.clear()
        ax.plot(t[:i], V[:i])
        ax.axhline(default_Vth, linestyle='--')
        ax.set_xlabel("Time (ms)")
        ax.set_ylabel("mV")
        ax.set_title("Canlı Tek Nöron")
        placeholder
