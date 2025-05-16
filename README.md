# 📚 VISTA: Video-to-Text Summarization Dataset for Scientific Presentations

This repository contains the official implementation of "What Is That Talk About? A Video-to-Text Summarization Dataset for Scientific Presentations" accepted at Transactions of the Association for Computational Linguistics (TACL).

<p align="center">
  <img src="https://img.shields.io/badge/ACL-2025-blue" alt="ACL 2025">
  <img src="https://img.shields.io/badge/Status-Available-green" alt="Status: Available">
</p>

## 📥 Dataset

The VISTA dataset is available on Huggingface:
[https://huggingface.co/datasets/dongqi-me/VISTA](https://huggingface.co/datasets/dongqi-me/VISTA)

## 💻 Code

The implementation code is stored in the `code` folder. 

## 📄 Paper Abstract

Transforming recorded videos into concise and accurate textual summaries is a growing challenge in multimodal learning. This paper introduces VISTA, a dataset specifically designed for video-to-text summarization in scientific domains. VISTA contains 18,599 recorded AI conference presentations paired with their corresponding paper abstracts. We benchmark the performance of state-of-the-art large models and apply a plan-based framework to better capture the structured nature of abstracts. Both human and automated evaluations confirm that explicit planning enhances summary quality and factual consistency. However, a considerable gap remains between models and human performance, highlighting the challenges of our dataset. This study aims to pave the way for future research on scientific video-to-text summarization.

## 📝 Citation

```bibtex
@article{liu2025vista,
  title={What Is That Talk About? A Video-to-Text Summarization Dataset for Scientific Presentations},
  author={Liu, Dongqi and Whitehouse, Chenxi and Yu, Xi and Mahon, Louis and Saxena, Rohit and Zhao, Zheng and Qiu, Yifu and Lapata, Mirella and Demberg, Vera},
  journal={arXiv preprint arXiv:2502.08279},
  year={2025}
}
```
