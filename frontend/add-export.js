const fs = require('fs');
const path = require('path');

function processFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  if (!/^\s*(import|export)\s/m.test(content)) {
    fs.appendFileSync(filePath, '\nexport {};\n');
    console.log('Patched:', filePath);
  }
}

function walkDir(dir) {
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      walkDir(fullPath);
    } else if (/\.(ts|tsx)$/.test(file)) {
      processFile(fullPath);
    }
  });
}

walkDir(path.join(__dirname, 'src'));
console.log('Done!');