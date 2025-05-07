# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model was created by Nick Newby for the Udacity Machine Learning DevOps course through WGU. It utilizes the scikit-learn RandomForestClassifier model with default parameters.

## Intended Use

This model uses census data to predict whether an individual earns over $50,000 USD anually.

## Training Data

80% of the original 'census.csv' dataset was used to train the model. The dataset is comprised of 32562 rows of data eith the following 15 columns:
- Age
- Workclass
- fnlgt
- education
- education-num
- marital-status
- occupation
- relationship
- race
- sex
- capital-gain
- capital-loss
- hours-per-week
- native-country
- salary

## Evaluation Data

The remaining 20% of data was used to test the model.

## Metrics

The following metrics and scores were produced by the model:
- Precision: 0.7431
- Recall: 0.6372
- F1 Score: 0.6861

## Ethical Considerations

Considering the relatively small dataset, care should be taken in regards to any inhereny biases resulting from the data selection process. A larger dataset to be used for training the model would lead to results less susceptible to selection biases.

## Caveats and Recommendations

The dataset set is from 1994, meaning the results of this model will be significantly out of date until new training data can be used to update the assumptions in the model. Many things can change in 30 years, and this model is most likely not viable when compared to more recent datasets considering not only the effects of inflation on the income levels of individuals, but also shifting populations and demographics within those populations.