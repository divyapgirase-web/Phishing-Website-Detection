from urllib.parse import urlparse


def extract_features(url):
    features = []

    # 1. URL length
    features.append(len(url))

    # 2. Number of dots
    features.append(url.count("."))

    # 3. Number of hyphens
    features.append(url.count("-"))

    # 4. Number of @ symbols
    features.append(url.count("@"))

    # 5. Number of slashes
    features.append(url.count("/"))

    # 6. Number of question marks
    features.append(url.count("?"))

    # 7. Number of equal signs
    features.append(url.count("="))

    # 8. Number of percent signs
    features.append(url.count("%"))

    # 9. Number of underscores
    features.append(url.count("_"))

    return features