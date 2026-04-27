# Example: Healthcare Intake

## High-value facts

- patient identity
- age / sex if relevant
- main symptom
- onset time
- allergies / medications
- severity signals

## Good use of the pattern

- SLM tracks the facts and contradictions
- LLM handles the bedside manner
- tools verify eligibility, schedule windows, and prior records only when identity is meaningful enough

## Example confirmation ladder

1. Who is the patient?
2. Can you confirm the full name and date of birth?
3. I found `candidate record X`. Is that the right person?
4. If not, please spell the surname.
