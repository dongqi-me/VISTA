# 📚 VISTA: Video-to-Text Summarization Dataset for Scientific Presentations

This repository contains the official implementation of "What Is That Talk About? A Video-to-Text Summarization Dataset for Scientific Presentations" accepted at the Annual Meeting of the Association for Computational Linguistics (ACL 2025).

<p align="center">
  <img src="https://img.shields.io/badge/ACL-2025-blue" alt="ACL 2025">
  <img src="https://img.shields.io/badge/Status-Available-green" alt="Status: Available">
  <img src="https://img.shields.io/badge/Code-Cleaning-yellow" alt="Code: Cleaning">
</p>

## 🚧 Code Status

The code is temporarily available in this repository but is currently undergoing cleanup and documentation.

## 📥 Dataset

The VISTA dataset is available on Huggingface:
[https://huggingface.co/datasets/dongqi-me/VISTA](https://huggingface.co/datasets/dongqi-me/VISTA)

## 💻 Code Structure

The implementation code will be organized as follows:
```
code/
├── data/              # Data processing scripts
├── models/            # Model implementations
├── training/          # Training scripts
└── evaluation/        # Evaluation scripts
```

## 📄 Paper Abstract

Transforming recorded videos into concise and accurate textual summaries is a growing challenge in multimodal learning. This paper introduces VISTA, a dataset specifically designed for video-to-text summarization in scientific domains. VISTA contains 18,599 recorded AI conference presentations paired with their corresponding paper abstracts. We benchmark the performance of state-of-the-art large models and apply a plan-based framework to better capture the structured nature of abstracts. Both human and automated evaluations confirm that explicit planning enhances summary quality and factual consistency. However, a considerable gap remains between models and human performance, highlighting the challenges of our dataset. This study aims to pave the way for future research on scientific video-to-text summarization.

## 📝 Citation

```bibtex
@inproceedings{liu-etal-2025-talk,
    title = "What Is That Talk About? A Video-to-Text Summarization Dataset for Scientific Presentations",
    author = "Liu, Dongqi  and
      Whitehouse, Chenxi  and
      Yu, Xi  and
      Mahon, Louis  and
      Saxena, Rohit  and
      Zhao, Zheng  and
      Qiu, Yifu  and
      Lapata, Mirella  and
      Demberg, Vera",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.310/",
    pages = "6187--6210",
    ISBN = "979-8-89176-251-0"
}
``` 
