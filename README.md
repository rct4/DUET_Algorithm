DUET: Blind Sound Source Separation (DoA + Delay/Attenuation Clustering)

DUET (Degenerate Unmixing Estimation Technique) separates overlapping sound sources from two microphone signals by exploiting relative delay and attenuation across time–frequency bins. This repo implements an end-to-end DUET pipeline with reproducible experiments, plots, and audio outputs.
What this project does

    Takes two-channel audio x1(t),x2(t)x1​(t),x2​(t)

    Computes STFT spectrograms

    Estimates relative delay and attenuation from spectrogram ratios

    Clusters time–frequency (TF) bins in the delay–attenuation plane

    Reconstructs N sources via TF masking and inverse STFT

Algorithm

    STFT: Compute short-time Fourier transforms of the two signals → complex spectrograms X1(f,n)X1​(f,n), X2(f,n)X2​(f,n).

    TF Ratio: Compute R(f,n)=X2(f,n)X1(f,n)R(f,n)=X1​(f,n)X2​(f,n)​. From RR estimate

        Relative attenuation aa

        Relative delay ττ (via phase vs. frequency slope)

    Clustering: Map each TF bin (f,n)(f,n) to a point (a^,τ^)(a^,τ^); cluster into N groups.

    Reconstruction: Build binary/soft masks per cluster and apply to X1X1​ or a mix; inverse STFT → N separated sources.
