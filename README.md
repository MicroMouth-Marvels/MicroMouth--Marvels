# MicroMouth--Marvels
# The Influence of Probiotic Mouthwash on Genomic Profiles and Health of the Oral Human Microbiome​

## Overview
This repository contains all modules used for analysis of data obtained from an experiment that tested the efficacy of a probiotic mouthwash on oral health, where efficacy means improved or restored oral health parameters as follows:

1. Reduction in gum bleeding prevalence.​
2. Decrease in tooth plaque accumulation.​
3. Maintenance of normal salivary pH levels.​
4. Positive shift in microbiome composition​

Efficacy was tested by PH testing, classification of gum bleeding (frequency) and classification of plaque occurrence.

## Purpose
The analysis aims to determine the effectiveness of the probiotic mouthwash in maintaining the health of the oral microbiome. 

## Methodology
The analysis includes:

- Data cleaning and preprocessing
- Statistical analysis.
- Visualization of data
- Dashboard preparation

## Analysis
Data Inspection: Examining dataset structure, missing values, and data types
Visualization: Utilizing histograms, scatter plots, and box plots for data exploration
Statistical Tests: MannWhitney test, AndersonDarling test, Q_Q_Plot,Mcmenar's test, Wilcoxon-sign-ranked test

## Files Used
PH.ipynb
Panel_DSPH.ipynb
Gum_bleeding_interactive.ipynb
Gum_bleeding_plt.ipynb
Main.ipynb
Mouth.datascience_1.ipynb
Plaque.ipynb
Pplaque.results.ipynb
Statistican_modules.py

## How to Use this application
1. Clone repository
2. Check if dependencies needed are installed on machine (requirements.txt)
3. Execute main.ipynb in a Jupyter Notebook environment.

## Conclusion
The analysis reveals there was not a significant change in PH values, gum bleeding and plaque values amongst all participants after the use of the probiotic mouthwash based on the individual pvalues obtained from the various protocols before and after the test period. However, there was a significant change in gum bleeding values when the responses of all the participants are put together based on the pvalues obtained after the use the probiotic mouthwash.This shows that probiotic mouthwash used did have little or no effect on maintaining the health of the oral microbiome.

## Group members
- Lily Konadu Gyammerah
- Dipto Gosswami
- Jetske Van Kampen
- Delinyah Koning
- Maryam Esmaeli 

## References
- M. Emile F. Apol, *Life Science & Technology, Hanze University of Applied Sciences, Groningen*(codes for Q-Q plot,MannWhitney test, AndersonDarling test )
- Edwards AL: Note on the “correction for continuity” in testing the significance of the difference between correlated proportions. Psychometrika 1948, 13(3):185–187.

*References on the use of mcnemars test*
- Fagerland, M. W., Lydersen, S., & Laake, P. (2013). The McNemar test for binary matched-pairs data: Mid-p and asymptotic are better than exact conditional. Retrieved April 14, 2018, from http://www.biomedcentral.com/1471-2288/13/91
- Gibbons, J. D., & Chakraborti, S. (2010). Nonparametric statistical inference. London: Chapman & Hall.
- Wikipedia contributors. (2018, April 29). McNemar's test. In Wikipedia, The Free Encyclopedia. Retrieved 12:24, August 15, 2018, from https://en.wikipedia.org/w/index.php?title=McNemar%27s_test&oldid=838855782

*References for biological concepts that this study was based on* 
1. Deo, P. N., & Deshmukh, R. (2019). Oral microbiome: Unveiling the fundamentals. Journal of oral and maxillofacial pathology : JOMFP, 23(1), 122–128. https://doi.org/10.4103/jomfp.JOMFP_304_18
2.	Romano, F., Perotto, S., Bianco, L., Parducci, F., Mariani, G. M., & Aimetti, M. (2020). Self-Perception of Periodontal Health and Associated Factors: A Cross-Sectional Population-Based Study. International journal of environmental research and public health, 17(8), 2758. https://doi.org/10.3390/ijerph17082758
3.	Seneviratne CJ, Zhang CF, Samaranayake LP. Dental plaque biofilm in oral health and disease. Chin J Dent Res. 2011;14(2):87-94. PMID: 22319749.
4.	Baliga, S., Muglikar, S., & Kale, R. (2013). Salivary pH: A diagnostic biomarker. Journal of Indian Society of Periodontology, 17(4), 461–465. https://doi.org/10.4103/0972-124X.118317
5.	Kotronia, E., Brown, H., Papacosta, A. O., Lennon, L. T., Weyant, R. J., Whincup, P. H., Wannamethee, S. G., & Ramsay, S. E. (2021). Oral health and all-cause, cardiovascular disease, and respiratory mortality in older people in the UK and USA. Scientific reports, 11(1), 16452. https://doi.org/10.1038/s41598-021-95865-z
6.	Tripathi, K., & Tripathi, R. (2022). Oral health and diabetes. National journal of maxillofacial surgery, 13(3), 319–321. https://doi.org/10.4103/njms.njms_197_22
7.	Chung, M., York, B. R., & Michaud, D. S. (2019). Oral Health and Cancer. Current oral health reports, 6(2), 130–137. https://doi.org/10.1007/s40496-019-0213-7
8.	Mark Welch J.L., Ramírez-Puebla S.T., Borisy G.G. Oral Microbiome Geography: Micron-Scale Habitat and Niche. Cell Host Microbe. 2020;28:160–168. doi: 10.1016/j.chom.2020.07.009
9.	Şenel S. An Overview of Physical, Microbiological and Immune Barriers of Oral Mucosa. Int. J. Mol. Sci. 2021;22:7821. doi: 10.3390/ijms22157821
10.	Shang L., Deng D., Buskermolen J.K., Janus M.M., Krom B.P., Roffel S., Waaijman T., van Loveren C., Crielaard W., Gibbs S. Multi-species oral biofilm promotes reconstructed human gingiva epithelial barrier function. Sci. Rep. 2018;8:16061. doi: 10.1038/s41598-018-34390-y
11.	Zhao H, Chu M, Huang Z, Yang X, Ran S, Hu B, Zhang C, Liang J. Variations in oral microbiota associated with oral cancer. Sci Rep. 2017 Sep 18;7(1):11773. doi: 10.1038/s41598-017-11779-9. PMID: 28924229; PMCID: PMC5603520
12.	Perera M, Al-Hebshi NN, Speicher DJ, Perera I, Johnson NW. Emerging role of bacteria in oral carcinogenesis: A review with special reference to perio-pathogenic bacteria J Oral Microbiol. 2016;8:32762
13.	Ma, G., Qiao, Y., Shi, H., Zhou, J., & Li, Y. (2022). Comparison of the Oral Microbiota Structure among People from the Same Ethnic Group Living in Different Environments. BioMed research international, 2022, 6544497. https://doi.org/10.1155/2022/6544497
14.	Lamont, R. J., Koo, H., & Hajishengallis, G. (2018). The oral microbiota: dynamic communities and host interactions. Nature reviews. Microbiology, 16(12), 745–759. https://doi.org/10.1038/s41579-018-0089-x
15.	Radaic, A., & Kapila, Y. L. (2021). The oralome and its dysbiosis: New insights into oral microbiome-host interactions. Computational and structural biotechnology journal, 19, 1335–1360. https://doi.org/10.1016/j.csbj.2021.02.010
16.	Loesche W. J. (1986). Role of Streptococcus mutans in human dental decay. Microbiological reviews, 50(4), 353–380. https://doi.org/10.1128/mr.50.4.353-380.1986
17.	Lemos, J. A., Palmer, S. R., Zeng, L., Wen, Z. T., Kajfasz, J. K., Freires, I. A., Abranches, J., & Brady, L. J. (2019). The Biology of Streptococcus mutans. Microbiology spectrum, 7(1), 10.1128/microbiolspec.GPP3-0051-2018. https://doi.org/10.1128/microbiolspec.GPP3-0051-2018
18.	How, K. Y., Song, K. P., & Chan, K. G. (2016). Porphyromonas gingivalis: An Overview of Periodontopathic Pathogen below the Gum Line. Frontiers in microbiology, 7, 53. https://doi.org/10.3389/fmicb.2016.00053
19.	Kurtzman, G. M., Horowitz, R. A., Johnson, R., Prestiano, R. A., & Klein, B. I. (2022). The systemic oral health connection: Biofilms. Medicine, 101(46), e30517. https://doi.org/10.1097/MD.0000000000030517
20.	Moye, Z. D., Zeng, L., & Burne, R. A. (2014). Fueling the caries process: carbohydrate metabolism and gene regulation by Streptococcus mutans. Journal of oral microbiology, 6, 10.3402/jom.v6.24878. https://doi.org/10.3402/jom.v6.24878
21.	Barranca-Enríquez, A., & Romo-González, T. (2022). Your health is in your mouth: A comprehensive view to promote general wellness. Frontiers in oral health, 3, 971223. https://doi.org/10.3389/froh.2022.971223
22.	Inchingolo, F., Inchingolo, A. M., Malcangi, G., De Leonardis, N., Sardano, R., Pezzolla, C., de Ruvo, E., Di Venere, D., Palermo, A., Inchingolo, A. D., Corriero, A., & Dipalma, G. (2023). The Benefits of Probiotics on Oral Health: Systematic Review of the Literature. Pharmaceuticals (Basel, Switzerland), 16(9), 1313. https://doi.org/10.3390/ph16091313 
23.	Etebarian, A., Sheshpari, T., Kabir, K., Sadeghi, H., Moradi, A., & Hafedi, A. (2023). Oral Lactobacillus species and their probiotic capabilities in patients with periodontitis and periodontally healthy individuals. Clinical and experimental dental research, 9(5), 746–756. https://doi.org/10.1002/cre2.740
24.	Hirasawa M, Kurita-Ochia T. Probiotic Potential of Lactobacilli Isolated from Saliva of Periodontally Healthy Individuals. Oral Health Prev Dent. 2020;18(1):563-570. doi: 10.3290/j.ohpd.a44693. PMID: 32515429.
25.	Mazziotta, C., Tognon, M., Martini, F., Torreggiani, E., & Rotondo, J. C. (2023). Probiotics Mechanism of Action on Immune Cells and Beneficial Effects on Human Health. Cells, 12(1), 184. https://doi.org/10.3390/cells12010184
26.	Lin CW, Chen YT, Ho HH, Hsieh PS, Kuo YW, Lin JH, Liu CR, Huang YF, Chen CW, Hsu CH, Lin WY, Yang SF. Lozenges with probiotic strains enhance oral immune response and health. Oral Dis. 2022 Sep;28(6):1723-1732. doi: 10.1111/odi.13854. Epub 2021 Mar 30. PMID: 33749084.
27.	Schlagenhauf, U., Rehder, J., Gelbrich, G., & Jockel-Schneider, Y. (2020). Consumption of Lactobacillus reuteri-containing lozenges improves periodontal health in navy sailors at sea: A randomized controlled trial. Journal of periodontology, 91(10), 1328–1338. https://doi.org/10.1002/JPER.19-0393
28.	Toiviainen, A., Jalasvuori, H., Lahti, E., Gursoy, U., Salminen, S., Fontana, M., Flannagan, S., Eckert, G., Kokaras, A., Paster, B., & Söderling, E. (2015). Impact of orally administered lozenges with Lactobacillus rhamnosus GG and Bifidobacterium animalis subsp. lactis BB-12 on the number of salivary mutans streptococci, amount of plaque, gingival inflammation and the oral microbiome in healthy adults. Clinical oral investigations, 19(1), 77–83. https://doi.org/10.1007/s00784-014-1221-6
