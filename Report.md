# Modeling Latent Health States Using Hidden Markov Models

## 1. Overview
This project applies a Hidden Markov Model (HMM) to model latent health states in individuals using a combination of hormonal birth control usage, mood tracking, and metabolic biomarker data. The goal is to uncover unobserved health states that evolve over time.

---

## 2. Data Description

### 2.1 Hormonal Birth Control (BC) Data

- **Total records:** 1000 participants  
- **Columns:**
  - `participant_id` (int): Unique identifier
  - `age` (int): Age of participant
  - `bmi` (float): Body Mass Index
  - `hormonal_bc_use` (object): Whether participant used hormonal birth control
  - `bc_type` (object): Type of birth control used (e.g., Pill, IUD) — 39.8% missing
  - `duration_months` (int): Duration of birth control use in months
  - `smoking_status` (object): Smoking behavior
  - `chronic_conditions` (object): Any known chronic conditions — 70.1% missing

- **Missing Data Summary:**
  - `bc_type`: 398 missing (39.8%)
  - `chronic_conditions`: 701 missing (70.1%)

---

### 2.2 Mood Tracking Data

- **Total records:** 1000 entries
- **Columns:**
  - `participant_id` (int)
  - `date` (object): Date of entry (later parsed to datetime)
  - `mood_score` (int): Scale 1–10
  - `notes` (object): Qualitative notes (e.g., "Tired", "Calm")

- **Summary Statistics:**
  - `mood_score`: Median = 5, Range = 1–10
  - `notes`: 8 unique qualitative tags

---

### 2.3 Metabolic Markers Data

- **Total records:** 1000 longitudinal biomarker measurements
- **Columns:**
  - `participant_id` (int)
  - `date` (object): Measurement date
  - `fasting_glucose` (int)
  - `cholesterol_total` (int)
  - `hdl` (int): High-density lipoprotein
  - `ldl` (int): Low-density lipoprotein
  - `triglycerides` (int)

- **Statistics:**
  - `fasting_glucose`: Median = 85 mg/dL
  - `cholesterol_total`: Median = 176 mg/dL
  - `hdl`: Median = 55 mg/dL
  - `ldl`: Median = 110 mg/dL
  - `triglycerides`: Median = 130 mg/dL

All datasets were merged and time-sorted by `participant_id` and `date` before HMM training.

---

## 3. Methods

### 3.1 Latent State Model  
- Model type: Gaussian HMM  
- Number of states: 3 (low, moderate, high risk)  
- Training iterations: 100  

### 3.2 Data Processing  
- Sorting by participant and date  
- Feature selection  

---

## 4. Basic Results

- Age and BMI Distributions
Age Distribution (Left Panel)
The age distribution of participants is relatively uniform across the range of approximately 18 to 44 years, suggesting good representation across different age groups. Notable peaks occur around ages 20, 25, 30, 35, 40, and 44, which may reflect recruitment patterns, life stages, or enrollment targets. The kernel density estimate (KDE) shows a fairly flat curve, indicating a roughly uniform sample rather than the typical age distribution observed in the general population.

BMI Distribution (Right Panel)
The BMI distribution is unimodal with a slight right skew, typical for adult populations. The peak BMI range lies between 22 and 27, mostly within or just above the normal range. A small right tail indicates some overweight or obese individuals (BMI > 30), though these represent a minority. The smooth KDE suggests a well-sampled continuous distribution appropriate for use in regression or predictive modeling.

- Mood Scores Over Time (Longitudinal)
This figure presents longitudinal mood scores for selected participants over approximately 2.5 years. Mood scores demonstrate high variability across time points.

Participant 1007 exhibits relatively stable mood scores clustered in the mid-to-high range.

Participant 1013 shows wider fluctuations, including sustained periods of lower mood scores.

Interpretation:
The observed mood variability supports further analysis of temporal trends, seasonality, and associations with time-varying exposures such as changes in birth control or life events. The individual differences highlight the potential need for personalized modeling approaches or mixed models incorporating random effects.

---

## 5. Discussion

This exploratory analysis highlights important characteristics of the study cohort and the data quality across hormonal birth control use, mood tracking, and metabolic markers. The age distribution shows a relatively even spread across adult reproductive ages, which supports the generalizability of the findings. The BMI distribution, while mostly normal, has a slight right skew indicating some participants with overweight or obesity, which is typical for this population.

The overwhelming predominance of pill use among birth control types reflects common usage patterns seen in broader populations, likely influenced by factors such as accessibility and prescribing practices. However, the imbalance in birth control method groups suggests that caution is needed in modeling to avoid bias and low statistical power in smaller categories.

Longitudinal mood data reveals considerable variability both within and between individuals, underscoring the dynamic nature of mood over time. This supports the need for models that account for temporal changes and individual differences, such as mixed-effects or time series models.

Overall, the continuous variables like age and BMI appear suitable for regression analyses without the need for categorization, preserving statistical power. The metabolic marker correlations and distributions look consistent with expected biological patterns, suggesting reliable data quality.

Limitations include potential recruitment bias and the uneven distribution of birth control methods, which may affect subgroup analyses. The mood data, while longitudinal, covers only a subset of participants and may be influenced by self-reporting biases.

In conclusion, this data exploration provides a solid foundation for further analyses investigating the relationships between hormonal birth control, metabolic health, and mood dynamics in this cohort.