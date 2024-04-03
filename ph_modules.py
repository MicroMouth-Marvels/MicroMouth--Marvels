def DS_Q_Q_Plot_test(y, est = 'robust', **kwargs):
    """
    *
    Function DS_Q_Q_Plot(y, est = 'robust', **kwargs)
    
       This function makes a normal quantile-quantile plot (Q-Q-plot), also known
       as a probability plot, to visually check whether data follow a normal distribution.
    
    Requires:            - 
    
    Arguments:
      y                  data array
      est                Estimation method for normal parameters mu and sigma:
                         either 'robust' (default), or 'ML' (Maximum Likelihood),
                         or 'preset' (given values)
      N.B. If est='preset' than the *optional* parameters mu, sigma must be provided:
      mu                 preset value of mu
      sigma              preset value of sigma
      
    Returns:
      Estimated mu, sigma, n, and expected number of datapoints outside CI in Q-Q-plot.
      Q-Q-plot
      
    Author:            M.E.F. Apol
    Date:              2020-01-06, revision 2022-08-30
    """
    
    import numpy as np
    from scipy.stats import iqr
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    
    # First, get the optional arguments mu and sigma:
    mu_0 = kwargs.get('mu', None)
    sigma_0 = kwargs.get('sigma', None)
    
    n = len(y)
    
    # Calculate order statistic:
    y_os = np.sort(y)
  
    # Estimates of mu and sigma:
    # ML estimates:
    mu_ML = np.mean(y)
    sigma2_ML = np.var(y)
    sigma_ML = np.std(y) # biased estimate
    s2 = np.var(y, ddof=1)
    s = np.std(y, ddof=1) # unbiased estimate
    # Robust estimates:
    mu_R = np.median(y)
    sigma_R = iqr(y)/1.349

    # Assign values of mu and sigma for z-transform:
    if est == 'ML':
        mu, sigma = mu_ML, s
    elif est == 'robust':
        mu, sigma = mu_R, sigma_R
    elif est == 'preset':
        mu, sigma = mu_0, sigma_0
    else:
        print('Wrong estimation method chosen!')
        return()
        
    
    # Expected number of deviations (95% confidence level):
    n_dev = np.round(0.05*n)
    
         
    # Perform z-transform: sample quantiles z.i
    z_i = (y_os - mu)/sigma

    # Calculate cumulative probabilities p.i:
    i = np.array(range(n)) + 1
    p_i = (i - 0.5)/n

    # Calculate theoretical quantiles z.(i):
    
    z_th = norm.ppf(p_i, 0, 1)

    # Calculate SE or theoretical quantiles:
    SE_z_th = (1/norm.pdf(z_th, 0, 1)) * np.sqrt((p_i * (1 - p_i)) / n)

    # Calculate 95% CI of diagonal line:
    CI_upper = z_th + 1.96 * SE_z_th
    CI_lower = z_th - 1.96 * SE_z_th

    # Make Q-Q plot:
    plt.plot(z_th, z_i, 'o', color='k', label='experimental data')
    plt.plot(z_th, z_th, '--', color='r', label='normal line')
    plt.plot(z_th, CI_upper, '--', color='b', label='95% CI')
    plt.plot(z_th, CI_lower, '--', color='b')

    stats_text = f'Estimation method: {est}\nn = {n}, mu = {mu:.4g}, sigma = {sigma:.4g}\nExpected number of data outside CI: {n_dev:.0f}'
    plt.text(1.05, 0.95, stats_text, transform = plt.gca(). transAxes, fontsize=9, verticalalignment='top')
    plt.xlabel('Theoretical quantiles, $z_{(i)}$')
    plt.ylabel('Sample quantiles, $z_i$')
    plt.title('Q-Q plot (' + est + ')')
    plt.legend(loc='best')
    plt.show()


def DS_AndersonDarling_test_normal(y, alpha=0.05):
    """
    *
    Function DS_AndersonDarling_test_normal(y, alpha)
    
       This function tests whether the data y follow a normal distribution (Null Hypothesis Significance Test).
    
    Requires:            scipy.stats.anderson
    
    References:          * Th. Anderson & D. Darling (1952) - "Asymptotic Theory of 
                         Certain "Goodness of Fit" Criteria Based on Stochastic Processes".
                         Ann. Math. Statist. 23, 193-212. DOI: 10.1214/aoms/1177729437
                         * R.B. D'Agostino (1986). "Tests for the Normal Distribution"
                         In: R.B. D'Augostino & M.A. Stephens - "Goodness-of-fit
                         techniques", Marcel Dekker.
    
    Arguments:
      y                  data array
      alpha              significance level of the critical value (default: alpha = 0.05)
      
    Usage:               DS_AndersonDarling_test_normal(y, alpha=alpha)
      
      
    Returns:             AD, AD_star, p_value [ + print interpretable output to stdout ]
    where
      AD                 (Large-sample) Anderson-Darling statistic
      AD_star            Small-sample Anderson-Darling statistic
      p_value            p-value of AD-test
      
    Author:            M.E.F. Apol
    Date:              2023-12-05
    """
    
       
    AD = anderson(y, dist='norm').statistic
    n = len(y)
    AD_star = AD*(1 + 0.75/n + 2.25/n**2)
    
    # p-values based on D'Augostino & Stephens (1986):
    if(AD_star <= 0.2): # Eq. (1)
        p_value = 1 - np.exp(-13.436 + 101.14*AD_star - 223.73*AD_star**2)
    elif((AD_star > 0.2) & (AD_star <= 0.34)): # Eq. (2)
        p_value = 1 - np.exp(-8.318 + 42.796*AD_star - 59.938*AD_star**2)
    elif((AD_star > 0.34) & (AD_star < 0.6)): # Eq. (3)
        p_value = np.exp(0.9177 - 4.279*AD_star - 1.38*AD_star**2)
    elif(AD_star >= 0.6): # Eq. (4)
        p_value = np.exp(1.2937 - 5.709*AD_star + 0.0186*AD_star**2)
        
    # Critical AD* values, based on D'Augostino & Stephens (1986):
    # Inverting these relations, we get
    # Invert (1) if alpha > 0.884
    # Invert (2) if 0.50 < alpha < 0.884
    # Invert (3) if 0.1182 < alpha < 0.50
    # Invert (4) if alpha < 0.1182
    
    if(alpha >= 0.884): # Eq. (1a)
        AD_crit = (-101.14+np.sqrt(101.14**2-4*-223.73*(-13.436-np.log(1-alpha))))/(2* -223.73)
    elif((alpha < 0.884) & (alpha >= 0.50)): # Eq. (2a)
        AD_crit = (-42.796+np.sqrt(42.796**2-4* -59.938*(-8.318-np.log(1-alpha))))/(2* -59.938)
    elif((alpha < 0.50) & (alpha >= 0.1182)): # Eq. (3a)
        AD_crit = (4.279-np.sqrt(4.279**2-4* -1.38*(0.9177-np.log(alpha))))/(2* -1.38)
    elif(alpha < 0.1182): # Eq. (4a)
        AD_crit = (5.709-np.sqrt(5.709**2-4*0.0186*(1.2937-np.log(alpha))))/(2*0.0186)
    
    # Additional statistics:
    y_av = np.mean(y)
    s = np.std(y, ddof=1)
    
    print(80*'-')
    print('Anderson-Darling-test for normality of data:')
    print('     assuming Normal(mu | sigma2) data for dataset')
    print('y.av = {:.3g}, s = {:.3g}, n = {:d}, alpha = {:.3g}'.format(y_av, s, n, alpha))
    print('H0: data follows normal distribution')
    print('H1: data does not follow normal distribution')
    print('AD = {:.3g}, AD* = {:.3g}, p-value = {:.3g}, AD*.crit = {:.3g}'.format(AD, AD_star, p_value, AD_crit))
    print(80*'-')
    
    return(AD, AD_star, p_value);



def DS_2sample_MannWhitney_test_medians(y1, y2, alternative='two-sided', alpha=0.05):
    """
    *
    Function DS_2sample_MannWhitney_test_medians(y1, y2, alternative='two-sided', alpha=0.05)
    
       This function tests two medians eta.1 and eta.2 of data y1 and y2 (Null Hypothesis Significance Test).
       The distributions are assumed to be identical, but not necessarily normal.
    
    Requires:            scipy.stats.mannwhitneyu
    
    Usage:               DS_2sample_MannWhitney_test_medians(y1, y2, 
                              alternative=['two-sided']/'less'/'greater', alpha=0.05)
    
    Arguments:
      y                  data array
      popmedian          reference value of the median, median*
      alternative        'two-sided' [default]   H1: eta.1 != eta.2
                         'less'                  H1: eta.1 <  eta.2
                         'greater'               H1: eta.1 >  eta.2
      alpha              significance level of test [default: 0.05]     
 
 
    Returns:             U.1, U.2, U, p_value [ + print interpretable output to stdout ]
    where
      U.1, U.2, U        Mann-Whitney statistics
      p_value            p-value of Mann-Whitney U-test
      
    Validation:          against SPSS v. 28
      
    Author:            M.E.F. Apol
    Date:              2023-12-20
    """


    
    # Additional statistics:
    y_med_1 = np.median(y1)
    y_med_2 = np.median(y2)
    n_1 = len(y1)
    n_2 = len(y2)
    
    print(80*'-')
    print('2-sample Mann-Whitney U-test for 2 medians:')
    print('     assuming identical distributions for both datasets, that may differ in location')
    print('y.med.1 = {:.4g}, y.med.2 = {:.4g}, n.1 = {:d}, n.2 = {:d}, alpha = {:.3g}'.format(y_med_1, y_med_2, n_1, n_2, alpha))
    print('H0: eta.1  = eta.2')
    
    if alternative == 'two-sided':
        print('H1: eta != eta*')
    elif alternative == 'greater':
        print('H1: eta  > eta*')
    elif alternative == 'less':
        print('H1: eta  < eta*')
    else:
        print('Wrong alternative hypothesis chosen!')
        print(80*'-' + '\n')
        U_1, U_2, U, p_value = np.nan, np.nan, np.nan, np.nan
    return(U_1, U_2, U, p_value)
    
    #res = mannwhitneyu(y1, y2, alternative=alternative, use_continuity=True)
    res = mannwhitneyu(y1, y2, alternative=alternative, use_continuity=False)
    U_1 = res.statistic
    U_2 = n_1*n_2 - U_1
    U = np.min([U_1, U_2])
    p_value = res.pvalue
    
    # -- TO DO -- Find formula for U.crit
    U_crit = np.nan
    
    # To compute an effect size for the signed-rank test, one can use the rank-biserial correlation?
    
    # Correlation coefficient:
    # From: datatab.net (dd 2023_12_19), https://maths.shu.ac.uk/mathshelp/ (dd 2023_12_19)
    # Normal approximation:
    # Expectation value:
    mu_U = n_1*n_2/2
    # Standard deviation:
    sigma_U = np.sqrt(n_1*n_2*(n_1+n_2+1)/12)
    # Standard normal statistic:
    z = (U - mu_U) / sigma_U
    # Effect size:
    r = z / np.sqrt(n_1+n_2)
    
    # Point biserial correlation r.pb
    # From: https://www.andrews.edu/~calkins/math/edrm611/edrm13.htm
    # Additional statistics:
    y_av_1 = np.mean(y1)
    y_av_2 = np.mean(y2)
    s2_1 = np.var(y1, ddof=1)
    s2_2 = np.var(y2, ddof=1)
    s2_p = ((n_1-1)*s2_1 + (n_2-1)*s2_2)/(n_1+n_2-2)
    s_p = np.sqrt(s2_p)
    r_pb = (y_av_1 - y_av_2)/s_p * np.sqrt(n_1*n_2)/(n_1 + n_2)
    
    print('U.1 = {:.3g}, U.2 = {:.3g}, U = {:.3g}, p-value = {:.3g}, z = {:.3g}, U.crit = {:.3g}'.format(U_1, U_2, U, p_value, z, U_crit))
    print('Effect size: r    = {:.3g}; benchmarks |r|: 0.1 = small, 0.3 = medium, 0.5 = large'.format(r))
    # print('Effect size: r.pb = {:.3g}; benchmarks r: 0.1 = small, 0.3 = medium, 0.5 = large (?)'.format(r_pb))
    print(80*'-')
    
    return(U_1, U_2, U, p_value);
