% Author: Luciano de Oliveira Daniel
% https://sites.google.com/site/professorlucianodaniel

f = @(x) (1/sqrt(pi)).*exp(-x.^2)
[Q1,erro1] = quadgk(f,0,1)
[Q2,erro2] = quadgk(f,0,1,'RelTol',1e-8,'AbsTol',1e-12)      
[Q3,erro3] = quadgk(f,0,1,'RelTol',1e-8,'AbsTol',0)
[Q4,erro4] = quadgk(f,0,1,'RelTol',0,'AbsTol',1e-12)