# Weather Prediction using Bayesian Probability

# Dataset
total_days = 20
rain = 8
not_rain = 12

cloudy_rain = 7
cloudy_not_rain = 3

# Prior probabilities
p_rain = rain / total_days
p_not_rain = not_rain / total_days

# Conditional probabilities
p_cloudy_rain = cloudy_rain / rain
p_cloudy_not_rain = cloudy_not_rain / not_rain

# Probability of Cloudy
p_cloudy = (p_cloudy_rain * p_rain) + \
           (p_cloudy_not_rain * p_not_rain)

# Bayes' Theorem
p_rain_cloudy = (p_cloudy_rain * p_rain) / p_cloudy
p_not_rain_cloudy = (p_cloudy_not_rain * p_not_rain) / p_cloudy

# Display results
print("P(Rain) =", p_rain)
print("P(Not Rain) =", p_not_rain)

print("P(Cloudy | Rain) =", p_cloudy_rain)
print("P(Cloudy | Not Rain) =", p_cloudy_not_rain)

print("P(Rain | Cloudy) =", p_rain_cloudy)
print("P(Not Rain | Cloudy) =", p_not_rain_cloudy)

# Prediction
if p_rain_cloudy > p_not_rain_cloudy:
    print("Predicted Weather = Rain")
else:
    print("Predicted Weather = Not Rain")