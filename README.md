## Dynamical Network Biomarker (DNB) tools for time series data

---

This code extracts the early warning signal (EWS) reference indicators according to the DNB's idea.
In accordance with the literature [1], this code calculates the indicators by the following steps:
1. normalizing the data.
2. dividing the data into sliding windows.
3. calculating the covariance matrix and the maximum eigenvalue.

This package is available on github and can be used with the following pip code.
```code
pip install git+https://github.com/yuji0001/time_series_DNB
```

In addition to the DNB code, this code contains simulation data where the following branches occur:

1. Toy model with saddle node bifurcation 

2. A harvested population model with herbivores and biomass [2]

3. The spatial type of the above [3]

[1]	M. Oku and K. Aihara, “On the Covariance Matrix of the Stationary Distribution of a Noisy Dynamical System,” Nonlinear Theory and Its Applications, IEICE, 9(2), 166-184, doi:10.1587/nolta.9.166 (2018).

[2] May, Robert M. "Thresholds and breakpoints in ecosystems with a multiplicity of stable states." Nature 269.5628 (1977): 471-477.

[3] van Nes, Egbert H., and Marten Scheffer. "Implications of spatial heterogeneity for catastrophic regime shifts in ecosystems." Ecology 86.7 (2005): 1797-1807.
pip install test for time series DNB 

## Requirements
This packeage need the following:
```code
python >=3.7 
numpy
pandas
matplotlib
sklearn
ruptures
```

## Usage

See the folowing colaboratory code.
https://colab.research.google.com/drive/12cCTptbXhu_6vNHZ0OTBv9ggVg0KWnbs?usp=sharing

## License
Apache 2.0

## Auther
Yuji Okamoto (yuji.0001[at]gmail.com)