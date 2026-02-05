import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
