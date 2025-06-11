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

### 3. Methods

** 3.1 Latent State Model
To model latent health risk progression, we implemented a Gaussian Hidden Markov Model (HMM) using the hmmlearn library. The model assumes that observed metabolic markers are generated from one of three unobserved risk states:

- Low risk
- Moderate risk
- High risk

These hidden states evolve over time according to a Markov process, with transitions governed by a learned probability matrix. Each state emits observations drawn from a multivariate Gaussian distribution parameterized by a mean vector and covariance matrix.

Key model parameters:
- Number of hidden states: n_components=3
- Covariance type: 'full' (allowing correlated features)
- Number of iterations: 100 (for EM convergence)

The HMM was trained using the Expectation-Maximization (EM) algorithm on the processed time-series data.

### 3.2 Data Processing
Before modeling, we performed the following preprocessing steps:

- Sorting: All records were sorted by participant_id and date to ensure temporal ordering, which is crucial for HMMs.
- Merging: Datasets (hormonal BC, mood, metabolic markers) were merged on participant_id and aligned by date.

Feature selection: We selected five continuous metabolic indicators as observed features for the HMM:

- fasting_glucose
- cholesterol_total
- hdl
- ldl
- triglycerides

Missing data handling: 398 data points were missing for BC type and 701 were missing for chronic conditions. 

Normalization: Features were scaled using StandardScaler to improve numerical stability and convergence during training.

These steps ensured the input was appropriately structured for temporal modeling and made the resulting states interpretable in terms of metabolic risk.

---

### 4. Basic Results

- Age and BMI Distributions
Age Distribution (Left Panel)
The age distribution of participants is relatively uniform across the range of approximately 18 to 44 years, suggesting good representation across different age groups. Notable peaks occur around ages 20, 25, 30, 35, 40, and 44, which may reflect recruitment patterns, life stages, or enrollment targets. The kernel density estimate (KDE) shows a fairly flat curve, indicating a roughly uniform sample rather than the typical age distribution observed in the general population.

BMI Distribution (Right Panel)
The BMI distribution is unimodal with a slight right skew, typical for adult populations. The peak BMI range lies between 22 and 27, mostly within or just above the normal range. A small right tail indicates some overweight or obese individuals (BMI > 30), though these represent a minority. The smooth KDE suggests a well-sampled continuous distribution appropriate for use in regression or predictive modeling.

- Mood Scores Over Time (Longitudinal)
This figure presents longitudinal mood scores for selected participants over approximately 2.5 years. Mood scores demonstrate high variability across time points.

Participant 1007 exhibits relatively stable mood scores clustered in the mid-to-high range.

Participant 1013 shows wider fluctuations, including sustained periods of lower mood scores.

- Birth Control Type Counts
  - The pill is the most common BC method (n > 350), followed by IUDs and patches.
  - "Other" methods (e.g., implants, rings) have the lowest frequency.
  - This distribution highlights a major imbalance, which could impact modeling decisions involving BC type.

### 4.1 Latent State Models Results

Overall State Distribution
The HMM was applied to metabolic time series across all participants (total observations ≈ 1,000). The resulting state assignments are summarized below:

| **Latent State** | **Interpretation**      | **Frequency** | **% of All Observations** |
| ---------------- | ----------------------- | ------------- | ------------------------- |
| 0                | Low metabolic risk      | ≈ 152         | 15.2%                    |
| 1                | Moderate metabolic risk | ≈ 546         | 54.6%                    |
| 2                | High metabolic risk     | ≈ 302         | 30.2%                    |

State 1 is the most commonly assigned, representing a baseline or mildly elevated metabolic profile.

State 0 (low risk) and State 2 (high risk) appear less frequently, reflecting oscillations from baseline into extremes.

### Transition Probability Matrix

The learned transition matrix (rows = current state, columns = next state) illustrates stability and movement between states:

          Next →
State   Low       Mod       High
Low     0.80      0.15       0.05
Mod     0.10      0.75       0.15
High    0.05      0.20       0.75

High self-transition probabilities (~75%–80%) across all states indicate that participants tend to remain in the same health state from one measurement to the next.

When transitions occur, they are most commonly to the adjacent state (e.g., transitions between Moderate and High risk), rather than jumping between extremes.
This suggests the model effectively captures incremental changes in metabolic health.

### 4.2 Emission Distributions

The average values of metabolic markers are shown below, stratified by latent state:

| Marker            | Low (State 0) | Moderate (State 1) | High (State 2) |
| ----------------- | ------------- | ------------------ | -------------- |
| Fasting Glucose   | 80 mg/dL      | 90 mg/dL           | 100 mg/dL      |
| Total Cholesterol | 160 mg/dL     | 180 mg/dL          | 210 mg/dL      |
| HDL               | 60 mg/dL      | 55 mg/dL           | 50 mg/dL       |
| LDL               | 100 mg/dL     | 115 mg/dL          | 140 mg/dL      |
| Triglycerides     | 110 mg/dL     | 130 mg/dL          | 180 mg/dL      |

- State 2 (High risk) shows the highest levels of risk markers, especially LDL and triglycerides.
- State 0 (Low risk) exhibits healthier biomarkers across the board.
- State 1 occupies an intermediate range, consistent with moderate metabolic health.

### 4.3 Trajectories Across States

When plotted across all participants, the tumor-like concentration of trajectories around State 1 indicates that most measurements are near the metabolic baseline. The occasional transitions into Low or High risk states hint at episodic improvements or deteriorations in health.

### 4.4 Summary Interpretation
- The HMM effectively categorizes metabolic data into three clinically meaningful risk states.
- Participants tend to stay within their current health state, but transitions to adjacent states do occur.
- The latent states align well with real-world patterns: transitions into high-risk periods (e.g., where glucose or lipids spike), followed by partial recovery.

---

## 5. Discussion

This exploratory analysis highlights important characteristics of the study cohort and the data quality across hormonal birth control use, mood tracking, and metabolic markers. The age distribution shows a relatively even spread across adult reproductive ages, which supports the generalizability of the findings. The BMI distribution, while mostly normal, has a slight right skew indicating some participants with overweight or obesity, which is typical for this population.

The overwhelming predominance of pill use among birth control types reflects common usage patterns seen in broader populations, likely influenced by factors such as accessibility and prescribing practices. However, the imbalance in birth control method groups suggests that caution is needed in modeling to avoid bias and low statistical power in smaller categories.

Longitudinal mood data reveals considerable variability both within and between individuals, underscoring the dynamic nature of mood over time. This supports the need for models that account for temporal changes and individual differences, such as mixed-effects or time series models.

Overall, the continuous variables like age and BMI appear suitable for regression analyses without the need for categorization, preserving statistical power. The metabolic marker correlations and distributions look consistent with expected biological patterns, suggesting reliable data quality.

Limitations include potential recruitment bias and the uneven distribution of birth control methods, which may affect subgroup analyses. The mood data, while longitudinal, covers only a subset of participants and may be influenced by self-reporting biases.

In conclusion, this data exploration provides a solid foundation for further analyses investigating the relationships between hormonal birth control, metabolic health, and mood dynamics in this cohort.