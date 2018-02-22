#! /usr/bin/env python3


def preprocess():
    with open('pope_essay.txt', 'r') as f:
        text = f.read().replace('\n\n', '\n')
        lines = text.strip().split('\n')
        couplets = []
        print(len(lines))
        print(lines[-1])
        for i in range(0, len(lines), 2):
            line1 = lines[i].strip()
            line2 = lines[i+1].strip()
            couplets.append("\n".join([line1,line2]))
        return couplets


couplets = preprocess()

badopinions = ['DouthatNYT', 'BretStephensNYT', 'nytdavidbrooks']
