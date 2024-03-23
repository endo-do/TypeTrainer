import fs from 'fs';
import csvParser from 'csv-parser';
const csvFile = "ressources\\all_words.csv";
let cachedWords = [];

function initializeWordCache() {
    return new Promise((resolve, reject) => {
        const words = [];

        fs.createReadStream(csvFile)
            .pipe(csvParser())
            .on('data', (row) => {
                const word = row['word'];
                if (word) {
                    words.push(word);
                }
            })
            .on('end', () => {
                cachedWords = words;
                resolve();
            })
            .on('error', (err) => {
                reject(err);
            });
    });
}

function getRandomWordsFromCache(n) {
    if (cachedWords.length === 0) {
        throw new Error('Word cache is empty. Call initializeWordCache() first.');
    }
    const randomWords = [];
    for (let i = 0; i < n; i++) {
        const randomIndex = Math.floor(Math.random() * cachedWords.length);
        randomWords.push(cachedWords[randomIndex]);
    }
    return randomWords;
}