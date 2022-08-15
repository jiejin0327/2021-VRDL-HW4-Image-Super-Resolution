# 2021-VRDL-HW4-Image-Super-Resolution

HW4 Introduction: Image super resolution

The proposed challenge is an image super resolution, and we have to train the model to reconstruct a high-resolution image from a low-resolution input. There are three parts in my project:

1. Split training dataset to train and valid datasets.
2. The train images are scaled down by 3 times as the low-resolution images.
3. Train the model to generate the high-resolution image
  I implemented the Lightweight Image Super-Resolution with Information Multi-distillation Network (IMDN) to fix this challenge.


model : IMDN

1. [inference.ipynb](https://colab.research.google.com/drive/1v_cu4xTalTMVO68XuHQoPVSV6JQsmxq7?usp=sharing)  
2. [Download weight data](https://drive.google.com/file/d/1m_57jk3gY_jQkbnQjpYUKMjhZRInt2zJ/view?usp=sharing)
3. [Download dataset](https://drive.google.com/drive/folders/1coNBvGijDkh_rkFXFuOpRIimgPupVvQR?usp=sharing)

reference code from [IMDN official github](https://github.com/Zheng222/IMDN/tree/62075400defe49361de0a24ea653528dcdac6067)
