def temperature_colors(temperature):

    if temperature <= 0:
        return '\033[1;97m'

    elif 0 < temperature <= 30:
        return '\033[0;34m'

    elif 30 < temperature <= 50:
        return '\033[1;94m'

    elif 50 < temperature <= 60:
        return '\033[1;96m'

    elif 60 < temperature <= 70:
        return '\033[33m'

    elif 70 < temperature <= 75:
        return '\033[0;80m'

    elif 75 < temperature <= 80:
        return '\033[0;33m'

    elif 80 < temperature <= 90:
        return '\033[0;33'

    else:
        return '\033[31m'
