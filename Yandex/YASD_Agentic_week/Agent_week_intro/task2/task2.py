from sklearn.ensemble import GradientBoostingClassifier

def make_features(runes):
    rows = []
    for r in runes:
        v = [{'F':0,'W':1,'E':2}[c] for c in r]
        feat = []
        for i in range(5):
            for val in range(3):
                feat.append(int(v[i] == val))
        feat += [r.count('F'), r.count('W'), r.count('E')]
        for i in range(4):
            for a in range(3):
                for b in range(3):
                    feat.append(int(v[i]==a and v[i+1]==b))
        for i in range(5):
            for j in range(i+1,5):
                feat += [(v[i]+v[j])%3, (v[i]-v[j])%3, (v[i]*v[j])%3, int(v[i]==v[j])]
        rows.append(feat)
    return np.array(rows)

clf = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=3, random_state=42)
clf.fit(make_features(train['rune']), train['spell'])
preds = clf.predict(make_features(test['rune']))