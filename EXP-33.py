disease(diabetes, low_carb_diet).
disease(hypertension, low_salt_diet).
disease(heart_disease, low_fat_diet).
disease(gout, low_purine_diet).

suggest_diet(Disease, Diet) :- disease(Disease, Diet).
