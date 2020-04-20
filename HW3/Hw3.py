# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:48:54 2020

@author: Yasin Uslu 71028
"""
import pandas as pd
import pystan

## Model 1:

data = pd.read_csv('trend2.csv')
data = data.dropna()

data.county= data.country.str.strip()
mn_counties = data.county.unique()

county_lookup = dict(zip(mn_counties, range(len(mn_counties))))

county = data['county_code'] = data.county.replace(county_lookup).values

data.outcome = data.church2

gini = data.gini_net.values
rgdpl = data.rgdpl.values
church2 = data.church2.values
n_county = data.country.unique()

varying_intercept_model1 = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> county[N];
  vector[N] x;
  vector[N] z;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- a[county[i]]  + x[i]*b1 + z[i]*b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 1);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_data_model1 = {'N': len(church2),
                                 'J': len(n_county),
                                 'county': county+1,
                                 'x': gini,
                                 'y': church2,
                                 'z': rgdpl}

varying_intercept_fit_model1 = pystan.stan(model_code=varying_intercept, data=varying_intercept_data, iter=1000, chains=2)
varying_intercept_fit_model1

## Model 2:

data = pd.read_csv('trend2.csv')
data = data.dropna()

data.county= data.country.str.strip()
mn_counties = data.county.unique()

county_lookup = dict(zip(mn_counties, range(len(mn_counties))))

county = data['county_code'] = data.county.replace(county_lookup).values

data.outcome = data.church2

gini = data.gini_net.values
rgdpl = data.rgdpl.values
church2 = data.church2.values
n_county = data.country.unique()

varying_intercept_model2 = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> county[N];
  vector[N] x;
  vector[N] z;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- a[county[i]]  + x[i]*b1 + z[i]*b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 100);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_data_model2 =  {'N': len(church2),
                                  'J': len(n_county),
                                  'county': county+1,
                                  'x': gini,
                                  'y': church2,
                                  'z': rgdpl}
varying_intercept_fit_model2 = pystan.stan(model_code=varying_intercept, data=varying_intercept_data, iter=1000, chains=2)
varying_intercept_fit_model2
