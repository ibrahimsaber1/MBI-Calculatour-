# BMI Calculator

## Overview

This Python script calculates the Body Mass Index (BMI) based on the user's weight and height in metric units. The BMI is then used to categorize the user's weight status, providing feedback on whether they are underweight, normal, overweight, or obese.

## How It Works

1. **Input:** The script prompts the user to enter their name, weight (in kilograms), and height (in meters).
2. **Calculation:** The BMI is calculated using the formula:
   \[
   \text{BMI} = \frac{\text{mass (kg)}}{\text{height (m)}^2}
   \]
3. **Output:** Based on the calculated BMI, the script provides a categorization of the user's weight status and gives additional information about healthy BMI ranges.

## BMI Categories

- **Severe Thinness:** BMI < 16
- **Moderate Thinness:** 16 ≤ BMI < 17
- **Mild Thinness:** 17 ≤ BMI < 18.5
- **Normal:** 18.5 ≤ BMI < 25
- **Overweight:** 25 ≤ BMI < 30
- **Obese Severely:** 30 ≤ BMI < 35
- **Obese Morbidly:** BMI ≥ 35

## Usage

To run the script:

1. Ensure you have Python installed on your system.
2. Copy the script into a Python file (e.g., `bmi_calculator.py`).
3. Run the script using a Python interpreter.

```bash
python bmi_calculator.py
```
4. Follow the prompts to enter your name, weight, and height.
5. The script will display your BMI and corresponding weight category.

## Notes
- The script uses metric units: kilograms for weight and meters for height.
- The healthy BMI range is between 18.5 kg/m² and 25 kg/m².

## References
- The BMI categories and ranges are based on information from [this calculator](https://www.calculator.net/bmi-calculator.html).
- This README provides an overview of the script, explains how it works, lists the BMI categories, and gives instructions on how to run the script.
