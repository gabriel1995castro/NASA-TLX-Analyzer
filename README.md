# NASA-TLX-Analyzer

This Python script provides a comprehensive tool for analyzing and visualizing the results of the NASA-TLX (Task Load Index) questionnaire. It's designed to measure the perceived workload of participants across different experimental conditions.

---

## ✨ Features

* **Final TLX Score Calculation**: Computes the final TLX score, with or without considering individual weights for each dimension.
* **Interactive Graphical Visualization**: Generates a variety of insightful and interactive charts:
    * Average bars per dimension
    * Boxplot per dimension
    * Radar chart with a hexagonal grid (Spider Chart)
    * Final TLX score per participant

---

## 📋 Expected CSV File Format

For the script to work correctly, your `.csv` file must adhere to the following format.

| Participant | Condition | Mental | Physical | Temporal | Performance | Effort | Frustration | Mental\_Weight | Physical\_Weight | ... |
| :---------- | :-------- | :----- | :------- | :------- | :---------- | :----- | :---------- | :------------- | :--------------- | :-- |
| P1          | A         | 70     | 60       | 65       | 80          | 75     | 55          | 5              | 3                | ... |
| P2          | B         | 50     | 40       | 60       | 70          | 60     | 45          | 4              | 2                | ... |
| ...         | ...       | ...    | ...      | ...      | ...         | ...    | ...         | ...            | ...              | ... |

**Important Notes:**

* The columns **`Participant`**, **`Condition`**, **`Mental`**, **`Physical`**, **`Temporal`**, **`Performance`**, **`Effort`**, and **`Frustration`** are **mandatory**.
* The `Weight_<Dimension>` columns are **optional**. They are only used when the analysis is performed with weights.
* Dimension scores must be on a scale of **0 to 100**.
* Weights should be on a defined scale (e.g., 0 to 5) and represent the relative importance of each dimension for a participant.

---

## 🚀 How to Use

Follow these steps to get started:

1.  **Install the necessary packages:**
    ```bash
    pip install pandas matplotlib seaborn numpy
    ```

2.  **Run the script:**
    ```bash
    python nasa_tlx_analyzer.py
    ```

3.  **Follow the interactive instructions in the terminal:**
    * Select the CSV file containing your data.
    * Choose whether to use weights in your analysis.
    * Select the specific graphs you wish to display.

---

## 🎨 Visual Features

* **Dedicated Windows**: Each graph is displayed in a separate window to prevent overlapping and allow for clear comparisons.
* **Unified Color Palette**: A consistent color scheme is used across all graphs for a cohesive look.
* **Enhanced Titles**: Graph titles are bold and feature an enlarged font for better readability.
* **Hexagonal Radar Chart**: The radar graph (Spider Chart) is rendered with a unique hexagonal grid for improved visual clarity.

---

## ℹ️ About NASA-TLX

The **NASA Task Load Index** is a widely used, subjective assessment tool developed by the NASA Ames Research Center. It measures a person's perceived workload based on six distinct dimensions:

1.  🧠 **Mental Demand**: How much mental and perceptual activity was required?
2.  💪 **Physical Demand**: How much physical activity was required?
3.  ⏳ **Temporal Demand**: How much time pressure did the participant feel?
4.  🎯 **Perceived Performance**: How successful was the participant in accomplishing the goals?
5.  🥵 **Effort**: How hard did the participant have to work (mentally and physically)?
6.  😤 **Frustration**: How insecure, discouraged, or irritated versus secure and content did the participant feel?

This script automates the analysis of this data, making it easier to interpret and compare results between different conditions.
