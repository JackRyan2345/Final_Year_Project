# Research Notebook: A comparative study of ML models for predicting traffic volume at selected Irish traffic locations using open traffic data, weather observations, and calendar features.

**Student:** Jack Ryan | **Supervisor:** Conor Ryan **Second Reader:** Alison O' Connor

**Project aim:** Compare ML models for forecasting hourly traffic volume 24 hours ahead, historical traffic volume, using weather and calendar features.

---

## Week 1 (23 Sep to 30 Sep 2026)

**Goals for the week**
- Review Literature on traffic prediction.

**Work completed**
- Read: Xueyan Yin, 2022 "Deep Learning on Traffic Prediction: Methods, Analysis, and Future Directions" on traffic prediction.

**Results / findings**
- Traffic prediction has a correlation in both spatial and temporal dimensions.
- Two categories of traffic prediction. Classic ML & Deep learning.
- Classic ML approaches are statistical models (ARIMA, SARIMA) and tree-based ensemble algorithms (RandomForest, XGBoost).
- Deep learning approaches are (LSTM, GRU, CNN).

**Limitations**
- There is a high data demand for Deep Learning.
- High computational complexity for Deep Learning.
- Lack of interpretability for Dep Learning as they are considered "Black-boxes".

**Problems and how I handled them**
- Finding Papers: Looking through Google Scholar.

**Time spent:** 3 hours

**Plan for next week**
- Read a second traffic prediction paper.

---

## Week 2 (1 Oct to 7 Oct 2026)

**Goals for the week**
- Continued review of Literature on traffic prediction.

**Work completed**
- Read: Mohammad Alam, 2025 "Road Traffic Congestion Prediction using AI/ML and Spatiotemporal Data: Literature Review".

**Results / findings**
- Traditional methods are simple and easy to interpret but assume lineararity and don't handle well with unusual events.
- Gradient-boosted decision trees improved predictions but need a lot of feature engineering and relies on good data quality.
- LSTM models capture long-term dependencies in time series traffic data, and CNNs extract local patterns.
- Short-term forecasting (minutes to hours) assumes future patterns resemble past ones, so it struggles with rare events such as accidents or extreme weather.
- Hybrid models are more accurate but tend to be more complex and takes longer to train.

**Limitations**
- Data quality problems (noise, missing data) reduce model performance.
- Deep Learning models need large amounts of data and heavy computation, and is hard to interpret.

**Problems and how I handled them**
- This paper focuses on congestion and not volume, therefore it talks about reinforcement learning and signal control. I therefore focused on traditional ML, Deep Learning and data quality.

**Time spent:** 3 hours

**Plan for next week**
- Read another literature paper for more research.

---

## Week 3 (8 Oct to 15 Oct 2026)

**Goals for the week**
- Read a literature paper for time-series and traffic prediction.
- Start preparing for my week 8/9 presentation.

**Work completed**
- Read Amar Mahmoud's study on deep learning for time series.
- Started preparing for the week 8/9 presentations.


**Results / findings**
- Deep Learning models can learn complex patterns and mappings  and do not require stationary data.
- Deep Learning modelshandle input variables and features such as weather, calendar features and hourly inputs, which suits my project.
- Got started with the slide deck for my presentation.

**Limitations**
- Data volume matters for Deep Learning models, will have to see how much data I will need to use.

**Problems and how I handled them**
-

**Time spent:** 4 hours.

**Plan for next week**
- Make more progress on the presentation.
- Research models.
- Obtain traffic & weather data.

---

## Week 4 (16 Oct to 23 Oct 2026)

**Goals for the week**
- Make progress on the presentation.
- Research models.
- Obtain traffic and weather data.

**Work completed**
- Made progress on presentation.
- Identified potential 7 models.
- Obtained weather data.

**Results / findings**
- Have slides created for the presentation, asked for feedback from Conor.
- The papers I've read have Identified ARIMA, SARIMA, RandomForrest, XGBoost. LSTM, GRU, 1D CNN as potential models for the project.
- Have downloaded weather data from Met Eireann weather stations. Shannon Airport & Ardnacrusha.
- Traffic data is available to the public & have identified 22 counters for the project.

**Limitations**
- Current weather data is actual data not forecasted, found places where forecasts are but needs more research.
- Traffic data has missing values, needs data cleaning.

**Problems and how I handled them**
- Access errors when trying to bulk download traffic data, overcame by finding csv/html downloads of the data from each counter.
- Have actual weather data not forecasted, found where forecasted data is but needs research.

**Time spent:** 5 hours

**Plan for next week**
- Finish presentation.
- Obtain traffic data.

---

## Week 5 (24 Oct to 31 Oct 2026)

**Goals for the week**
- Finish presentation.
- Obtain traffic data.

**Work completed**
- Finished presentation.
- Downloaded some individual monthly traffic volume files.

**Results / findings**
- Found that the traffic data is stored as a html file.
- Presentation runs over the why, plan, research, work done and what is needed to be done.

**Limitations**
- Only able to to download traffic data file one at a time at the moment.

**Problems and how I handled them**
- 

**Time spent:** 5 hours

**Plan for next week**
- Present my project to Conor and Alison.
- Find a way to bulk download traffic data file.

---

## Week 6 (31 Oct to 7 Nov 2026)

**Goals for the week**
- Present project
- Find a way to bulk donwload traffic data

**Work completed**
- 

**Results / findings**
- 

**Limitations**
- 

**Problems and how I handled them**
- 

**Time spent:** 

**Plan for next week**
- 