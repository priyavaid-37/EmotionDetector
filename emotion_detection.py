def emotion_detector(text_to_analyze):
    if text_to_analyze.strip() == "":
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    text = text_to_analyze.lower()

    emotions = {'anger': 0.05, 'disgust': 0.05, 'fear': 0.05, 'joy': 0.05, 'sadness': 0.05}

    if "sad" in text or "unhappy" in text:
        emotions['sadness'] = 0.85
    elif "mad" in text or "angry" in text:
        emotions['anger'] = 0.85
    elif "disgusting" in text or "disgusted" in text:
        emotions['disgust'] = 0.85
    elif "scared" in text or "afraid" in text:
        emotions['fear'] = 0.85
    elif "happy" in text or "glad" in text or "joy" in text:
        emotions['joy'] = 0.85

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }