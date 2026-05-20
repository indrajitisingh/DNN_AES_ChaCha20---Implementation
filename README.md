# Deep Neural Network Based Implementation and Analysis of AES and ChaCha20 Encryption Algorithms

## Overview

This project focuses on the implementation and analysis of modern cryptographic encryption algorithms using Deep Neural Networks (DNN). The project generates encrypted datasets using AES and ChaCha20 algorithms and applies machine learning techniques to analyze ciphertext patterns.

The implementation was developed using Python, TensorFlow, Keras, and cryptographic libraries in an Ubuntu Linux environment running on VMware with VS Code Remote SSH integration.

---

## Objectives

- Generate encrypted datasets using AES and ChaCha20 algorithms
- Implement Deep Neural Network models using TensorFlow and Keras
- Train a DNN model on AES encrypted data
- Develop a combined classification model for AES and ChaCha20 ciphertexts
- Evaluate model performance and accuracy
- Analyze the difficulty of distinguishing modern encrypted ciphertext using AI techniques

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Core Programming Language |
| TensorFlow | Deep Learning Framework |
| Keras | Neural Network API |
| NumPy | Numerical Computation |
| Pandas | Dataset Handling |
| PyCryptodome | Cryptographic Operations |
| Ubuntu Linux | Development Environment |
| VMware | Virtualization Platform |
| VS Code | Code Editor |

---

## Project Structure

```bash
DNN_AES_ChaCha20_Implementation/
│
├── aes_dataset_generator.py
├── chacha_dataset_generator.py
├── train_aes_model.py
├── train_combined_model.py
└── README.md
