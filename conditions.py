def condition(cond):

    if cond == "Sunny":
        return '\033[93m'
    elif cond == "Clear":
        return '\033[0m'
    elif cond == "Partly cloudy":
        return '\033[37m'
    elif cond == "Cloudy":
        return '\033[90m'
    elif cond == "Overcast":
        return '\033[90m'
    elif cond == "Mist":
        return '\033[96m'
    elif cond == "Patchy rain possible":
        return '\033[96m'
    elif cond == "Patchy snow possible":
        return '\033[37m'
    elif cond == "Patchy sleet possible":
        return '\033[37m'
    elif cond == "Patchy freezing drizzle possible":
        return '\033[36m'
    elif cond == "Thundery outbreaks possible":
        return '\033[93m'
    elif cond == "Blowing snow":
        return '\033[37m'
    elif cond == "Blizzard":
        return '\033[34m'
    elif cond == "Fog":
        return '\033[90m'
    elif cond == "Freezing Fog":
        return '\033[37m'
    elif cond == "Patchy light drizzle":
        return '\033[37m'
    elif cond == "Light drizzle":
        return '\033[96m'
    elif cond == "Freezing drizzle":
        return '\033[96m'
    elif cond == "Heavy freezing drizzle":
        return '\033[34m'
    elif cond == "Patchy light rain":
        return '\033[96m'
    elif cond == "Light rain":
        return '\033[96m'
    elif cond == "Moderate rain at times":
        return '\033[94m'
    elif cond == "Moderate rain":
        return '\033[94m'
    elif cond == "Heavy rain at times":
        return '\033[34m'
    elif cond == "Heavy rain":
        return '\033[34m'
    elif cond == "Light freezing rain":
        return '\033[96m'
    elif cond == "Moderate or heavy freezing rain":
        return '\033[34m'
    elif cond == "Light sleet":
        return '\033[96m'
    elif cond == "Moderate or heavy sleet":
        return '\033[34m'
    elif cond == "Patchy light snow":
        return '\033[37m'
    elif cond == "Light snow":
        return '\033[37m'
    elif cond == "Patchy moderate snow":
        return '\033[94m'
    elif cond == "Moderate snow":
        return '\033[94m'
    elif cond == "Patchy heavy snow":
        return '\033[37m'
    elif cond == "Heavy snow":
        return '\033[34m'
    elif cond == "Ice pellets":
        return '\033[94m'
    elif cond == "Light rain shower":
        return '\033[96m'
    elif cond == "Moderate or heavy rain shower":
        return '\033[34m'
    elif cond == "Torrential rain shower":
        return '\033[34m'
    elif cond == "Light sleet showers":
        return '\033[96m'
    elif cond == "Moderate or heavy sleet showers":
        return '\033[37m'
    elif cond == "Light snow showers":
        return '\033[37m'
    elif cond == "Moderate or heavy snow showers":
        return '\033[36m'
    elif cond == "Light showers of ice pellets":
        return '\033[94m'
    elif cond == "Moderate or heavy showers of ice pellets":
        return '\033[36m'
    elif cond == "Patchy light rain with thunder":
        return '\033[93m'
    elif cond == "Moderate or heavy rain with thunder":
        return '\033[93m'
    elif cond == "Patchy light rain with thunder":
        return '\033[93m'
    elif cond == "Moderate or heavy rain with thunder":
        return '\033[93m'
    elif cond == "Patchy light snow with thunder":
        return '\033[93m'
    elif cond == "Moderate or heavy snow with thunder":
        return '\033[93m'
    else:
        return '\033[0m'
