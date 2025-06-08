# NASA-TLX-Analyzer

This Python script allows the analysis and visualization of the results of the NASA-TLX (Task Load Index) questionnaire, used to measure the workload perceived by participants in different experimental conditions.

- Features:

1. Calculation of the final TLX score, with or without the use of individual weights per dimension;

2. Interactive graphical visualization with the following graphs:

3. Average bars per dimension;

4. Boxplot per dimension;

5. Radar chart with hexagonal grid (Spider Chart);

7. Final TLX per participant.

Obs: Expected CSV file format

The .csv file to be analyzed must follow the following format:
Participant Mental Condition Physical Temporal Performance Effort Frustration Mental_Weight Physical_Weight ...
P1 A 70 60 65 80 75 55 5 3 ...
P2 B 50 40 60 70 60 45 4 2 ...
... ... ... ... ... ... ... ... ... ... ...

The Mental, Physical, Temporal, Performance, Effort, Frustration columns are mandatory.

The Weight_<Dimension> columns are optional and are only used when the analysis is performed with weights.

The dimension scores must be between 0 and 100.

The weights must be on a defined scale (e.g. 0 to 5), and are used to weigh the relative importance of each dimension per participant.

- How to use:

1. Install the necessary packages:

2. pip install pandas matplotlib seaborn numpy

3. Run the script:

python nasa_tlx_analyzer.py

4. Follow the interactive instructions:

- Select the CSV file with the data;

- Choose whether to use weights;

- Choose the graphs to display.

Visual resources:

- Graphs displayed in separate windows, without overlapping;

- Unified color palette across all graphs;

- Bold titles with enlarged font;

- Radar graph with hexagonal grid, "Spider Chart" style.

About NASA-TLX

The NASA Task Load Index is a subjective instrument developed by NASA to measure workload based on six dimensions:

1 - Mental Demand,

2 - Physical Demand,

3 - Time Demand,

4 - Perceived Performance,

5 - Effort,

6 - Frustration.

This script automates the analysis of these data, facilitating comparison between different experimental conditions.
