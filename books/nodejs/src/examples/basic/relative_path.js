const path = require('path');

console.log(__filename);
console.log(__dirname);

const root = path.dirname(__dirname)
console.log(root);

const templates = path.join(root, 'templates');
console.log(templates);

const rel_path_to_file = path.join(root, 'templates', 'main.html');
console.log(rel_path_to_file);
