#!/usr/bin/node

const fs = require('fs');

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const outputPath = process.argv[4];

fs.readFile(file1Path, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1Path}: ${err}`);
    return;
  }

  fs.readFile(file2Path, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2Path}: ${err}`);
      return;
    }

    const concatData = data1 + data2;
    fs.writeFile(outputPath, concatData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${outputPath}: ${err}`);
      }
    });
  });
});
