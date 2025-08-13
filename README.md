# DUET: Blind Sound Source Separation (DoA + Delay/Attenuation Clustering)

DUET (Degenerate Unmixing Estimation Technique) separates overlapping sound sources from **two microphone signals** by exploiting **relative delay** and **attenuation** across time–frequency bins.

## What this project does
- Takes two-channel audio `(x₁(t), x₂(t))`
- Computes **STFT** spectrograms
- Estimates **relative delay** and **attenuation** from **spectrogram ratios**
- **Clusters** time–frequency (TF) bins in the **delay–attenuation** plane
- **Reconstructs N sources** via TF masking and inverse STFT

---

## Algorithm

1. **STFT**: Compute short-time Fourier transforms of the two signals → complex spectrograms `X₁(f, n)`, `X₂(f, n)`.  
2. **TF Ratio**: Compute `R(f, n) = X₂(f, n) / X₁(f, n)`. From `R` estimate:  
   - **Relative attenuation** `a`  
   - **Relative delay** `τ` (via phase vs. frequency slope)  
3. **Clustering**: Map each TF bin `(f, n)` to a point `(â, τ̂)`; cluster into **N** groups.  
4. **Reconstruction**: Build binary/soft masks per cluster and apply to `X₁` or a mix; inverse STFT → **N separated sources**.


## References
- Jourjine, A., Rickard, S., & Yilmaz, O. (2000). **Blind Separation of Disjoint Orthogonal Signals: DUET**. *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*. [https://doi.org/10.1109/ICASSP.2000.859087](https://doi.org/10.1109/ICASSP.2000.859087)  
- Rickard, S., Balan, R., & Rosca, J. (2001). **Real-Time Time–Frequency Masks for Source Separation**. *Proceedings of the SAPA Workshop on Statistical and Perceptual Audio Processing*. [https://www.mee.tcd.ie/~sigproc/pubs/sapa01.pdf](https://www.mee.tcd.ie/~sigproc/pubs/sapa01.pdf)
