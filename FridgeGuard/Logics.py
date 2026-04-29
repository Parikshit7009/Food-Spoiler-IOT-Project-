import config

def get_status(diff):
    if diff > config.SPOILED_THRESHOLD:
        return "SPOILED"
    elif diff > config.WARNING_THRESHOLD:
        return "WARNING"
    else:
        return "SAFE"

def update_baseline(baseline, gas):
    return int(0.98 * baseline + 0.02 * gas)