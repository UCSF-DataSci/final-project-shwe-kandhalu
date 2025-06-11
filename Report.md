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

## 4. Results

- Training progress (log likelihood per iteration)  
- Model parameters (transition matrix, means) — you can include a table or matrix here  
- Example plot(s) of latent state over time for a participant (if you have visuals)  

---

## 5. Discussion

- Interpretation of latent states  
- Potential clinical relevance  
- Limitations and future work  

---

## 6. Conclusion

Summarize key takeaways.

---

## 7. References (optional)

---

## Appendix (optional)

- Code snippets or command-line examples to run your model